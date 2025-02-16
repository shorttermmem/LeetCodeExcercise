# Jump Game Series - Increasing Complexity in DP

## 1. Jump Game (Leetcode 55)
**Problem:** Given an array `nums`, where `nums[i]` represents the maximum jump length from index `i`, determine if you can reach the last index.

### **Difficulty Progression**
- **State:** `dp[i] = true` if index `i` is reachable.
- **Transition:** `dp[i] = dp[j]` for any `j` that can reach `i` (`j + nums[j] >= i`).
- **Optimization:** Can be solved greedily by keeping track of the maximum reachable index.

---

## 2. Jump Game II (Leetcode 45)
**Problem:** Given `nums`, find the minimum number of jumps required to reach the last index.

### **Increased Difficulty**
- **New state:** `dp[i] = min jumps needed to reach i`.
- **Transition:** `dp[i] = min(dp[j]) + 1` where `j` can reach `i`.
- **Greedy approach:** Instead of using DP explicitly, track the farthest index reachable within the current jump range.

---

## 3. Jump Game III (Leetcode 1306)  
**Problem:** Given `nums` and a starting index, determine if you can reach any index with value `0`. You can jump left or right by `nums[i]` steps.  

### **Increased Difficulty**  
- **New constraints:** Can jump **both** left and right, but not beyond array bounds.  
- **State:** `dp[i] = true` if index `i` can reach an index with `0`.  
- **Transition:** `dp[i] = true` if `dp[i + nums[i]] = true` or `dp[i - nums[i]] = true`.  
- **Optimization:** Use **BFS or DFS** to avoid cycles and unnecessary recomputation.  

---  

## 4. Jump Game IV (Leetcode 1345)  
**Problem:** Given `nums`, where you can jump to adjacent indices or any index with the same value, find the minimum jumps to reach the last index.  

### **Increased Difficulty**  
- **New jump condition:** Can jump to **any index with the same value** in addition to adjacent indices.  
- **State:** `dp[i] = min jumps to index i`.  
- **Transition:** `dp[i] = min(dp[i-1], dp[i+1], min(dp[j] for j in indices where nums[j] == nums[i])) + 1`.  
- **Optimization:** Use **BFS** and a **HashMap to track indices with the same value**, marking visited indices to prevent redundant computations.  

---  

## 5. Jump Game V (Leetcode 1340)
**Problem:** Given `nums`, where you can jump left or right up to `d` steps, find the maximum number of indices you can visit starting from any index.

### **Increased Difficulty**
- **New constraints:** Jumps must be within `d`, and only to strictly smaller values.
- **State:** `dp[i] = max steps from index i`.
- **Transition:** `dp[i] = 1 + max(dp[j])` for all valid `j` in range `[i-d, i+d]` where `nums[j] < nums[i]`.
- **Additional complexity:** Sorting-based approach to process smaller elements first.

---

## 6. Jump Game VI (Leetcode 1696)
**Problem:** Given `nums`, where you can jump forward up to `k` steps, find the maximum score you can achieve by summing values along the way.

### **Increased Difficulty**
- **New objective:** Maximize score instead of minimizing jumps.
- **State:** `dp[i] = max score reaching index i`.
- **Transition:** `dp[i] = nums[i] + max(dp[j])`, where `j` is within `k` steps.
- **Optimization:** Use a **monotonic deque** to efficiently find the max of `dp[j]` in O(1) instead of O(k).

---

## 7. Jump Game VII (Leetcode 1871)
**Problem:** You can only jump within `[minJump, maxJump]` and must land on ‘0’ in a binary string.

### **Increased Difficulty**
- **New constraints:** Binary string limits landing positions.
- **State:** `dp[i] = true` if index `i` is reachable.
- **Transition:** `dp[i] = true` if there exists a `j` in `[i - maxJump, i - minJump]` such that `dp[j] = true` and `s[i] = '0'`.
- **Optimization:** Instead of checking all `j`, use a **prefix sum** or **sliding window** to efficiently track reachable indices.

---

## 8. Jump Game VIII (Leetcode 2297)
**Problem:** Given `nums`, where each jump costs a specific price, find the minimum cost to reach the last index.

### **Most Difficult Variant**
- **New complexity:** Jumps now have individual costs.
- **State:** `dp[i] = min cost to reach index i`.
- **Transition:** `dp[i] = min(dp[j] + cost[j])` for all `j` within allowed jumps.
- **Optimization:** **Monotonic deque** to efficiently track the minimum cost in a sliding window.

---

## **Updated Complexity Summary**  
| Problem | Constraints & Complexity |  
|---------|-------------------------|  
| **Jump Game 55** | Basic DP/Greedy (Reachability Check) |  
| **Jump Game 45** | Greedy Optimization (Min Jumps) |  
| **Jump Game III** | Bi-Directional Jumps (Graph Traversal) |  
| **Jump Game IV** | Graph-Based Jumps with Same-Value Indices (BFS + HashMap) |  
| **Jump Game V** | Constrained Jumps with Order Dependency (Sorting + DP) |  
| **Jump Game VI** | Max Score with Range Limitation (Monotonic Deque) |  
| **Jump Game VII** | Binary String Constraints (Prefix Sum/Sliding Window) |  
| **Jump Game VIII** | Min Cost with Variable Jump Cost (Monotonic Deque) |  

The primary difficulty increase comes from:  
- Introducing **bi-directional movement** (Jump Game III).  
- Allowing **non-adjacent jumps via same values** (Jump Game IV).  
- Increasing reliance on **graph traversal techniques** (BFS, HashMap optimizations).  
- Introducing more constraints (limited jump range, order dependency).
- Changing the objective (min/max cost instead of reachability).
- Requiring efficient data structures (monotonic deque, prefix sum, sorting).

