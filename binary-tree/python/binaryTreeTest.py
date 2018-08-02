from binaryTree import Node, BinaryTree, dPrint
from random import randint

# Constants
MAX_INT_32 = 2147483647
MIN_INT_32 = -2147483646
LONG_TEST_LOOPS = 100000

randomNumbers = [32,16,50,30,2,5,18,48,50,12]
divider = "\n***********************************************************\n"

def testEmptyTree():
    print(divider + "Executing testEmptyTree()...")
    tree = BinaryTree()
    assert(tree.elementCount == 0)
    assert(tree.height == 0)
    assert(tree.root == None)
    print("Passed" + divider)

def testTreeWithOneNode():
    print(divider + "Executing testTreeWithOneNode()...")
    tree = BinaryTree()
    tree.insert(Node(0))
    assert(tree.elementCount == 1)
    assert(tree.height == 0)
    assert(tree.root.parent == None)
    print("Passed" + divider)

def testSingleInserts(loops):
    print(divider + "Executing testTreeWithOneNode()...")
    for i in range(loops):
        tree = BinaryTree()
        val = randint(MIN_INT_32, MAX_INT_32)
        tree.insert(Node(val))
        assert(tree.elementCount == 1)
        assert(tree.height == 0)
        assert(tree.root.parent == None)
    print("Passed" + divider)

def main():
    testEmptyTree()
    testTreeWithOneNode()
    testSingleInserts(LONG_TEST_LOOPS)
    '''
    tree = BinaryTree()
    tree.insert(Node(1))
    print("Tree.root.data = {}".format(tree.root.data))

    # Test tree with one node
    assert(tree.elementCount == 1)
    assert(tree.root.parent == None)

    #Test single insert
    tree.insert(Node(2))

    #Test sequential insert
    for i in range(3,10):
        tree.insert(Node(i))

    #Test random insert
    randTree = BinaryTree()
    for number in randomNumbers:
        dPrint("inserting " + str(number))
        randTree.insert(Node(number))
    
    #Test printing trees
    print("Printing tree with sequential elements...")
    tree.printDFS()
    print("\nPrinting tree with random elements...")
    randTree.printDFS()
    '''

if __name__ == "__main__":
    main()
