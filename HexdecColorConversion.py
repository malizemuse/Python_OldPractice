""" Converts 6-digit hexadecimal color codes to base 10 """

# Inits necessary variables
hex_split = []
hex_val = {'a':10, 'b':11, 'c': 12, 'd':13, 'e':14, 'f':15}

print('Convert 6-digit hexadecimal color code to base 10 values (red, green, blue)\n')

# User input of bexadecimal color code
hexdec = input('Enter a color in hexadecimal code: ')

# Splits hexadecimal into respective red, green, blue values
for k in range(0, len(hexdec), 2):
    hex_split.append(hexdec[k : k + 2])

# Lowercases all letters for simplicity in dictionary values
for k in range(len(hex_split)):
    hex_split[k] = hex_split[k].lower()

# Red
red = list(hex_split[0])
# Assigns hex_val dictionary value if a-f
for k in range(len(red)):
    if red[k].isdigit() == False:
        red[k] = hex_val[red[k]]
# Converts values to int
for k in range(len(red)):
    red[k] = int(red[k])
# Base 10 algorithm
red_b10 = red[0]*16 + red[1]

# Green
green = list(hex_split[1])
# Assigns hex_val dictionary value if a-f
for k in range(len(green)):
    if green[k].isdigit() == False:
        green[k] = hex_val[green[k]]
# Converts values to int
for k in range(len(green)):
    green[k] = int(green[k])
# Base 10 algorithm
green_b10 = green[0]*16 + green[1]

# Blue
blue = list(hex_split[2])
# Assigns hex_val dictionary value if a-f
for k in range(len(blue)):
    if blue[k].isdigit() == False:
        blue[k] = hex_val[blue[k]]
# Converts values to int
for k in range(len(blue)):
    blue[k] = int(blue[k])
# Base 10 algorithm
blue_b10 = blue[0]*16 + blue[1]

# Outputs results
print('\nColor Values (Base 10):')
print('  Red:', red_b10)
print('  Green:', green_b10)
print('  Blue:', blue_b10)