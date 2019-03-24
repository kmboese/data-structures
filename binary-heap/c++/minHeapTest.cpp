#include <iostream>
#include <assert.h>
#include "minHeap.h"

using namespace std;

void testCreateHeap();

// Helper functions
void printPassed();

int main(int argc, char **argv) {
    testCreateHeap();
    return 0;
}

void testCreateHeap() {
    printf("\nTest: %s\n", __func__);
    MinHeap heap{};
    assert(heap.getSize() == 0);
    assert(!heap.getRoot());

    printPassed();
}

void printPassed() {
    cout << "***** PASS *****\n";
}