#include <iostream>
#include <assert.h>
#include "binaryTree.h"

using namespace std;

// Test functions
void testCreateTree(void);

// Helper functions
void printPass(void);

int main(void) {
    testCreateTree();
    return 0;
}

void testCreateTree(void) {
    printf("Test: %s\n", __func__);
    int data = 137;

    // construct a tree 
    BinaryTree tree{data};

    // Test initial tree values
    assert(tree.getHeight() == 0);
    assert(tree.getSize() == 1);
    assert(tree.getRoot() != nullptr);
    assert(tree.getRoot()->parent == nullptr);
    assert(tree.getRoot()->left == nullptr);
    assert(tree.getRoot()->right == nullptr);
    assert(tree.getRoot()->data == data);
    printPass();
    
}

// Helper functions
void printPass(void) {
    cout << "#####\tPASS\t#####\n";
}