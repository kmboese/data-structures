from linkedList import Node, LinkedList

def main():
    LL = LinkedList()
    for i in range(1,10,2):
        LL.insert(i)
    LL.traverse()

if __name__ == "__main__":
    main()