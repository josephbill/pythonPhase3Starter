# nested functions 
# take another function as an arguement 
# It will have its own processes and then will make the call to the passed function

def my_decorator(func):
    # nested function: initial work of the decorator 
    def wrapper():
        print("Something is called before the function passed is invoked.")
        func()
        print("Something is called after the function passed is invoked.")
    return wrapper


# usage 
# notation : @nameofyourdecorator before defination of the function passed as an argument 
@my_decorator
def printName():
    print("Joseph")


printName()


#  INPUT validation using a decorator 
# Calculation logic , basing the input validation on the entries being positive integers 

# What the inbuilt method to check for the data type of a value ?  type(element)
# def name (x,y): 
# #   type(x, int)  int. more consice
# # isinstance(element,int)

def validatePositiveInteger(func):
    # * : list collection
    # **: dictonary : key values 
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg,int) or arg <= 0:
                raise ValueError("Arguments must be positive integers")
        return func(*args, **kwargs)
    return wrapper


@validatePositiveInteger
def multiply(a,b):
    print(b)
    return a * b


# result = multiply(10,5)
result = multiply(b=10 , a=5)
print("Result:",result)
# result = multiply(-5,10)
# print("Result:",result)


# **kwargs 
# Keyword arguments : named arguments : allows us to pass arguments to a function or a method by specifying the 
# argument name plus the value 
# allows arguments to be defined as explicit and readable 
# functionname(argvalue=value)

# advantages of using keyword arguements 
# 1. Clarity  : code more readable 
# 2. Flexibility : 
# 3. Order independence : arguments can be provided in any order esp. when a function has multiple parameters 