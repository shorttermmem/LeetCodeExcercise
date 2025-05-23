# Python Tricks for LeetCode Array Problems

## 1. Sorting

### Sort by Key
```python
# Sort courses by their deadlines (ascending order)
courses.sort(key=lambda x: x[1])
```

### Sort in Descending Order
```python
# Sort by the second element in descending order
arr.sort(key=lambda x: x[1], reverse=True)
```

### Sort by Multiple Keys
```python
# Sort by first element, then second element in descending order
arr.sort(key=lambda x: (x[0], -x[1]))
```

## 2. Two-Pointer Techniques

### Find Pair with Target Sum
```python
# Two-pointer technique (sorted array)
left, right = 0, len(arr) - 1
while left < right:
    total = arr[left] + arr[right]
    if total == target:
        break
    elif total < target:
        left += 1
    else:
        right -= 1
```

### Merge Two Sorted Arrays
#### 
```python
# Merge nums1 and nums2 into nums1 (assuming nums1 has enough space)
while m > 0 and n > 0:
    # copying back-to-front
    if nums1[m - 1] > nums2[n - 1]:
        nums1[m + n - 1] = nums1[m - 1]
        m -= 1
    else:
        nums1[m + n - 1] = nums2[n - 1]
        n -= 1
nums1[:n] = nums2[:n]  # Copy remaining elements if any
```

## 3. Sliding Window

### Find Maximum Sum Subarray of Size K
```python
# Sliding window approach
max_sum, curr_sum = 0, sum(arr[:k])
for i in range(k, len(arr)):
    curr_sum += arr[i] - arr[i - k]
    max_sum = max(max_sum, curr_sum)
```

## 4. Prefix Sum

### Compute Prefix Sum Array
```python
# Compute prefix sum array
prefix = [0] * (len(arr) + 1)
for i in range(len(arr)):
    prefix[i + 1] = prefix[i] + arr[i]
```

### Range Sum Query (O(1) per query)
```python
# Sum of arr[l:r] using prefix sum
range_sum = prefix[r] - prefix[l]
```

## 5. Hash Map Tricks

### Find Duplicates
```python
# Find duplicates using Counter
from collections import Counter
duplicates = [k for k, v in Counter(arr).items() if v > 1]
```

### Two Sum (Using Hash Map)
```python
# Find two numbers that sum to target
seen = {}
for num in arr:
    if target - num in seen:
        result = (target - num, num)
    seen[num] = True
```

## 6. Heap (Priority Queue)

### Find K Smallest Elements
```python
import heapq
heapq.nsmallest(k, arr)
```

### Find K Largest Elements
```python
heapq.nlargest(k, arr)
```

### Maintain a Min-Heap of K Largest Elements
```python
heap = []
for num in arr:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)  # Keep only k largest elements

# this may be faster
heap = arr[:k]
heapq.heapify(heap)
for num in arr[k:]:
    if num > heap[0]:
        heapq.heappushpop(heap, num)
```

## 7. List Comprehensions

### Flatten a 2D List
```python
flat_list = [num for row in matrix for num in row]
```

### Filter and Transform
```python
# Square even numbers in the list
squared_evens = [x ** 2 for x in arr if x % 2 == 0]
```

## 8. Matrix Manipulations

### Transpose a Matrix
```python
# *matrix unpacks the rows of the matrix into separate arguments
# zip groups these rows column-wise into tuples.
# map(list, ...) applies the list function to each tuple into a map obj
transposed = list(map(list, zip(*matrix)))
```

### Rotate a Matrix 90 Degrees Clockwise
```python
# *matrix[::-1] unpack reversed order of the rows
# zip groups these rows column-wise into tuples.
rotated = [list(row) for row in zip(*matrix[::-1])]
rotated = list(map(list, zip(*matrix[::-1])))
```

### Spiral Order Traversal
```python
res = []
while matrix:
    res += matrix.pop(0)  # First row
    if matrix and matrix[0]:
        for row in matrix:
            res.append(row.pop())
    if matrix:
        res += matrix.pop()[::-1]  # Last row (reversed)
    if matrix and matrix[0]:
        for row in matrix[::-1]:
            res.append(row.pop(0))
```

## 9. Bitwise Tricks

### Find Unique Element (Single Number)
```python
result = 0
for num in arr:
    result ^= num  # XOR cancels out duplicates
```

### Check if a Number is Power of Two
```python
is_power_of_two = n > 0 and (n & (n - 1)) == 0
```

## 10. Monotonic Stack

### Next Greater Element
```python
stack, res = [], [-1] * len(arr)
for i, num in enumerate(arr):
    while stack and arr[stack[-1]] < num:
        res[stack.pop()] = num
    stack.append(i)
```

## 11. Sweep Line Algorithm

### Interval Counting with Sweep Line
```python
  # Separate and sort the start and end times  
  starts, ends = map(sorted, zip(*events))
  # Calculate overlapping events for each observation time
  # bisect_right(starts, time): Counting how many intervals have started by the given time.
  # bisect_left(ends, time): Counting how many intervals have ended before the given time.
  res = [bisect_right(starts, time) - bisect_left(ends, time) for time in observation_times]
```

```python
  trips = [[2,1,5], [3,3,7]]
  # Outer loop: for n, i, j in trips: [2,1,5], [3,3,7]
  # Inner loop: for x in [[i, n], [j, -n]]  
  # a flattened sequence of all the x pairs from all trips.
  for i, v in sorted(x for n, i, j in trips for x in [[i, n], [j, -n]]):
    # n = 2, i = 1, j = 5 → [[1, 2], [5, -2]].
    # n = 3, i = 3, j = 7 → [[3, 3], [7, -3]].
    # i, v = [1, 2], [3, 3], [5, -2], [7, -3]
```

## 12. Circular Buffer
```python
def circular_loop(arr, start, n):
    for k in range(n):  # Iterate n times
        idx = (start + k) % n  # Circular index
        print(arr[idx])  # Access element at idx

# Example usage
arr = ['A', 'B', 'C', 'D']  # n = 4
start = 2  # Start at 'C'
n = len(arr)
circular_loop(arr, start, n)  # Outputs: C, D, A, B
```

## 13. Interesting case of 2D arrays
```python
# list comprehension method is essential for matrix operations.
# CORRECT APPROACH (independent lists) - Only the modified cell changes in its specific row
correct_grid = [[False for _ in range(3)] for _ in range(2)]
correct_grid[0][0] = True
print("Correct result:", correct_grid)  # [[True, False, False], [False, False, False]]

# WRONG APPROACH (shared references) - All rows change when modifying one cell
wrong_grid = [[False] * 3] * 2
wrong_grid[0][0] = True
print("Wrong result:", wrong_grid)  # [[True, False, False], [True, False, False]]
```
---

This document provides a concise collection of Python tricks commonly used for solving LeetCode array problems efficiently.

