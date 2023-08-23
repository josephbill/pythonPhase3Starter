# A stack is a data structure in python. 
# Its a linear data structure that follows the L.I.F.O principle 
# LAST IN FIRST OUT 
# Linear : data is accessed in a sequences 
# Tech terminology for a stack : a linear ds that stores a collection of elements , allowing 
# two main operations 
# push / append (add an element to the top) # pop (remove the top element) 

# Practical use case 
# Advanced : function call stack 
# Browser Back Button

# Custom DSA. 
class SimpleBrowser: 
    def __init__(self) -> None:
        self.history = []

    # user accesses a page 
    def visit(self, url):
       print(f"Visting {url}")
    #    add items to my stack 
       self.history.append(url)


    # user presses the back button 
    # pop()
    def back(self):
        if self.history:
            previous_url = self.history.pop()
            print(f"Going to back to {previous_url}")
        else:
            print("No more pages to go back to")


chromeBrowser = SimpleBrowser()

# simulate visiting some pages 
chromeBrowser.visit("https://www.example.com")
chromeBrowser.visit("https://www.openai.com")
chromeBrowser.visit("https://www.python.com")
chromeBrowser.visit("https://www.moringaschool.com")


# simulate using the back button 
chromeBrowser.back()
chromeBrowser.back()
chromeBrowser.back()
chromeBrowser.back()
chromeBrowser.back()

