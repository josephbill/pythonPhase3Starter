# Algorithm : step by step process to solve a problem 
# Why enhance ? writing code to cater for an upper bound 
#  upper bound  ? absolute number of steps that an algorithm takes inorder to execute 
#  BIG O notation : measurement of the time taken to process the execution of an algo and the space taken up in memory 
#  Time and Space complexity 


#  Common BIG O notation groups 
# 1. O(1) : constant complexity : time taken by algo to complete does not depend on the input size : in built methods for data types.
# 2. O(N) : linear complexity : The larger a data set is, 
# the longer an algorithm in O(N) time will take - but the increase in time will be constant. : loops
# 3. O(log n) : logarithmic time complexity : time taken by algo to complete grows logarithmically with the 
# size of the input data  : divide and conquer algos. : merge sort : binary search
# 4. O(n²): quadratic time complexity : time taken by algo to complete grows exponetially : nested loops : bubble sort.


#  checks if a number is even O(1) : id is based on the comparison logic 
#  % modulo : result of the remainder of division
def isEven(number):
    return number % 2 == 0

#  access the dictionary values 
student_info = {
    "name" : "Alice",
    "Age" : 20
}

def getstudentAge(info):
    return info["age"]


print(getstudentAge(student_info))


# O(N) : linear 
myarray  = [5,3,8,2,9]

def findMaxElement(arr):
    # intialization of my max element value 
    maxelement = arr[0] 
    # logic is to loop the array comparing the values 
    for num in arr[1:]:
        if num > maxelement:
            maxelement = num

    return maxelement


print(findMaxElement(myarray))


#  above is considered O(N) : it performs a constant-time operation for each element in the array 
#  results in a linear relationship between the input size and the number of operations.

