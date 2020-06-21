
#General form of STACK

class Stack:
    def __init__(self):
        self.items = []

    #Adding an item to the stack
    def push(self,item):
        self.items.append(item)

    #Remving the item from the top of the stack
    def pop(self):
        return self.items.pop()

    #Printing the top of the item in the stack
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    #Check whether the stack is empty
    def is_empty(self):
        return self.items == []

    #TO get the Stack items
    def get_stack(self):
        return self.items

s = Stack()
s.push('B')
s.push('O')
s.push('O')
s.pop()
print(s.peek())
s.is_empty()
print(s.get_stack())