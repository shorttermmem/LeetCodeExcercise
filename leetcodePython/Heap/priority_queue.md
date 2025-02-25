# `heapq` API Summary for LeetCode Problems

## 1. Basic Min-Heap Operations
```python
import heapq

heap = []
heapq.heappush(heap, 5)  # Insert element
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)

min_elem = heapq.heappop(heap)  # Remove & return smallest element
top_elem = heap[0]  # Peek smallest element without removing
```
*️⃣ **Alternative**: `heapq.heappushpop(heap, x)` inserts `x` then pops the smallest (more efficient than separate push + pop).

---

## 2. Convert List into Heap
```python
nums = [5, 2, 8, 3]
heapq.heapify(nums)  # In-place conversion (O(n) time complexity)
```
*️⃣ **Use Case**: When starting with an unsorted list instead of inserting one by one.

---

## 3. Max-Heap with Negated Values (Python Has Min-Heap by Default)
```python
heap = []
heapq.heappush(heap, -5)  # Insert as negative value
heapq.heappush(heap, -2)
heapq.heappush(heap, -8)

max_elem = -heapq.heappop(heap)  # Convert back to positive
```
*️⃣ **Alternative**: Use tuples like `(priority, value)` for complex objects.

---

## 4. Retrieve k Smallest/Largest Elements
```python
nums = [5, 2, 8, 3, 9, 1]
smallest_k = heapq.nsmallest(3, nums)  # [1, 2, 3]
largest_k = heapq.nlargest(3, nums)    # [9, 8, 5]
```
*️⃣ **Use Case**: More efficient than sorting when only `k` elements are needed.

---

## 5. Efficient k-Largest with Fixed-Size Heap
```python
nums = [5, 2, 8, 3, 9, 1]
heap = []

for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > 3:  # Keep heap size at k
        heapq.heappop(heap)

# Heap contains 3 largest elements, smallest among them at top
result = heapq.heappop(heap)  # Third largest element
```
*️⃣ **Use Case**: Efficient for streaming data or when `k` is small.

---

## 6. Merge k Sorted Lists (Heap-Based Merge Sort)
```python
lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
heap = []

for i, lst in enumerate(lists):
    if lst:
        heapq.heappush(heap, (lst[0], i, 0))  # (value, list index, element index)

merged = []
while heap:
    val, list_idx, elem_idx = heapq.heappop(heap)
    merged.append(val)
    if elem_idx + 1 < len(lists[list_idx]):
        heapq.heappush(heap, (lists[list_idx][elem_idx + 1], list_idx, elem_idx + 1))
```
*️⃣ **Use Case**: Common pattern in merging sorted sequences (e.g., K-way merge).

---

### 🚨 Notes:
- **Heap Size Matters**: Keeping a heap of size `k` is often more efficient than sorting.
- **Tuple Sorting**: When dealing with objects, tuples `(priority, item)` help maintain order.
- **Negative Values for Max-Heap**: Python does not have a built-in max-heap, so use negation.

---
**🔹 Use this as a quick reference for solving priority queue-related problems on LeetCode.**