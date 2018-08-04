DEBUG = True

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data

    def getChildren(self):
        children = []
        if self.left:
            children.append(self.left)
        if self.right:
            children.append(self.right)
        return children

class BinaryTree:

    def __init__(self):
        self.root = None
        self.elementCount = 0
        self.height = 0

    def insert(self, n, current = None, height=1):
        # Special case: insert into an empty tree
        if self.elementCount == 0:
            self.root = n
            #dPrint("root set to {}".format(n.data))
            self.elementCount += 1
            return

        # By default, start inserts at the root node
        if current == None:
            current = self.root

        # Insert left
        if (n.data <= current.data):
            if (current.left == None):
                dPrint("inserting {} left".format(n.data))
                current.left = n
                n.parent = current
                if (height > self.height):
                    self.height = height
                self.elementCount += 1
            else:
                height += 1
                self.insert(n, current.left, height)

        # Insert right
        else:
            if (current.right == None):
                dPrint("inserting {} right".format(n.data))
                current.right = n
                n.parent = current
                if (height > self.height):
                    self.height = height
                self.elementCount += 1
            else:
                height += 1
                self.insert(n, current.right, height)

    # Traversal functions
    def printDFS(self, n=None, level=0):
        if not self.root:
            print("Error in printDFS(): cannot print empty tree")
            # Base case: node is the root
        if not n:
            print("DFS: The tree has {} elements and is height {}".\
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

    def printBFS(self, n=None, children=[], height=0):
        if not self.root:
            print("Error in printBFS(): cannot print empty tree")
        # Base case: node is the root
        if not n:
            children = self.root.getChildren()
            print("BFS: The tree has {} elements and is height {}".\
                format(self.elementCount, self.height))
            n = self.root
            print("Root: {:4}\tHeight: {}".format(n.data, height))
        
        for child in children:
            print("Node: {:4}\tHeight: {}".format(child.data, height))


# Helper functions
def dPrint(message):
    if DEBUG: print("\tDebug: {}".format(message))