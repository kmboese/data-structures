from binaryTree import Node, BinaryTree, dPrint
from random import randint

def main():
    tree = BinaryTree()
    print("Tree.root.data = {}".format(tree.root.data))

    #Test single insert
    tree.insert(Node(1))

    #Test sequential insert
    for i in range(2,10):
        tree.insert(Node(i))

    #Test random insert
    randTree = BinaryTree()
    for i in range(0,10):
        value = randint(1,50)
        dPrint("inserting " + str(value))
        randTree.insert(Node(value))
    
    #Test printing trees
    print("Printing tree with sequential elements...")
    tree.printDFS()
    print("\nPrinting tree with random elements...")
    randTree.printDFS()

if __name__ == "__main__":
    main()
