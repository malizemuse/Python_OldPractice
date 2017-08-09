""" Checks if given string is a palindrome """

print('Determine if the given string is a palindrome')
print('  (Enter) to exit\n')

# Variable only serves purpose of terminating program when 'enter' is pressed
empty = ''

# Gets string from user input
chars = input('Enter string to check:')

# Gets next string from user (until user exits)
while chars != empty:

    # List of string and its reverse compared
    check_init = list(chars)
    check_final = list(reversed(chars))

    # Results whether palindrome or not
    if check_init == check_final:
        print('\n ' + chars + ' is a palindrome\n')
    else:
        print('\n ' + chars + ' is NOT a palindrome\n')

    # Next user input
    chars = input('Enter string to check:')
