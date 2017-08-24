def remove_duplicates(numbers):
    ''' Removes duplicate elements within a given list of numbers '''
    
    duplicates = []
    result_list = []
    
    for num in numbers:
        if num not in duplicates:
            duplicates.append(num)
            result_list.append(num)
        
    return result_list


# Example
print(remove_duplicates([1, 1, 2, 3, 3, 2, 2, 2, 4, 5, 4]))
        