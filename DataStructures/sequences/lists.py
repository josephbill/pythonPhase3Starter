#  ordered collection of items and can contain items of different data types 
#  are mutable  : changeable / can be reassigned 
fruits = ["apple","banana","cherry"]

# indexing and slicing : index positions -> 0 
firstFruit = fruits[0]
slicedList = fruits[1:3] 
# output ["banana" ,"Cherry"]
print(firstFruit, slicedList)

# CRUDING 
# modifying 
fruits[0] = "Orange"
# adding 
fruits.append("grape")

# removing 
fruits.remove("banana")


print(fruits)

# #  checking if item exists 
# x = input("Check for this fruit")
# # keyword in 
# if x in fruits:
#     print("yes")
# else:
#     print("no")


# joining two lists : extend 
fruits2 = ["kiwi","mango"]
fruits.extend(fruits2)

# adding a different data type 
tupleExample = ('tomato','lemons')
fruits.extend(tupleExample)

# print(fruits)

#  pop is used to select an item based on index or last item if no index is provided 
# print(fruits.pop(2))

# insert 
print(fruits.insert(0, "Apple"))
print(fruits)
# clear items 
# print(fruits.clear())



# https://www.w3schools.com/python/python_lists_sort.asp : Sorting a list
# https://www.w3schools.com/python/python_lists_copy.asp  : copying a list
# https://www.w3schools.com/python/python_lists_join.asp  : joining a list
# https://www.w3schools.com/python/python_lists_methods.asp : glossary of list methods

