# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    names_list = []
    for name in names:
        only_name = name.strip("\n")
        names_list.append(only_name)
# print(names_list)

# Replace the [name] placeholder with the actual name.
with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()
# print(letter)

# Save the letters in the folder "ReadyToSend".
for name in names_list:
    individual_letter = letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as file:
        file.write(individual_letter)
