#  FUNCTIONS : self-contained block of code that performs a specific task or set of tasks. 
#  Usage : helps modularize the code , make code organized , reusable and easier to maintain 


# def function_name():
#     return result

# def function_name(parameters):
#   logic 

#     return result

#  Function Parameters and Arguments 

def greet(name): 
    return f"Hello, {name}!"

message = greet("Joseph")
print(message)

#  Default parameter values 
def exponent(base, power=2):
    return base ** power 

print(exponent(3,4))
print(exponent(3))


# Return values : 
def add_sub(a,b):
    addition = a + b 
    subtraction = a - b 
    return addition ,subtraction 
#  returns multiple values as a tuple (11,5)

add , sub = add_sub(8,3)
print(add)
print(sub)


