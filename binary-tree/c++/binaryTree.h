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
    BinaryTree();

    // Tree functions
    /* insert:
    * inputs: 
    *   data: data to insert
    *   n: pointer to current node of tree
    *   height: tree height of current insert
    * Returns:
    *   0 if successful, -1 otherwise.
    */
    int insert(struct Node *newNode, struct Node *n, int height=1);

    // Accessors
    int getHeight();
    long int getSize();
    struct Node *getRoot();

    // Print functions
    void print();

private:
    // Root node
    struct Node *root;
    // Height of the tree
    int height;
    // Total number of nodes in the tree
    long int size;
};

// Helper functions
void printLine(std::vector<struct Node *> nodes, std::vector<int> indices);
void getIndexLocations(std::vector<int> &indices, \
    std::vector<int> &parentIndices);
#endif