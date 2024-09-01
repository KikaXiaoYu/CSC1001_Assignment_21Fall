


def factorial(n):
    res = 1 # used for output
    stack = list() # create the stack
    stack.append((n)) # push the biggest function
    while (len(stack) > 0): # still has function to finish
        num = stack.pop() # get the most outside one
        res *= num # update the output
        if (num == 1): # the basic situation
            break
        else:
            stack.append((num-1)) # push the smaller function
    return res

if __name__ == '__main__':
    print(factorial(5))
