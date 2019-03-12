#ifndef BINARYTREE_H
#define BINARYTREE_H

struct Node {
    struct Node *parent;
    struct Node *left;
    struct Node *right;
    int data;
};

#endif