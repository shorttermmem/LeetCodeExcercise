#https://leetcode.com/problems/lru-cache/

from common_types import *

"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
* ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
* [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.

"""

class Node:
    def __init__(self, key=-1, val=-1, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.key = key
        self.val = val
        
            
class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._dataMap = {}
        self._dummyHead = Node()
        self._dummyTail = Node()
        self._dummyHead.next = self._dummyTail
        self._dummyTail.prev = self._dummyHead
        return

    def _removeNode(self, node):
        prev, nxt = node.prev, node.next
        node.prev = None
        node.next = None
        prev.next, nxt.prev = nxt, prev
        return

    def _appendLeft(self, node):
        prev = self._dummyHead
        nxt = self._dummyHead.next
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node
        return

    def get(self, key: int) -> int:
        if key not in self._dataMap:
            return -1
        dataNode = self._dataMap[key]
        self._removeNode(dataNode)
        self._appendLeft(dataNode)
        return dataNode.val
        

    def put(self, key: int, value: int) -> None:
        if key not in self._dataMap:
            dataNode = Node(key, value, None, None)
            self._appendLeft(dataNode)
            self._dataMap[key] = dataNode
            if len(self._dataMap) > self._capacity:
                removeKey = self._dummyTail.prev.key
                self._removeNode(self._dummyTail.prev)
                self._dataMap.pop(removeKey)
        else:
            dataNode = self._dataMap[key]
            dataNode.val = value
            self.get(key)
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)