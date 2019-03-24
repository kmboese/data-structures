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
    assert(tree.size == 0)
    assert(tree.height == 0)
    assert(tree.root is None)
    print("Passed" + divider)

def testTreeWithOneNode():
    print(divider + "Executing testTreeWithOneNode()...")
    tree = BinaryTree()
    tree.insert(Node(0))
    assert(tree.size == 1)
    assert(tree.height == 0)
    print("Passed" + divider)

def testSingleInserts(loops):
    print(divider + "Executing testSingleInserts()...")
    for i in range(loops):
        tree = BinaryTree()
        val = randint(MIN_INT_32, MAX_INT_32)
        tree.insert(Node(val))
        assert(tree.size == 1)
        assert(tree.height == 0)
    print("Passed" + divider)

def testSequentialInsert():
    print(divider + "Executing testSequentialInsert()...")
    tree  = BinaryTree()
    for i in range(1,11):
        tree.insert(Node(i))
    assert(tree.root.data == 1)
    assert(tree.size == 10)
    #print("Tree height is {}, expected to be {}".format(tree.height, 9))
    assert(tree.height == 9)
    print("Passed" + divider)

def testRandomInsert():
    print(divider + "Executing testRandomInsert()...")
    numbers = [7,2,10,4,3,1,5,8,6,9]
    tree = BinaryTree()
    for number in numbers:
        tree.insert(Node(number))
    assert(tree.root.data == 7)
    assert(tree.size == 10)
    print("Tree height is {}, expected to be {}".format(tree.height, 4))
    tree.printDFS()
    print()
    tree.printBFS()
    assert(tree.height == 4)
    print("Passed" + divider)

def testDFSRandom():
    print(divider + "Executing testDFSRandom()...")
    tree = BinaryTree()
    expectedNodes = [32,16,2,5,12,30,18,50,48,53]
    for number in randomNumbers:
        tree.insert(Node(number))
    assert(tree.size == len(randomNumbers))
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

def testFind():
    print(divider + "Executing testFind()...")
    tree = BinaryTree()
    lowerBound = 0
    upperBound = 100

    # Insert values
    for i in range(lowerBound, upperBound):
        tree.insert(Node(i))
    
    # Ensure all inserted values are found
    for i in range(lowerBound, upperBound):
        assert(tree.find(i, tree.root))

    # Ensure values outside of range are not found
    for i in range(-10000, lowerBound):
        assert(not tree.find(i, tree.root))

    for i in range(upperBound, 10000):
        assert(not tree.find(i, tree.root))

    print("Passed " + divider)
    

def main():
    testEmptyTree()
    testTreeWithOneNode()
    testSingleInserts(LONG_TEST_LOOPS)
    testSequentialInsert()
    testRandomInsert()

    # Find
    testFind()

    testDFSRandom()
    testBFSSingleInsert()
    testBFSRandom()

if __name__ == "__main__":
    main()
