# Kevin Fernandez
# Super List - A doubly linked list that keeps track of the last node (for constant appending) and length (for constant access).
# Can be implemented as a queue or stack with constant time.

# Node that the SuperList object will have.
class SListNode:
    # Constructor
    def __init__(self, val, pre = None, t = None):
        self.value = val
        self.next = t
        self.prev = pre

# Super List class
class SuperList:
    # Constructor
    def __init__(self):
        self.head = None
        self.last = None
        self.length = 0
    
    # Insert first. Constant time.
    def insert_first(self, v):
        node = SListNode(v)
        if self.head is None:
            self.head = node
            self.last = node
            self.length = 1
        else:
            node.next = self.head
            self.head = node
            self.length += 1
    
    # Appends node. Constant time.
    def append(self, v):
        if self.head is None:
            self.insert_first(v)
        else:
            node = SListNode(v)
            node.prev = self.last
            self.last.next = node
            self.last = node
            self.length += 1
    
    # Removes node at given position and returns value. Run's in constant time if
    # node is first or last, runs in linear time otherwise.
    # -1 for last node
    def pop(self, i = -1):
        if self.length == 0:
            print("Super List is empty.")
        else:
            self.length -= 1
            if i == -1: # last node
                v = self.last.value
                prevNode = self.last.prev
                self.last.prev = None
                self.last = prevNode
                # if the list is now empty, the head should point to None
                if self.last == None:
                    self.head = None
                return v
            elif i == 0: # first
                v = self.head.value
                nextNode = self.head.next
                self.head.next = None
                self.head = nextNode
                #if the list is empty, last should point to None
                if self.head == None:
                    self.last = None
                return v
            else:
                p = self.head
                currI = 0
                while currI != i and p is not None:
                    currI += 1
                    p = p.next
                    if p is None and currI != i: # reached end, out of index
                        print("Out of index")
                        return None
                p.prev.next = p.next
                return p.value

    # Returns printable string of the Super List.
    def __str__(self):
        s = ""
        p = self.head
        while p is not None:
            s += str(p.value) + ", "
            p = p.next
        return "(" + s[:-2] + ")"
