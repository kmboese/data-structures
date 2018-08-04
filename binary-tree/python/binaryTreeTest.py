from binaryTree import Node, BinaryTree, nodesToString
from random import randint

# Constants
MAX_INT_32 = 2147483646
MIN_INT_32 = -2147483646
LONG_TEST_LOOPS = 100000

randomNumbers = [32,16,50,2,30,5,18,12,48,53]
divider = "\n***********************************************************\n"

def testEmptyTree():
    print(divider + "Executing testEmptyTree()...")
    tree = BinaryTree()
    assert(tree.elementCount == 0)
    assert(tree.height == 0)
    assert(tree.root is None)
    print("Passed" + divider)

def testTreeWithOneNode():
    print(divider + "Executing testTreeWithOneNode()...")
    tree = BinaryTree()
    tree.insert(Node(0))
    assert(tree.elementCount == 1)
    assert(tree.height == 0)
    assert(tree.root.parent is None)
    print("Passed" + divider)

def testSingleInserts(loops):
    print(divider + "Executing testTreeWithOneNode()...")
    for i in range(loops):
        tree = BinaryTree()
        val = randint(MIN_INT_32, MAX_INT_32)
        tree.insert(Node(val))
        assert(tree.elementCount == 1)
        assert(tree.height == 0)
        assert(tree.root.parent is None)
    print("Passed" + divider)

def testDFSRandom():
    print(divider + "Executing testDFSRandom()...")
    tree = BinaryTree()
    expectedNodes = [32,16,2,5,12,30,18,50,48,53]
    for number in randomNumbers:
        tree.insert(Node(number))
    assert(tree.elementCount == len(randomNumbers))
    nodes = tree.getNodesDFS()
    print("Returned nodes = {}".format(nodesToString(nodes)))
    print("Expected nodes = {}".format([n for n in expectedNodes]))
    
    # Ensure that the order of the nodes is in the proper order for DFS
    for i in range(0,len(nodes)):
        assert(nodes[i].data == expectedNodes[i])
    print("Passed" + divider)
    
def testBFSSingleInsert():
    print(divider + "Executing testBFSSingleInsert()...")
    nodes = []
    tree = BinaryTree()
    tree.insert(Node(7))
    nodes = tree.getNodesBFS()
    print(nodesToString(nodes))
    assert(nodes[0].data == 7)
    print("Passed" + divider)

def testBFSRandom():
    print(divider + "Executing testBFSRandom()...")
    tree = BinaryTree()
    expectedNodes = [32,16,50,2,30,48,53,5,18,12]
    for num in randomNumbers:
        tree.insert(Node(num))
    bfsNodes = tree.getNodesBFS()
    print(nodesToString(bfsNodes))
    # Ensure that the order of the nodes is in the proper order for BFS
    for i in range(0, len(expectedNodes)):
        assert(bfsNodes[i].data == expectedNodes[i])
    print("Passed" + divider)
    


def main():
    testEmptyTree()
    testTreeWithOneNode()
    testSingleInserts(LONG_TEST_LOOPS)
    testDFSRandom()
    testBFSSingleInsert()
    testBFSRandom()
    '''
    tree = BinaryTree()
    tree.insert(Node(1))
    print("Tree.root.data = {}".format(tree.root.data))

    # Test tree with one node
    assert(tree.elementCount == 1)
    assert(tree.root.parent is None)

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
