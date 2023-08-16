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


# Return multiple values as tuples  : 
def add_sub(a,b):
    addition = a + b 
    subtraction = a - b 
    return addition ,subtraction 
#  returns multiple values as a tuple (11,5)

add , sub = add_sub(8,3)
print(add)
print(sub)


#  Scope and local variables 

global_variable  = 10 

def my_function():
    local_variable = 20 
    print(global_variable, local_variable)

my_function()


# Anonymous functions (Lambda Functions)
#  small , unnamed functions defined using the lambda keyword 

multiply = lambda x , y : x * y 
print(multiply(4,5))

# Recursion 
# Functions can call themselves , 
#  useful for solving problems that can be broken down into smaller instances of the same problem 

#  n references the number which will be used to calculate the factorial 
#  recursion requires a base case  ()
def factorial(n):
    if n == 0:
      return 1
    else: 
      return n * factorial(n-1)  
    
print("FACTORIAL RESULT")
print(factorial(5)) 
# 120 
#  5 * (4 * (3 * (2 * 1)))


#  FUNCTION OVERLOADING ; not supported in python but hacked by using default arguement and the concept of 
#  variable length argument list 