#include <iostream>
#include <vector>

#include "binaryTree.h"

BinaryTree::BinaryTree(int data) {
    struct Node *tmp = new Node;
    tmp->parent = nullptr;
    tmp->left = nullptr;
    tmp->right = nullptr;
    tmp->data = data;

    // Assign root node
    this->root = tmp;
    // Set height and size
    this->height = 0;
    this->size = 1;
}

/* ***** Binary Tree functions ***** */
void BinaryTree::insert(int data, struct Node *n) {
    
}

/* ***** Accessors ***** */
int BinaryTree::getHeight() {
    return this->height;
}

long int BinaryTree::getSize() {
    return this->size;
}

struct Node *BinaryTree::getRoot() {
    return this->root;
}