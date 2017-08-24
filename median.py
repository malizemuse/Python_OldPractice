def median(numbers):
    ''' Returns median from a given list (numbers)'''
    
    numbers_sorted = sorted(numbers)
    
    # Even length
    if len(numbers) % 2 == 0:
        even_index_1 = len(numbers_sorted) / 2
        even_index_2 = (len(numbers_sorted) / 2) - 1
        
        even_1 = float(numbers_sorted[even_index_1])
        even_2 = float(numbers_sorted[even_index_2])
        
        median = (even_1 + even_2) / 2
        
    # Odd length
    else:
        odd_index = (len(numbers_sorted) - 1) / 2
        median = numbers_sorted[odd_index]
    
    return median


# Example
print(median([1, 2, 3, 4]))
