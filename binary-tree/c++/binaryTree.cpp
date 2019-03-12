#include <iostream>
#include <vector>

#include "binaryTree.h"

BinaryTree::BinaryTree() {

    // Assign root node
    this->root = nullptr;
    // Set height and size
    this->height = 0;
    this->size = 0;
}

/* ***** Binary Tree functions ***** */
int BinaryTree::insert(struct Node *newNode, struct Node *parent, int height) {

    // Insert into empty tree
    if (this->size == 0) {
        this->root = newNode;
        this->size++;
        return 0;
    }

    // If not empty, ensure node ptr exists
    if (!parent) {
        return -1;
    }

    // Insert left
    else if (newNode->data <= parent->data) {
        // Insert left if no left child
        if (!(parent->left)) {
            // Set parent left and new node's parent
            parent->left = newNode;
            newNode->parent = parent;

            // Update height if changed
            if (height > this->height) {
                this->height = height;
            }
            
            // Update size
            this->size++;
            return 0;
        }
        // Otherwise recursively insert left
        else {
            return(insert(newNode, parent->left, height++));
        }
    }

    // TO-DO: insert right
    else {
        return 0;
    }
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