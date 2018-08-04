DEBUG = False

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

    def getNodesDFS(self, n=None, nodes=[]):
        if not self.root:
            print("Error in getNodesDFS(): tree is empty")
        # Handle initial insert
        if not n:
            n = self.root
            nodes.append(n)
        # Standard insert
        else:
            nodes.append(n)
        # Recurse down the tree
        if n.left:
            self.getNodesDFS(n.left, nodes)
        if n.right:
            self.getNodesDFS(n.right, nodes)
        return nodes

    def getNodesBFS(self):
        nodes = []
        queue = []
        children = []
        if not self.root:
            print("Error in getNodesBFS: tree is empty")
        nodes.append(self.root)
        queue.append(self.root)
        while len(queue) > 0:
            children = queue[0].getChildren()
            for child in children:
                nodes.append(child)
                queue.append(child)
            queue.remove(queue[0])
        return nodes
        
        

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

def nodesToString(nodes):
    ret = ""
    for node in nodes:
        ret += str(node.data) + " "
    #ret += "\n"
    return ret