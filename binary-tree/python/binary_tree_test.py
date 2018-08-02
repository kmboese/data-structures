from binary_tree import Node, BinaryTree, dPrint
from random import randint
import copy
def main():
    tree = BinaryTree()

    #Test single insert
    tree.insert(Node(1))

    #Test sequential insert
    for i in range(2,10):
        tree.insert(Node(i))

    #Test DFS
    DFSTree = BinaryTree()
    data = [17,44,13,41,11,15,22]
    for num in data:
        DFSTree.insert(Node(num))
    
    #Test printing trees
    print("Printing tree with sequential elements...")
    tree.printDFS()
    print("\nPrinting tree with random elements...")
    DFSTree.printDFS()

if __name__ == "__main__":
    main()
