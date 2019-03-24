import sys
from os.path import abspath

'''
# Work Node directory
node_dir = abspath('C:/github-projects/data-structures/shared/')
# Home Node directory
#node_dir = r'D:\github-projects\data-structures\shared'
sys.path.insert(0, node_dir)
from node import Node
'''

DEBUG = True

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
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
        self.size = 0
        self.height = 0

    def insert(self, n, current = None, height=1):
        # Special case: insert into an empty tree
        if self.size == 0:
            self.root = n
            self.size += 1
            return

        # By default, start inserts at the root node
        if current is None:
            current = self.root

        # Insert left
        if (n.data <= current.data):
            if (current.left is None):
                current.left = n
                n.parent = current
                if (height > self.height):
                    self.height = height
                self.size += 1
            else:
                height += 1
                self.insert(n, current.left, height)

        # Insert right
        else:
            if (current.right is None):
                current.right = n
                n.parent = current
                if (height > self.height):
                    self.height = height
                self.size += 1
            else:
                height += 1
                self.insert(n, current.right, height)

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
        # Handle the root node
        nodes.append(self.root)
        queue.append(self.root)

        # Get all child nodes at each level
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
            # Base case: node is the root
        if not n:
            print("DFS: The tree has {} elements and is height {}".\
                format(self.size, self.height))   
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
                format(self.size, self.height))
            n = self.root
            print("Root: {:4}\tHeight: {}".format(n.data, height))
        
        for child in children:
            print("Node: {:4}\tHeight: {}".format(child.data, height))


# Helper functions
def dPrint(message):
    if DEBUG: print("\tDebug: {}".format(message))

def nodesToString(nodes):
    ret = ""
    for node in nodes:
        ret += str(node.data) + " "
    #ret += "\n"
    return ret