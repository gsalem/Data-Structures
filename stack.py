""" 
Stack implementation using Single Linked List

"""

class Element(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element

        else:
            self.head = new_element


    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
      if self.head:
        temp = self.head
        temp = temp.next
        del_node = self.head
        del_node.next = self.head
        self.head = temp
      else:
        return None
    
    def empty_stack(self):
      temp = self.head
      while temp.next != None:
        temp = temp.next
        del_node = self.head
        del_node.next = self.head
        self.head = temp
        temp.next = None

    def display(self):
      list = []
      curr = self.head
      if self.head:
        while curr.next != None:
          list.append(curr.value)
          curr = curr.next
      print (list)

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        self.ll.delete_first()
    
    def display(self):
      self.ll.display()

    def empty_stack(self):
      self.ll.empty_stack()
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)
e6 = Element(6)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.display()

stack.push(e3)
stack.display()

stack.push(e4)
stack.display()

stack.push(e5)
stack.display()

stack.push(e6)
stack.display()

stack.pop()
stack.display()

stack.pop()
stack.display()

stack.pop()
stack.display()

stack.push(e4)
stack.display()

stack.push(e5)
stack.display()

stack.push(e6)
stack.display()

# Empty the stack
stack.empty_stack()
stack.display()

# Test pop function when stack is empty
stack.pop()
stack.display()