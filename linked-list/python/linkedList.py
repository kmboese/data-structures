class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data=None):
        if data:
            tmp = Node(data)
            self.head = tmp
        else:
            self.head = None

    def insert(self, data):
        tmp = Node(data)
        tmp.next = self.head
        self.head = tmp
    
    def traverse(self):
        if not self.head:
            return
        tmp = self.head
        while True:
            if not tmp:
                break
            print("{} ".format(tmp.data), end='')
            tmp = tmp.next


