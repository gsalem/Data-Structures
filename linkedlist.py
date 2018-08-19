""" Linked List Implementation """

class node(object):
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = node()

    # append to list
    def append(self, data):
        new_node = node(data)  
        current = self.head # head of the list
        while current.next != None: # while not last node
            current = current.next  # traverse
        current.next = new_node # append


    # display list
    def display(self):
        list = []
        current = self.head
        while current.next != None:
            current = current.next
            list.append(current.data)
        return print(list)
    
    # get length of linked list
    def len(self): 
        length = 0
        current = self.head
        while current.next != None:
            current = current.next
            length += 1
        return length

    # get node at given index
    def get(self, index):
        # error check
        if index > self.len() or index < 0:
            return print ("ERROR: Index out of range")
        current = self.head
        current_index = 0
        while True:
            current = current.next
            if current_index == index:
                return print(current.data)
            current_index += 1
    
    # delete node at given index
    def delete(self, index):
        if index > self.len() or index < 0:
            return print ("ERROR: Index out of range")
        current = self.head
        current_index = 0
        while True:
            prev_node = current
            current = current.next
            if current_index == index:
                prev_node.next = current.next
                return
            current_index += 1

    # insert node at given index
    def insert(self, data, index):
        if index > self.len() or index < 0:
            return print ("ERROR: Index out of range")
        current = self.head
        current_index = 0
        while True:
            prev_node = current
            current = current.next
            if current_index == index:
                new_node = node(data)
                prev_node.next = new_node
                new_node.next = current
                return
            current_index += 1


#####  Test cases  #####

list = LinkedList()

# display list
list.display()

# append some values
list.append(0)
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.display()

# get length of linked list
print ("The length of this linked list is", list.len())

# get data of given index
list.get(4)

# delete node of given index
list.delete(3)
list.display()
list.delete(999)
list.delete(-999)

# insert node of given index
list.insert("insert", 3)
list.display()
list.insert(3, 999)
list.insert(3, -999)