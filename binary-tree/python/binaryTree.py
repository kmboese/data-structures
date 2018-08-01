DEBUG = True

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data

class BinaryTree:

    def __init__(self):
        self.root = None
        self.elementCount = 1
        self.height = 0

    def insert(self, n, current = None):
        if current == None:
            current = self.root
        if (n.data <= current.data):
            if (current.left == None):
                dPrint("inserting left")
                current.left = n
                n.parent = current
                self.elementCount += 1
                self.height += 1
            else:
                self.insert(n, current.left)
        elif (n.data > current.data):
            if (current.right == None):
                dPrint("inserting right")
                current.right = n
                n.parent = current
                self.elementCount += 1
                self.height += 1
            else:
                self.insert(n, current.right)

    # Traversal functions
    def printDFS(self, n=None, level=0):
        if not n:
            print("The tree has {} elements and is height {}".\
                format(self.elementCount, self.height))   
            n = self.root
            print("Root: {}".format(n.data))
        else:
            print("Node: {}\tlevel {}".format(n.data, level))
        if n.left:
            self.printDFS(n.left, level)
        if n.right:
            self.printDFS(n.right, level)


# Helper functions
def dPrint(message):
    if DEBUG: print("\tDebug: {}".format(message))
