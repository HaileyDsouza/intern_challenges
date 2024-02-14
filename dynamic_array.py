class DynamicArray:
    
    def __init__(self, capacity: int): #O(n) - n is capacity 
        self.capacity = capacity
        self.size = 0
        self.array = [0] * capacity
    
    def get(self, i: int) -> int: #o(1)
        return self.array[i]

    def insert(self, i: int, n: int) -> None: #o(1)
        self.array[i] = n 

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None: #o(1) - avg case aka am,ortized time complexity
        if self.size == self.capacity:
            self.resize()
        
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int: #o(1)
        self.size -= 1
        return self.array[self.size]
 

    def resize(self) -> None: #O(n)
        self.capacity = self.capacity * 2
        new_array = [0] * self.capacity

        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def getSize(self) -> int:  #O(1)
        return self.size
    
    def getCapacity(self) -> int: #O(1)
        return self.capacity


""" 
Your DynamicArray class should support the following operations:

DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
int get(int i) will return the element at index i. Assume that index i is valid.
void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
void pushback(int n) will push the element n to the end of the array.
int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
void resize() will double the capacity of the array.
int getSize() will return the number of elements in the array.
int getCapacity() will return the capacity of the array.
If we call void pushback(int n) but the array is full, we should resize the array first.
"""