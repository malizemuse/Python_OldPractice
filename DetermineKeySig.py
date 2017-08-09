""" Determines key signature of a music piece
    
    Asks    if major or minor,
            if key sig has sharps or flats
            for number of sharps of flats
    
    Returns key signature
"""

# Prelim info
flats = ['B','E','A','D','G','C','F']
sharps = ['F','C','G','D','A','E','B']

# Inits variables
sharpsOrFlats_num = 0
sharpsOrFlats_num = 0
validnum_sof = [1,2,3,4,5,6,7]

# Multi-dimensional list of key sigs for later result output
keySig = [['G major','D major','A major','E major','B major','F major','C# major'],
           ['F major','Bb major','Eb major','Ab major','Db major','Gb major','Cb major'],
           ['E minor','B minor','F# minor','C# minor','G# minor','D# minor','A# minor'],
           ['D minor','G minor','C minor','F minor','Bb minor','Eb minor','Ab minor']]

print('Key Signature Determiner\n\n')
print('Order of Flats:\n  ', flats, '\n')
print('Order of Sharps:\n  ', sharps, '\n')

# Asks for user input of info to determine key
majorOrMinor = ''
while majorOrMinor != "M" and majorOrMinor != "m":
    majorOrMinor = input("\nTone: Major (M) or minor (m)?\n  ")

anySharpsOrFlats = ''
while anySharpsOrFlats != "y" and anySharpsOrFlats != "n":
    anySharpsOrFlats = input("\nAre there any sharps or flats in the key signature? (y) or (n)\n  ")

# If/elif/else statements to determine key
if anySharpsOrFlats == "n":
    if majorOrMinor == "major":
        print("\n\n  Key: C major\n\n")
    elif majorOrMinor == "minor":
        print("\n\n  Key: A minor\n\n")
else:
    sharpsOrFlats = ''
    while sharpsOrFlats != '#' and sharpsOrFlats != 'b':
        sharpsOrFlats = input("\nSharps (#) or flats (b)?\n  ")
    sharpsOrFlats_num = 8
    while sharpsOrFlats_num not in validnum_sof:
        sharpsOrFlats_num = int(input("\nHow many?\n  "))

if majorOrMinor == 'M' and sharpsOrFlats == '#':
    if sharpsOrFlats_num == 1:
        print('\n\nKey:', keySig[0][0])
    elif sharpsOrFlats_num == 2:
        print('\n\nKey:', keySig[0][1])
    elif sharpsOrFlats_num == 3:
        print('\n\nKey:', keySig[0][2])
    elif sharpsOrFlats_num == 4:
        print('\n\nKey:', keySig[0][3])
    elif sharpsOrFlats_num == 5:
        print('\n\nKey:', keySig[0][4])
    elif sharpsOrFlats_num == 6:
        print('\n\nKey:', keySig[0][5])
    elif sharpsOrFlats_num == 7:
        print('\n\nKey:', keySig[0][6])

elif majorOrMinor == 'M' and sharpsOrFlats == 'b':
    if sharpsOrFlats_num == 1:
        print('\n\nKey:', keySig[1][0])
    elif sharpsOrFlats_num == 2:
        print('\n\nKey:', keySig[1][1])
    elif sharpsOrFlats_num == 3:
        print('\n\nKey:', keySig[1][2])
    elif sharpsOrFlats_num == 4:
        print('\n\nKey:', keySig[1][3])
    elif sharpsOrFlats_num == 5:
        print('\n\nKey:', keySig[1][4])
    elif sharpsOrFlats_num == 6:
        print('\n\nKey:', keySig[1][5])
    elif sharpsOrFlats_num == 7:
        print('\n\nKey:', keySig[1][6])

elif majorOrMinor == 'm' and sharpsOrFlats == '#':
    if sharpsOrFlats_num == 1:
        print('\n\nKey:', keySig[2][0])
    elif sharpsOrFlats_num == 2:
        print('\n\nKey:', keySig[2][1])
    elif sharpsOrFlats_num == 3:
        print('\n\nKey:', keySig[2][2])
    elif sharpsOrFlats_num == 4:
        print('\n\nKey:', keySig[2][3])
    elif sharpsOrFlats_num == 5:
        print('\n\nKey:', keySig[2][4])
    elif sharpsOrFlats_num == 6:
        print('\n\nKey:', keySig[2][5])
    elif sharpsOrFlats_num == 7:
        print('\n\nKey:', keySig[2][6])

elif majorOrMinor == "m" and sharpsOrFlats == 'b':
    if sharpsOrFlats_num == 1:
        print('\n\nKey:', keySig[3][0])
    elif sharpsOrFlats_num == 2:
        print('\n\nKey:', keySig[3][1])
    elif sharpsOrFlats_num == 3:
        print('\n\nKey:', keySig[3][2])
    elif sharpsOrFlats_num == 4:
        print('\n\nKey:', keySig[3][3])
    elif sharpsOrFlats_num == 5:
        print('\n\nKey:', keySig[3][4])
    elif sharpsOrFlats_num == 6:
        print('\n\nKey:', keySig[3][5])
    elif sharpsOrFlats_num == 7:
        print('\n\nKey:', keySig[3][6])

else: # Not possible to get here
    print("\n\nNot a valid key signature")
