import sys
sys.path.insert(0, 'D:\github-projects\data-structures\shared')
from node import Node

# Binary heap: implementation of a max heap
# Definition:
    # Parent node: must be greater than each of its children
    # Insert: insert a new node at the leftmost available leaf
    # and percolateUp() until the new node satisfies the parent requirement
class BinaryHeap:
    def __init__(self,data):
        self.root = Node(data)
        self.nodeCount = 1

    def insert(self, data):
        leaf = self.getLeaf(self.root)
        # Percolate new node up heap
        percolateUp(leaf, data)
        self.nodeCount += 1
    
    def getLeaf(self, node):
        if not node:
            return
        if node.left:
            getLeaf(node.left)
        if node.right:
            getLeaf(node.right)
        return node

    # Percolate new node up the heap until it satisfies min-heap requirements
    def percolateUp(parent, newNode):
        # If data is greater than parent, we can insert
        if newNode.data > parent.data:
            if not parent.left:
                parent.left = newNode
            elif not parent.right:
                parent.right = newNode
            else:
                print("Error: parent for percolate has no available children")
                return
        # Else swap with parent
        else:
            newNode.parent = parent.parent
            parent.parent = newNode
            newNode.




