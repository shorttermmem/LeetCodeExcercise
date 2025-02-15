# Unique Paths Series - Increasing Complexity in DP

## 1. Unique Paths (Leetcode 62)
**Problem:** Given an `m x n` grid, find the number of unique paths from the top-left to the bottom-right, only moving right or down.

### **Difficulty Progression**
- **State:** `dp[i][j] = number of unique paths to (i, j)`.
- **Transition:** `dp[i][j] = dp[i-1][j] + dp[i][j-1]`.
- **Optimization:** Can reduce to **1D DP** since each cell only depends on the previous row.
- **Complexity:** `O(m * n)`.

---

## 2. Unique Paths II (Leetcode 63)
**Problem:** Same as Unique Paths, but some grid cells are blocked (`0` = free, `1` = obstacle). Find the number of unique paths.

### **Increased Difficulty**
- **New constraint:** Obstacles restrict movement.
- **State:** `dp[i][j] = number of unique paths to (i, j), avoiding obstacles`.
- **Transition:** `dp[i][j] = dp[i-1][j] + dp[i][j-1]` if `grid[i][j] == 0`, otherwise `dp[i][j] = 0`.
- **Optimization:** **1D DP** still works.
- **Complexity:** `O(m * n)`.

---

## 3. Unique Binary Search Trees (Leetcode 96)
**Problem:** Given `n`, find the number of structurally unique BSTs that store values `1` to `n`.

### **Increased Difficulty**
- **New structure:** Trees instead of a grid.
- **State:** `dp[n] = number of unique BSTs with n nodes`.
- **Transition:** `dp[n] = sum(dp[i-1] * dp[n-i])` for `i = 1` to `n` (choosing each `i` as root).
- **Optimization:** **Catalan number formula** can optimize computation.
- **Complexity:** `O(n^2)` DP, `O(n)` with formula.

---

## 4. Unique Binary Search Trees II (Leetcode 95)
**Problem:** Generate all structurally unique BSTs for `n` nodes.

### **Most Difficult Variant**
- **New requirement:** Construct actual trees instead of counting.
- **State:** `dp[i][j] = list of BSTs possible with numbers from i to j`.
- **Transition:** Recursively construct trees using `i` as the root and combining left and right subtree results.
- **Complexity:** `O(Catalan(n))`, requires recursion and memoization.

---

## **Summary of Complexity Increase**
| Problem | Constraints & Complexity |
|---------|-------------------------|
| **Unique Paths (62)** | Basic Grid DP (1D Optimization, `O(m * n)`) |
| **Unique Paths II (63)** | Obstacles restrict movement (`O(m * n)`) |
| **Unique BSTs (96)** | Counting BST structures (`O(n^2)`, Catalan formula) |
| **Unique BSTs II (95)** | Constructing all BSTs (Recursion, `O(Catalan(n))`) |

The increasing difficulty comes from:
- **Introducing obstacles** (restricting valid paths).
- **Shifting from counting to constructing** actual trees.
- **Using Catalan number properties** for efficiency.

