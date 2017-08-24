def count(sequence, item):
    ''' Counts occurrences of an element (item) in a given list (sequence)'''
    
    count = 0
  
    for i in range(len(sequence)):
        if sequence[i] == item:
            count += 1
  
    return count


# Example
print(count(["hi", "hello", "hi", "hey", "hi"], "hi"))