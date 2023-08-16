# unordered, unchangeable , unindexed
# defined using a curly brace 
# sets cannot be duploicated 
# True and 1 are considered to be the same

shoppingSet = {
    "bread","sugar","salt"
}

# in built methods 
# len(nameofset) : calculates length of items in the set 
# in keyword in sets is also used for access 
for x in shoppingSet:
   print(x)
# in can also be used to check if an item exists ina set
print("bread" in shoppingSet)
# to add a new item to set 
shoppingSet.add("Flour")
# add items from another set to a current set 
newSet = {
       "bread","sugar","salt","Strawberries"
}
# update to add other iterables , [lists,tuples]
print(shoppingSet.update(newSet)) 
print(shoppingSet)

# other common methids 
# .remove : used to remove items when item is known 
# .discard 
# .pop() : remove a random element from the set 
# .clear() : clears a set 
# del keyword : set is deleted completely

# .union() : 
# intersection_update , intersection, symmetric_difference_update, symmetric_difference