class MyClass:
    # instance attributes : __init__ and they belong to the object 
    # class attributes : belong to the class , __init__ (class constructor) or defined as part of the class code. 
    class_attribute  = "I am a class attribute"
    def __init__(self):
        self.class_attribute = "I am a class attribute"

# its called by calling the class directly 
# dot notation.
print(MyClass.class_attribute)


class Animal:
    species = "I am animal"

    def __init__(self,name) -> None:
        self.name = name

    def printName(self):
        # logic using self to access the object attribute 
        pass

cat1  = Animal("rex")
# accessing the attributes 
cat1.name
# modifying the class attributes 
cat1.species = "a"


# Class methods 
# invoking the class methods : dot notation
# when defining class methods we need to use the @classmethod decorator - indicate the method belongs to the class 

class Book:
    # keeping track of the total pages across all books 
    total_pages = 0

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    @classmethod
    def update_total_pages(cls, pages):
        cls.total_pages += pages

    def add_to_total_pages(self):
        Book.update_total_pages(self.pages)


# prints 
book1 = Book("Sample Book","Joseph",100)

# print the intial total_pages # 0
print("Initial total pages ", Book.total_pages)  

# add pages from book 1 using the instance method 
book1.add_to_total_pages()

# Print after update on total pages 
print("After update:  total pages ", Book.total_pages)  


#  Setting default values for objects 
class Restaurant:
    tip = 18
    def __init__(self, name, cuisine, bill, tip=None):
       self.name = name
       self.cuisine = cuisine
       self.bill = bill
       if tip is not None:
               self.tip = tip

# sharing info about objects 
class Book:
   count = 0
  
   def __init__(self, title, author, pages):
       self.title = title
       self.author = author
       self.pages = pages
       Book.count += 1

# Creating singletons 
# objects created only once and can be shared among multiple parts of your code 
# commonly used for shared resources such as db connections , caches systems ,
# any object that should be created once in a program

class Database:
#    this carries my singleton object 
   _instance = None 

# the __new__ method ensures that only one instance of the class is created i.e only one object  
   def __new__(cls):
       if cls._instance is None:
           cls._instance = super().__new__(cls)
       return cls._instance
   
db1 = Database()
db2 = Database()
# this will refer to the same object -> __new__ method