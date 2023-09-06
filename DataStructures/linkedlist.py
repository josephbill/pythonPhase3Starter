class Node: 
    def __init__(self, data):
        self.data = data
        # pointer 
        self.next = None 

class LinkedList: 
    def __init__(self) -> None:
        self.head = None

    def append(self,data):
        new_node = Node(data)
        # the node is added to the linked list 
        # creates the pointer to the next node value 
        if not self.head:
            self.head =  new_node
            return 
        # track the current pointer 
        current = self.head
        # giving the pointer after the HEAD 
        while current.next: 
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next 
        print("None")


class TaskList: 
    def __init__(self) -> None:
        self.tasks = LinkedList()

    def add_task(self,task):
        self.tasks.append(task)

    def remove_task(self,task):
        current = self.tasks.head
        previous = None

        while current:
            if current.data == task:
                if previous:
                    previous.next = current.next 
                else:
                    self.task.head = current.next 
                return 
            previous = current
            current = current.next
    
    def display_tasks(self):
        self.tasks.display()

if __name__ == "__main__":
      listing = LinkedList()
      listing.append(1)
      listing.append(2)
      listing.append(3)
      listing.append(4)

      listing.display()

# TaskList 
      tasks = TaskList()
      tasks.add_task("Buy Milk")
      tasks.add_task("Buy Sugar")
      tasks.display_tasks()

      tasks.remove_task("Buy Sugar")
      tasks.display_tasks()