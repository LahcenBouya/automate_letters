
#get latters
with open("mail_merge/input/letters/starting_letters.txt") as letters_file:
    text = letters_file.read()



#take name of receiver
with open("mail_merge/Names/invited_names.txt") as names_file:
    content = names_file.readlines()


#change names in the main letter
for i in content:
    name = i.strip()
    #check the empty lines
    if not name:
        continue
    letter = text.replace("{name}", name).replace("{signature}", "Lahcen Bouya")
    with open(f"mail_merge/output/Ready_to_send/{name}.txt", "w+") as send_letter:
        send_letter.write(letter)