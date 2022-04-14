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

    # Returns an empty linked list
    def empty():
        emp = LinkedList(None)
        return emp
    
    # Returns True of node is empty. Runs in CONSTANT time.
    def isEmpty(self):
        if self.head == None: return True
        return False

    # Returns True if node is not empty. Runs in CONSTANT time.
    def nonEmpty(self):
        return not self.isEmpty()

    # Returns printable version of the list. Runs in LINEAR time.
    def __str__(self) -> str:
        s = "("
        p = self
        while p.nonEmpty():
            s += str(p.head) + ", "
            p = p.tail
        s = s[:-2]
        s += ")"
        return s

    # Returns the length of the list. Runs in LINEAR time.
    def length(self):
        if self.isEmpty():
            return 0
        else: return 1 + self.tail.length()

    # Returns the max of the list. Runs in LINEAR time.
    def max(self):
        def max_of_two(x, y):
            try:
                if x > y: return x
                else: return y
            except:
                if x == None: return y
                else: return x
        if self.isEmpty():
            return None
        else:
            return max_of_two(self.head, self.tail.max())
    
    # Adds a node to the front of the list. Runs in CONSTANT time.
    def insert_first(self, val):
        node = LinkedList(self.head)
        node.tail = self.tail
        self.head = val
        self.tail = node

    # Inserts before the 'i' index. Runs in LINEAR time.
    def insert_at_index(self, val, i):
        node = LinkedList(val)
        p = self
        currentIndex = 0
        while currentIndex < i - 1:
            p = p.tail
            currentIndex += 1
        node.tail = p.tail
        p.tail = node

    # Gets the value at index 'i'. Runs in LINEAR time.
    def val_at_index(self, i):
        acc = 0
        p = self
        while acc != i:
            if p.tail.isEmpty():
                print("Error: Out of index")
                return None
            else:
                p = p.tail
                acc += 1
        return p.head    

# Performs merge sort on the linked list. Is a destructive function. Runs in n*log(n) time.
def mergeSort(lst):
    def merge(list1, list2):
        if list1.isEmpty(): return list2
        elif list2.isEmpty(): return list1
        else:
            if list1.head < list2.head:
                merged = merge(list1.tail, list2)
                merged.insert_first(list1.head)
                return merged
            else:
                merged = merge(list1, list2.tail)
                merged.insert_first(list2.head)
                return merged
    
    length = lst.length()
    if length <= 1: return lst
    elif length == 2:
        if lst.head > lst.tail.head:
            temp = LinkedList.empty()
            temp.insert_first(lst.head)
            temp.insert_first(lst.tail.head)
            return temp
        else:
            temp = LinkedList.empty()
            temp.insert_first(lst.tail.head)
            temp.insert_first(lst.head)
            return temp
    else:
        leftHalf = LinkedList.empty()
        rightHalf = LinkedList.empty()
        c = 0
        p = lst
        leftLen = length//2
        rightLen = leftLen
        if length%2 != 0:
            leftLen += 1
        while p.nonEmpty():
            if c < leftLen:
                leftHalf.insert_first(p.head)
            else:
                rightHalf.insert_first(p.head)
            c += 1
            p = p.tail
        return merge(mergeSort(leftHalf), mergeSort(rightHalf)) 
                
# Reverses the linked list. Runs in LINEAR time.
def reverseList(lst):
    p = lst
    newList = LinkedList.empty()
    
    while p.nonEmpty():
        n = p.tail
        p.tail = newList
        newList = p
        p = n
    return newList
    



