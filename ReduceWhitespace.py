def reduceWhitespace(line):
    """ Removes extra whitespace between words and returns the result """

    # Splits the line into a list divided by spaces
    line = line.split(' ')
    
    # Removes all empty quotes in list
    while '' in line:
        line.remove('')
    
    # Creates new string to hold the new line
    newline = line[0]
    
    # Adds all elements of the list line with only 1 space inbetween
    for k in range(1, len(line)):
        newline = newline + ' ' + line[k]
        
    return newline

### example ###

print('Sample execution of function reduceWhitespace()\n')
print("reduceWhitespace('Hello      there my   name           is Liz ')")
print(reduceWhitespace('Hello      there my   name           is Liz '))

