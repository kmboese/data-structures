#include <iostream>
#include <assert.h>
#include "minHeap.h"

using namespace std;

void testCreateHeap();
void testSingleInsert();
void testSequentialInsert();

// Helper functions
void printPassed();

int main(int argc, char **argv) {
    testCreateHeap();
    testSingleInsert();
    testSequentialInsert();
    return 0;
}

void testCreateHeap() {
    printf("\nTest: %s\n", __func__);
    MinHeap heap{};
    assert(heap.getSize() == 0);
    assert(!heap.getRoot());

    printPassed();
}

void testSingleInsert() {
    printf("\nTest: %s\n", __func__);
    int el = -1;
    // Leftmost parent
    struct Node *lmp;

    MinHeap heap{};
    heap.insert(el, heap.getRoot());
    // The LMP is the root in this example
    lmp = heap.findLeftmostParent(heap.getRoot());


    assert(heap.getSize() == 1);
    assert(heap.getRoot()->data == el);
    assert(lmp->data == el);

    heap.printDFS(heap.getRoot());

    printPassed();
}

void testSequentialInsert() {
    printf("\nTest: %s\n", __func__);

    MinHeap heap{};
    int lowerBound = 1;
    int upperBound = 10;

    // Insert elements
    for (int i = lowerBound; i < upperBound; i++) {
        heap.insert(i, heap.getRoot());
    }

    

    printPassed();
}

void printPassed() {
    cout << "\n***** PASS *****\n";
}