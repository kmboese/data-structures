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
        if current is None:
            current = self.root

        # Insert left
        if (n.data <= current.data):
            if (current.left is None):
                dPrint("inserting {} left".format(n.data))
                current.left = n
                n.parent = current
                self.elementCount += 1
                self.height += 1
            else:
                self.insert(n, current.left)
        # Insert right
        else:
            if (current.right is None):
                dPrint("inserting {} right".format(n.data))
                current.right = n
                n.parent = current
                self.elementCount += 1
                self.height += 1
            else:
                self.insert(n, current.right)

    # Traversal functions
    def printDFS(self, n=None, level=0):
        if not self.root:
            print("Error in printDFS(): cannot print empty tree")
        if not n:
            print("The tree has {} elements and is height {}".\
                format(self.elementCount, self.height))   
            n = self.root
            print("Root: {:4}".format(n.data))
        else:
            print("Node: {:4}\tLevel: {}".format(n.data, level))
        if n.left:
            level += 1
            self.printDFS(n.left, level)
        if n.right:
            level -= 1
            self.printDFS(n.right, level)

    def printBFS(self, n=None, level=0):
        if not self.root:
            print("Error in printBFS(): cannot print empty tree")


# Helper functions
def dPrint(message):
    if DEBUG: print("\tDebug: {}".format(message))