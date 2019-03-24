#ifndef BINARYHEAP_H
#define BINARYHEAP_H

struct Node {
    struct Node *left;
    struct Node *right;
    struct Node *parent;
    int data;

};


// MinHeap is implemented as a min heap binary heap
class MinHeap {
public:

    // Default constructor
    MinHeap();

    /* Inserts an element into a min-heap.
     * Returns: true if insert succeeds, false otherwise. 
     */
    bool insert(int data, struct Node *n);

    /* Find an element in a min-heap.
     * Returns: true if element exists in the heap, false otherwise.
     */
    bool find(int key, struct Node *n);

private:
    int size;
    struct Node *root;

    
};

#endif