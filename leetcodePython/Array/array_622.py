class MyCircularQueue:
    def __init__(self, k: int):
        self._capacity = k
        self._storage = [0] * self._capacity
        self._count = 0
        self._headIndex = 0
        self._tailIndex = -1

    def enQueue(self, value: int) -> bool:
        if self._count == self._capacity:
            return False
        self._storage[(self._headIndex + self._count) % self._capacity] = value
        self._count += 1
        return True

    def deQueue(self) -> bool:
        if self._count == 0:
            return False
        self._headIndex = (self._headIndex + 1) % self._capacity
        self._count -= 1
        return True

    def Front(self) -> int:
        if self._count == 0:
            return -1
        return self._storage[self._headIndex]

    def Rear(self) -> int:
        if self._count == 0:
            return -1
        return self._storage[(self._headIndex + self._count - 1) % self._capacity]

    def isEmpty(self) -> bool:
        return self._count == 0

    def isFull(self) -> bool:
        return self._count == self._capacity
    
    

"""_summary_
    622. Design Circular Queue

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

--------------------------------------------------
- Array of size k.
- Front: the index of the first element.
- Rear: the index of the last element.
- Count: the number of elements in the queue.


[1, 2]
headIndex = 0, capacity = 2, count = 2
enQueue(3) => [1, 2, 3]

enQueue: 
    # use count as offset from headIndex to insert element
    headIndex + count % capacity 
deQueue:
    # control headIndex to remove element from the front
    _headIndex = headIndex + 1 % capacity 
    
"""
