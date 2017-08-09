""" Evaluates RPN expression using a stack
    
    ie.     1234+-* = 5
        =>  ((4 + 3) - 2) + 1 =  5 
"""
# Practice with the specific data structure of stacks


# Stack functions defined
def getStack():
    """Creates and returns empty stack."""
    return[]
    
def isEmpty(s):
    """Returns True if stack empty, else False."""
    if s == []:
        return True
    else:
        return False

def top(s):
    """Returns value of top item of stack, if not empty."""
    if isEmpty(s):
        return None
    else:
        return s[len(s) - 1]
    
def push(s, item):
    """Pushes item onto top of stack."""
    s.append(item)
    
def pop(s):
    """Returns value of top of stack, if not empty."""
    if isEmpty(s):
        return None
    else:
        item = s[len(s) - 1]
        del s[len(s) - 1]
        return item


### Main ###
print('Evaluate an RPN expression\n  (ie.  1234+-*  =>  (4 + 3) - 2) + 1  =  5)\n')
stack_in = input('Enter an RPN expression: ')
rpn_list = list(stack_in)

# Inits stack and result variable
stack = getStack()
result = 0

operator = ['+','-','*','/','=']

# Evaluates RPN expression by selectively pushing / popping integers and performing operations with the stack data structure
for k in range(len(rpn_list)):
    if rpn_list[k] not in operator:
        push(stack, int(rpn_list[k]))
    elif rpn_list[k] == '+':
        result = top(stack) + stack[len(stack)-2]
        pop(stack)
        pop(stack)
        push(stack, result)
    elif rpn_list[k] == '-':   
        result = top(stack) - stack[len(stack)-2]
        pop(stack)
        pop(stack)
        push(stack, result)
    elif rpn_list[k] == '*':
        result = top(stack) * stack[len(stack)-2]
        pop(stack)
        pop(stack)
        push(stack, result)
    elif rpn_list[k] == '/':
        result = top(stack) / stack[len(stack)-2]
        pop(stack)
        pop(stack)
        push(stack, result)


print('\nValue of expression:', result)