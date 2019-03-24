#ifndef MINHEAP_H
#define MINHEAP_H

#include <limits>

const int ERROR_CODE = std::numeric_limits<int>::min();

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

    /* ***** Accessors ***** */
    // Returns the size of the minHeap
    unsigned int getSize();
    
    // Returns the root of the minheap
    struct Node *getRoot();

    // Returns the minimum element of the heap
    int getMin();

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