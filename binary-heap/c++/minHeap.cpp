#include "minHeap.h"

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
    return true;
}

bool MinHeap::find(int key, struct Node *n) {
    return true;
}