# concise and readable way to create lists in python 
# creates a new list by applying an expression to each list item in an existing iterable 

# basic syntax 
# new_list = [expression for item in iterable if condition]

# expression = operation to be performed on each item 
# item = variable representing each element in the iterable 
# iterable = existing sequence being looped 
# condition = (optional) incase you need to filter the list 

# create a list of even number from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# create a list of squares of numbers from 0 to 9 
squares = [x ** 2 for x in range(10)]
print(squares)

