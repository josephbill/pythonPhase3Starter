# calculating factorials 

def factorial(n):
    # base case 
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

result = factorial(5)
print(result)

# recursions repeat tasks similar to loops 
# main difference recursion uses function calls instead of standard loops.