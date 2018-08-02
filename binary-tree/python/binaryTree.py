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
        self.elementCount = 0
        self.height = 0

    def insert(self, n, current = None):
        # Special case: insert into an empty tree
        if self.elementCount == 0:
            self.root = n
            self.elementCount += 1
            return
        # By default, start inserts at the root node
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
