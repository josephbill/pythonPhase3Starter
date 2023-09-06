Data Structures ? a way of storing and organizing data 
- we have methods provided for accessing and modifying the data structures 

## KEY VOC. 
1. Sequence : a way in which data is stored and accessed in a specific order 
2. Stack :  a linear data structure that follows the L.I.F.O principle 
3. Queue : a linear data structure that follows the F.I.F.O principle 
4. Index : location of an element in a sequence 
5. Iterable : able to be broken down into smaller parts of equal sizes and processed in turns i.e. loop , trasverse 
6. Slice : a group of neighbouring elements in a sequence 
7. List : a mutable (can be changed/reassigned) that can store many data types 
8. Tuple : Immutable data type that can store many data types 
9. Dictionaries : a linear data structure , Mutable data type used to store data in value and keys pairs
10. Sets : a data structure that is unordered , imutable , unindexed and do not allow duplicated values 
11. Range : a data type that stores integers in a fixed pattern 
12. String : a sequence of indexed characters.
13. Trees : non linear data structure that is hierarchial and composed of nodes which have values and can have zero or more child nodes 
14. Graphs : non linear data structure that is a collection of nodes connected by edges 
15. Linked Lists : a linear data structure in which elements are stored as individual nodes each containing a value and a reference 

## Use case 
- The Javascript DOM : tree
- Call Stack : (understand how functions work.) 
  - what is a stack overflow ?  Tech term : 
  - execution context 
  - return 
  - parameters and arguments 



## Data Structures 
1. Linked Lists 
2. Trees (General Tree and Binary Tree)
3. Merge Sort 


## Merge Sort 
- This is a popular sorting (specific arrangement to your data set , asc, desc) algorithm 
- This is part of divide and conquer strategy to sort an array or list of elements 

list 
divide the list into two halves 
RECURSIVELY sort them : function that has our sort logic 
merge the sorted halves to produce a stored output.  

- The sorting behaviour is stable and a time complexity of O(n log n) , makes it efficient for large dataset

## Recursion 

defination : process of defining a problem or the solution to a problem in terms of a simpler version of itself.

in programming : a function calling itself until a "base condition" is true to produce the correct output. 


## uses
1. Sorting large datasets 
2. External Sorting 
3. Database sorting : efficient algos.
4. Data duplication


## Linked Lists 
A linked list is a data structure consisting of a sequence of elements , where each element points to the next element in the sequence 
Useful when you need dynamic size , efficient insertions and deletions : memory

## Trees 
A tree is a hierarchial data structure in which element known as nodes are linked together via edges such that 
there is only one path between any two nodes of the tree.  

Two main categorizations 
. General trees 
. Binary trees 

Differences : 
1. Structure 
tree : a tree has no restriction in the number of children that a node can have 
binary tree :every node in a binary tree can have at most two children. (left and right child)

2. Properties
tree : a tree has no restriction in the number of children that a node can have 
binary tree : each node can have either zero children (a leaf node) : one child (either left or right ) or two children 
(both left and right)

3. Usage
binary tree : commonly used for tasks like sorting and searching because of its balanced structure.
tree : commonly used to design file systems. (hierarchical data structure apps) (Charts)
