#include <iostream>
#include <assert.h>
#include <random>

#include "binaryTree.h"

using namespace std;

// Test functions
void testCreateTree(void);
void testSingleInsert(void);
void testMultipleInserts(void);
void testLeftInserts(void);
void testRightInserts(void);
void testBalancedInserts(void);
void testPrint(void);

// Helper functions
void printPass(void);

int main(void) {
    testCreateTree();
    testSingleInsert();
    testMultipleInserts();
    testLeftInserts();
    testRightInserts();
    testBalancedInserts();
    testPrint();
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
    struct Node *root = new Node();
    struct Node *left = new Node();
    struct Node *right = new Node();
    root->data = 5;
    left->data = 3;
    right->data = 7;

    tree.insert(root, tree.getRoot());
    tree.insert(left, tree.getRoot());
    tree.insert(right, tree.getRoot());

    // Verify tree properties
    assert(tree.getHeight() == 1);
    assert(tree.getSize() == 3);
    assert(tree.getRoot() != nullptr);

    // Verify tree data
    assert(tree.getRoot()->data == root->data);
    assert(tree.getRoot()->left->data == left->data);
    assert(tree.getRoot()->right->data == right->data);

    printPass();
}

void testLeftInserts(void) {
    printf("\nTest: %s\n", __func__);
    int count = 10;

    // Create tree
    BinaryTree tree{};

    // Perform only left inserts (reverse order)
    for (int i = count; i > 0; i--) {
        struct Node *tmp = new Node();
        tmp->data = i;
        assert(tree.insert(tmp, tree.getRoot()) == 0);
    }

    // Verify tree properties
    cout << "Tree height: " << tree.getHeight() << endl;
    cout << "Tree size: " << tree.getSize() << endl;
    assert(tree.getHeight() == count-1);
    assert(tree.getSize() == count);

    // Verify tree data
    assert(tree.getRoot()->data == count);

    //tree.print();
    printPass();
}

void testRightInserts(void) {
    printf("\nTest: %s\n", __func__);
    int count = 10;

    // Create tree
    BinaryTree tree{};

    // Perform only right inserts (in order)
    for (int i = 1; i <= count; i++) {
        struct Node *tmp = new Node();
        tmp->data = i;
        assert(tree.insert(tmp, tree.getRoot()) == 0);
    }

    // Verify tree properties
    cout << "Tree height: " << tree.getHeight() << endl;
    cout << "Tree size: " << tree.getSize() << endl;
    assert(tree.getHeight() == count-1);
    assert(tree.getSize() == count);

    // Verify tree data
    assert(tree.getRoot()->data == 1);

    printPass();
}

void testBalancedInserts(void) {
    printf("\nTest: %s\n", __func__);
    std::vector<int> elements = {50, 30, 100, 20, 40, 80, 120, 10, 25, \
        35, 45, 70, 85, 110, 130, 1, 11};
    int inserts = 0;

    // Create tree  
    BinaryTree tree{};

    // Insert root element
    struct Node *root = new Node();
    root->data = elements[0];
    tree.insert(root, tree.getRoot());
    inserts++;

    // Insert balanced elements
    for (unsigned int i = 1; i < elements.size(); i++) {
        struct Node *tmp = new Node();
        tmp->data = elements[i];
        tree.insert(tmp, tree.getRoot());
        inserts++;
    }

    // Verify tree properties
    cout << "Tree height: " << tree.getHeight() << endl;
    cout << "Tree size: " << tree.getSize() << endl;
    //assert(tree.getHeight() == (startRange/step)+1);
    assert(tree.getSize() == inserts);

    // Verify tree data
    assert(tree.getRoot()->data = elements[0]);

    tree.print();

    printPass();
}

void testPrint(void) {
    printf("\nTest: %s\n", __func__);
    int data = 100;

    // Create tree
    BinaryTree tree{};

    struct Node *root = new Node();
    struct Node *left = new Node();
    struct Node *right = new Node();
    struct Node *test = new Node();
    struct Node *test2 = new Node();

    root->data = data;
    left->data = data-1;
    right->data = data+1;
    test->data = 1;
    test2->data = 1000;

    // Insert elements
    tree.insert(root, tree.getRoot());
    tree.insert(left, tree.getRoot());
    tree.insert(right, tree.getRoot());
    tree.insert(test, tree.getRoot());
    tree.insert(test2, tree.getRoot());

    assert(tree.getRoot()->data == data);
    assert(tree.getRoot()->left->data == data-1);
    assert(tree.getRoot()->right->data == data+1);
    assert(tree.getRoot()->left->left->data == test->data);
    assert(tree.getRoot()->right->right->data == test2->data);


    // Print tree
    tree.print();

    printPass();
}

// Helper functions
void printPass(void) {
    cout << "#####\tPASS\t#####\n";
}