# Python Study Notes: Combinatoric Iterators, Collections, and Functools

## itertools: Combinatoric Iterators

### 1. `permutations(iterable, r=None)`
- Generates all possible orderings of `r` elements.
- Default `r` is the length of `iterable`.

```python
from itertools import permutations
list(permutations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
```

### 2. `combinations(iterable, r)`
- Generates all unique selections of `r` elements, order does not matter.

```python
from itertools import combinations
list(combinations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 3)]
```

### 3. `combinations_with_replacement(iterable, r)`
- Like `combinations`, but allows repeated elements.

```python
from itertools import combinations_with_replacement
list(combinations_with_replacement([1, 2, 3], 2))
# [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
```

### 4. `product(iterable, repeat=1)`
- Cartesian product of input iterables (like nested loops).

```python
from itertools import product
list(product([1, 2], repeat=2))
# [(1, 1), (1, 2), (2, 1), (2, 2)]
```

---

## collections: Most Used Classes

### 1. `deque`
- Efficient for queue operations (O(1) append and pop from both ends).

```python
from collections import deque
d = deque([1, 2, 3])
d.append(4)    # [1, 2, 3, 4]
d.appendleft(0) # [0, 1, 2, 3, 4]
d.pop()        # [0, 1, 2, 3]
d.popleft()    # [1, 2, 3]
# Rotate elements

d.rotate(1)  # [3, 1, 2]
d.rotate(-1) # [1, 2, 3]
```

### 2. `Counter`
- Counts occurrences of elements in an iterable.

```python
from collections import Counter
c = Counter("aabbccaa")
print(c)  # Counter({'a': 4, 'b': 2, 'c': 2})
print(c.most_common(2))  # [('a', 4), ('b', 2)]
print(list(c.items()))  # [('a', 4), ('b', 2), ('c', 2)]
print(list(c.elements()))  # ['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c']
```

### 3. `OrderedDict`
- Maintains insertion order (since Python 3.7, `dict` does this too).

```python
from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# Move key to end or beginning
od.move_to_end('a')  # Moves 'a' to the end
od.move_to_end('b', last=False)  # Moves 'b' to the beginning
```

### 4. `defaultdict`
- Similar to `dict`, but provides a default value for missing keys.

```python
from collections import defaultdict
dd = defaultdict(int)  # Default value is 0
dd['a'] += 1  # {'a': 1}

# Using list as default factory
dd_list = defaultdict(list)
dd_list['a'].append(1)
print(dd_list)  # defaultdict(<class 'list'>, {'a': [1]})
```

---

## functools: Useful for LeetCode

### 1. `lru_cache`
- Memoization to optimize recursive functions.

```python
from functools import lru_cache
@lru_cache(None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
print(fib(10))  # 55
print(fib.cache_info())  # Cache stats
```

### 2. `reduce`
- Applies a function cumulatively to an iterable.

```python
from functools import reduce
reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 24 (1*2*3*4)
```

### 3. `cmp_to_key`
- Converts a comparison function to a key function for sorting.

```python
from functools import cmp_to_key
def compare(x, y):
    return x - y
sorted([3, 1, 4, 1, 5], key=cmp_to_key(compare))
# [1, 1, 3, 4, 5]
```

---

### Summary
| Module | Utility | Use Case |
|--------|---------|----------|
| `itertools` | `permutations` | Generate all orderings |
| `itertools` | `combinations` | Select `r` elements ignoring order |
| `itertools` | `combinations_with_replacement` | Allow repeated selections |
| `itertools` | `product` | Cartesian product |
| `collections` | `deque` | Fast queue operations (rotate, pop, append) |
| `collections` | `Counter` | Count occurrences, list items, and elements |
| `collections` | `OrderedDict` | Maintain order, move keys |
| `collections` | `defaultdict` | Default values for missing keys |
| `functools` | `lru_cache` | Memoization, cache stats |
| `functools` | `reduce` | Apply function cumulatively |
| `functools` | `cmp_to_key` | Custom sorting |

These utilities are powerful for solving LeetCode problems efficiently. Use them where applicable to write clean and optimized solutions.

