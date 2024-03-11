class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index):
        if index < 0 or index >= self.length:
            return -1

        if index < self.length // 2:
            currNode = self.head
            for _ in range(index):
                currNode = currNode.next
        else:
            currNode = self.tail
            for _ in range(self.length - 1, index, -1):
                currNode = currNode.prev

        return currNode.val

    def addAtHead(self, val):
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length += 1

    def addAtTail(self, val):
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.length:
            return

        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            newNode = Node(val)
            currNode = self.head
            for _ in range(index):
                currNode = currNode.next
            newNode.prev = currNode.prev
            newNode.next = currNode
            currNode.prev.next = newNode
            currNode.prev = newNode
            self.length += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.length:
            return
        
        #index at start 
        if index == 0:
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        #index at end
        elif index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            #index at middle 
            currNode = self.head
            for _ in range(index):
                currNode = currNode.next
            currNode.prev.next = currNode.next
            currNode.next.prev = currNode.prev
        self.length -= 1

"""Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid."""