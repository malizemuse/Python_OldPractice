""" Simple Fibonacci number-related functions """
# A practice in recursive function calls

def fib(n):
    '''Computes the n-th Fibonacci number.'''
    
    # base case
    if n == 0:
        return 0
    # base case
    elif n ==1:
        return 1
    # recursive case
    else:
        return fib(n - 1) + fib(n - 2)

def fibcalls(n):
    '''Computes the number of function calls to fib() required
        to compute the n-th Fibonacci number.'''
    
    # base case
    if n == 0:
        return 0
    # base case
    elif n == 1:
        return 1
    # base case
    elif n == 2:
        return 1
    # recursive case
    else:
        return fibcalls(n - 1) + fibcalls(n - 2) + 1
