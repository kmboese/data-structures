from binaryHeap import BinaryHeap, Node

def main():
    heap = BinaryHeap(5)
    heap.insert(2)
    print("Root node: {}".format(heap.root.data))
    leaf = heap.getLeaf(heap.root)
    print("Leaf: {}".format(leaf.data))

if __name__ == "__main__":
    main()