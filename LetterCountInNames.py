""" Displays number of times a given letter appears in a list of inputted names """

# Initializes name list and name input
names_list = []
name_input = 'y'

print('Search a given letter within a user-inputted set of names\n')

# Until 'q' is typed, program continues to accept names
while name_input != 'x':
    name_input = input('Enter a name (x to finish input): ')
    names_list.append(name_input)

# Initializes letter count
letter = input('\nEnter a letter: ')
letter = letter.lower()
letter_num = 0

# Lower-case for simplicity
for k in range(len(names_list) - 1):
    names_list[k] = names_list[k].lower()

# Iteration goes through list in search of given character
count = 0
for k in range(len(names_list) - 1):
    count = count + names_list[k].count(letter)

# Outputs resulting letter count
print("\nAppearance of letter", "'" + letter + "'" + ":", count)
