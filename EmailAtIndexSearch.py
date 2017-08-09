def findAt(email_addr):
    """ Returns the index of the @ character in an email address
        
        Returns -1  if user name empty
                    if multiple @ signs
                    if domain name empty
                    if no @ sign
    """
    
    # Splits string into list of elements separated by @ symbol
    split = email_addr.split('@')

    # Splits string into list of each character as an element
    lst = list(email_addr)
    
    # Inits return variable (index of @)
    at_index = ''
    
    # If elif loop checks for errors
    # If no errors then @'s index is returned
    if len(split) > 2:
        return -1
    elif len(split) == 2 and split[0] == '':
        return -1
    elif len(split) == 2 and split[1] == '':
        return -1
    elif '@' not in lst:
        return -1
    else:
        at_index = lst.index('@')

    return at_index


### Example ###
print('Sample execution of function findAt()\n  Returns index of @ symbol in an email address\n')
print("findAt('email@naver.com') =", findAt('email@naver.com'))

