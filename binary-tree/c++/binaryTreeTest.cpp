#include <iostream>
#include <assert.h>
#include <random>

#include "binaryTree.h"

using namespace std;

// Test functions
void testCreateTree(void);

// Helper functions
void printPass(void);
void testSingleInsert(void);
void testMultipleInserts(void);

int main(void) {
    testCreateTree();
    testSingleInsert();
    testMultipleInserts();
    return 0;
}

void testCreateTree(void) {
    printf("Test: %s\n", __func__);

    // construct a tree 
    BinaryTree tree{};

    // Test initial tree values
    assert(tree.getHeight() == 0);
    assert(tree.getSize() == 0);
    assert(tree.getRoot() == nullptr);
    printPass(); 
}

void testSingleInsert(void) {
    printf("\nTest: %s\n", __func__);
    int data = 137;

    // Construct a tree
    BinaryTree tree{};
    struct Node *root = tree.getRoot();
    struct Node *newNode = new Node();
    newNode->data = data;

    // Insert a single element
    assert(tree.insert(newNode, root, tree.getHeight()) == 0);
    assert(tree.getHeight() == 0);
    assert(tree.getSize() == 1);
    assert(tree.getRoot() != nullptr);
    assert(tree.getRoot()->data == data);

    printPass(); 
}

void testMultipleInserts(void) {
    printf("\nTest: %s\n", __func__);

    // Create tree
    BinaryTree tree{};

    // Perform a two inserts to trigger a left insert
    struct Node *node1 = new Node();
    struct Node *node2 = new Node();
    node1->data = 5;
    node2->data = 3;

    tree.insert(node1, tree.getRoot());
    tree.insert(node2, tree.getRoot());

    // Verify tree properties
    assert(tree.getHeight() == 1);
    assert(tree.getSize() == 2);
    assert(tree.getRoot() != nullptr);

    // Verify tree data
    assert(tree.getRoot()->data == node1->data);
    assert(tree.getRoot()->left->data == node2->data);

    printPass();
}

// Helper functions
void printPass(void) {
    cout << "#####\tPASS\t#####\n";
}