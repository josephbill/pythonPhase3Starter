# ordered but immutable 
# defined using round brackets
# indexed 

shoppingBasket = ("bread","juice","flour",1,True)
print(len(shoppingBasket))

# to define a tuple with one item 
tupleOne = ("bread",)

# Accessing a Tuple
# access is done by reference to the index number
print(shoppingBasket[0])
print(shoppingBasket[-1]) # negative indexing #start from end
print(shoppingBasket[2:5]) # range
print(shoppingBasket[2:]) # to search out the first index in range.
print(shoppingBasket[:3]) # to search out the last index in range.
print(shoppingBasket[-4:-1]) # this will search from end of the tuple

# in keyword used to check if item exists in a tuple 


# Joining (+= assignment operator)
shoppingBasket += tupleOne
print(shoppingBasket)

# adding , updating and removing 
# type casting : 
# convert the tuple to a list(mutable)
tempList = list(shoppingBasket)
tempList.append("Apple")
tempList[0] = "Cherry"
tempList.remove(1)
del tempList[2]
# list back to tuple 
shoppingBasket = tuple(tempList)
print(shoppingBasket)

# duplicated , copies.
duplicate = shoppingBasket * 2


