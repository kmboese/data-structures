#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>

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
            return(insert(newNode, parent->left, height+1));
        }
    }

    // Insert right
    else {
        // Insert right if no right child
        if (!(parent->right)) {
            // Set parent left and new node's parent
            parent->right = newNode;
            newNode->parent = parent;

            // Update height if changed
            if (height > this->height) {
                this->height = height;
            }
            
            // Update size
            this->size++;
            return 0;
        }
        // Otherwise recursively insert right
        else {
            return(insert(newNode, parent->right, height+1));
        }
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

/* Print Functions */
void BinaryTree::print() {
    if (this->size == 0) {
        std::cerr << "Error: cannot print empty tree\n";
        return;
    }

    // Height used to format printing
    int width = pow(2, height+1)-1;
    int offset = this->height;
    std::vector<struct Node*> parents{};
    std::vector<int> parentIndices{};
    std::vector<struct Node*> children{};
    std::vector<int> indices{};
    // Initialize vectors
    for (int i = 0; i < width; i++) {
        indices.push_back(0);
    }
    //bool root = true;

    // Print root first
    parents.push_back(this->getRoot());
    indices[width/2] = 1;
    parentIndices.push_back(width/2);
    printLine(parents, indices);
    
    while (parents.size() != 0) {
        // Zero out indices
        std::fill(indices.begin(), indices.end(), 0);

        // Set indices to be printed and collect children
        for (unsigned int i = 0; i < parents.size(); i++) {
            struct Node *tmp = parents[i];
            
            // Add children's children
            if (tmp->left) {
                children.push_back(tmp->left);
                indices[parentIndices.back()-offset] = 1;
            }
            if (tmp->right) {
                children.push_back(tmp->right);
                indices[parentIndices.back()+offset] = 1;
            }

            // Remove parent
            //parents.pop_back();
            parentIndices.pop_back();
        }
        printLine(children, indices);
        // Reduce offset
        offset--;
        // Previous children become next parents
        parents = children;
        // Indices become new parentIndices
        parentIndices.clear();
        getIndexLocations(indices, parentIndices);
        // Clear the old children
        children.clear();
        //std::reverse(parents.begin(), parents.end());
    }

}

void printLine(std::vector<struct Node *> nodes, std::vector<int> indices) {
    std::string sep = "____";
    int nodeIndex = 0;
    for (auto i : indices) {
        if (i == 1) {
            std::cout << nodes[nodeIndex]->data;
            nodeIndex++;
        }
        else {
            std::cout << sep;
        }
    }
    std::cout << std::endl;
}

void getIndexLocations(std::vector<int> &indices, \
    std::vector<int> &parentIndices) {
        for (int i = (int)indices.size()-1; i > 0; i--) {
            if (indices[i] == 1) {
                parentIndices.push_back(i);
            }
        }
}