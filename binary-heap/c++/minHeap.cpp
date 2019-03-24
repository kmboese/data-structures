#include <iostream>
#include <vector>
#include "minHeap.h"

using std::cout;
using std::vector;

MinHeap::MinHeap() 
    : size{0} {
    this->root = nullptr;
}

// Accessors
unsigned int MinHeap::getSize() {
    return this->size;
}

struct Node *MinHeap::getRoot() {
    return this->root;
}

int MinHeap::getMin() {
    if (!this->root) {
        return ERROR_CODE;
    }
    else {
        return(this->root->data);
    }
}

// Heap functions
bool MinHeap::insert(int data, struct Node *n) {
    // Special case: root is empty
    if (!this->root) {
        struct Node *tmp = new Node;
        tmp->data = data;
        root = tmp;
        this->size++;
        return true;
    }

    // Find leftmost free node to insert
    struct Node *freeParent = findLeftmostParent(this->root);
    struct Node *tmp = new Node;
    tmp->data = data;
    tmp->parent = freeParent;
    if (!freeParent->left) {
        freeParent->left = tmp;
    }
    else {
        freeParent->right = tmp;
    }

    // Percolate the new node up the heap
    percolateUp(tmp);

    return true;
}

struct Node *MinHeap::findLeftmostParent(struct Node *root){
    vector<struct Node*> parents{};
    vector<struct Node*> children{};
    vector<struct Node*> tmp{};
    struct Node *freeParent = nullptr;

    parents.push_back(root);

    while (parents.size() > 0) {
        // Loop through all parents
        for (auto parent : parents) {
            tmp.clear();
            freeParent = parent;
            if (!parent->left || !parent->right) {
                return freeParent;
            }

            // Get each parent's children
            if (parent->left) {
                tmp.push_back(parent->left);
            }
            if (parent->right) {
                tmp.push_back(parent->right);
            }

            // Add children to list of children
            for (auto child : tmp) {
                children.push_back(child);
            }
        }
        parents = children;
        children.clear();
    }

    return freeParent;
}
bool MinHeap::find(int key, struct Node *n) {
    return true;
}

void MinHeap::printDFS(struct Node *n) {
    if (!n) {
        return;
    }

    cout << n->data << " ";
    printDFS(n->left);
    printDFS(n->right);
}

