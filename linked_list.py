# Kevin Fernandez
# Updated 5/8/2022
# Implementing linked lists

# imports
import random
import math

# Class Delcaration
class LinkedList: # This linked list data structure holds integers
    # Constructor of a Linked List node
    def __init__(self, v):
        self.head = v
        self.tail = None

    # Returns printable version of the list. Runs in LINEAR time.
    def __str__(self) -> str:
        s = "("
        p = self
        while p is not None:
            s += str(p.head) + ", "
            p = p.tail
        s = s[:-2]
        s += ")"
        return s

    # Returns the length of the list. Runs in LINEAR time.
    def length(self):
        return 1 if self.tail is None else 1 + self.tail.length()
    
    # Adds a node to the front of the list. Runs in CONSTANT time.
    def insert_first(self, val):
        node = LinkedList(self.head)
        node.tail = self.tail
        self.head = val
        self.tail = node

    # Inserts before the 'i' index. Runs in LINEAR time.
    def insert_at_index(self, val, i):
        if i == 0:
            self.insert_first(val)
        else:
            node = LinkedList(val)
            p = self
            currentIndex = 0
            while currentIndex < i - 1:
                p = p.tail
                currentIndex += 1
            node.tail = p.tail
            p.tail = node

    # Inserts at the very end of the cain. LINEAR time.
    def append(self, val):
        p = self
        while p.tail != None:
            p = p.tail
        node = LinkedList(val)
        p.tail = node

    # Gets the value at index 'i'. Runs in LINEAR time.
    def val_at_index(self, i):
        acc = 0
        p = self
        while acc != i:
            if p.tail is None:
                print("Error: Out of index")
                return None
            else:
                p = p.tail
                acc += 1
        return p.head
