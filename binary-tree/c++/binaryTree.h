#ifndef BINARYTREE_H
#define BINARYTREE_H

struct Node {
    struct Node *parent;
    struct Node *left;
    struct Node *right;
    int data;
};

class BinaryTree {

public:
    // Constructors
    BinaryTree(int data);

    // Tree functions
    void insert(int data, struct Node *n);

    // Accessors
    int getHeight();
    long int getSize();
    struct Node *getRoot();

private:
    // Root node
    struct Node *root;
    // Height of the tree
    int height;
    // Total number of nodes in the tree
    long int size;
};

#endif