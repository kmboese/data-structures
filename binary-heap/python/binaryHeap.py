import sys
sys.path.insert(0, 'C:\github-projects\data-structures\shared')
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
        return leaf
    
    def getLeaf(self, node):
        if not node:
            return
        if node.left:
            getLeaf(node.left)
        if node.right:
            getLeaf(node.right)
        return node
