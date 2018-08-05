import sys
sys.path.insert(0, 'D:\github-projects\data-structures\shared')
from node import Node


class BinaryHeap():
    def __init__(self,data):
        self.root = Node(data)