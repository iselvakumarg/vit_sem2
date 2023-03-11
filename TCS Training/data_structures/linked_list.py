# Create a singly linked list in python which takes input from the user and add it at the end of the list.

class Node:
    def __init__(self, value=None, next=None):
        self.value = value 
        self.next = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head 
        while node:
            yield node 
            node = node.next 

    def insertEnd(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            tempNode = self.head
            while tempNode.next != None:
                tempNode = tempNode.next
            tempNode.next = newNode

    def printList(self): 
        temp = self.head 
        while (temp): 
            print (temp.value, " -> ", end = '') 
            temp = temp.next
        print("")

singly = SinglyLinkedList()

use = True
while use:
    i = int(input("Enter the value for LL: "))
    if i < 0:
        use = False
        break
    else:
        singly.insertEnd(i)

# singly.insertEnd(1)
# singly.insertEnd(2)
# singly.insertEnd(3)
# print("Node inserted")

singly.printList()