class Node: 
    def __init__(self,key):
        self.left = None
        self.right = None

    # creation of a simple tree 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# general tree 
class Employee:
    def __init__(self, name, title) -> None:
        self.name = name
        self.title = title
        # use a list to rep the children 
        self.children = []

    def add_employee(self,employee):
        self.children.append(employee)

    def __str__(self, level=0) -> str:
        result = " "*level + f"{self.name} ({self.title})"
        for child in self.children:
            result += "\n" + child.__str__(level + 1)
        return result


# CEO = Employee("Joseph","CEO")
# CFO = Employee("Alice","CFO")
# CTO = Employee("Bob", "CTO")

# manager1 = Employee("Manager 1", "Engineering manager")
# manager2 = Employee("Manager 2", "Finance manager")
# eng1 = Employee("Eng 1", "Software Engineers")
# eng2 = Employee("Eng 2", "Software Engineers")


# # add the employees 
# CEO.add_employee(CFO)
# CEO.add_employee(CTO)
# CTO.add_employee(manager1)
# CFO.add_employee(manager2)
# manager1.add_employee(eng1)
# manager1.add_employee(eng2)


# # Print the organizational chart 
# print(manager2)

 
# binary tree 
class EmployeeBinary:
    def __init__(self,name,title) -> None:
        self.name = name
        self.title = title
        self.left = None
        self.right = None

    def add_left_employee(self,employee):
        if self.left is None:
            self.left = employee
        else:
            print("Left child already exists")

    def add_right_employee(self,employee):
        if self.right is None:
            self.right = employee
        else:
            print("right child already exists")

    def __str__(self, level=0) -> str:
        result = " "*level + f"{self.name} ({self.title})"
        if self.left:
            result += "\n" + self.left.__str__(level + 1)
        if self.right:
            result += "\n" + self.right.__str__(level + 1)
        return result
    

CEO = EmployeeBinary("Joseph","CEO")
CFO = EmployeeBinary("Alice","CFO")
CTO = EmployeeBinary("Bob", "CTO")

manager1 = EmployeeBinary("Manager 1", "Engineering manager")
manager2 = EmployeeBinary("Manager 2", "Finance manager")
eng1 = EmployeeBinary("Eng 1", "Software Engineers")
eng2 = EmployeeBinary("Eng 2", "Software Engineers")

CEO.add_right_employee(CFO)
CEO.add_left_employee(CTO)
CTO.add_left_employee(manager1)
CFO.add_right_employee(manager2)
manager2.add_left_employee(eng1)
manager2.add_right_employee(eng2)


print(manager2)