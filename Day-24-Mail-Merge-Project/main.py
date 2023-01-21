#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    draft_letter = starting_letter.read()
with open("./Input/Names/invited_names.txt") as name_list:
    names = name_list.readlines()

new_names = []

for name in names:
    new_name = name.strip()
    new_names.append(new_name)

#TODo print names in each letter
for new_name in new_names:
    with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as output_letter:
        output_letter.write(draft_letter.replace("[name]", new_name))


