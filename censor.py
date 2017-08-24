def censor(text, word):
    ''' Censors a given word with * in a given string text '''
    
    text_list = text.split(" ")
    
    result_list = []

    for w in range(len(text_list)):
        if text_list[w] == word:
            result_list.append("*" * len(word))
        else:
            result_list.append(text_list[w])
    
    result = " ".join(result_list)
    
    return result


# Example
print(censor("This cake is the sweetest cake I've ever tasted", "cake"))