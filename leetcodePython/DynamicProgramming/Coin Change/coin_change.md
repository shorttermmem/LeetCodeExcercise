# Coin Change Series - Increasing Complexity in DP

## 1. Coin Change (Leetcode 322)
**Problem:** Given an array `coins` representing different denominations and an integer `amount`, determine the minimum number of coins needed to make up `amount`. If it is not possible, return `-1`.

### **Difficulty Progression**
- **State:** `dp[i] = min coins needed to make amount i`.
- **Transition:** `dp[i] = min(dp[i - coin] + 1)` for each coin in `coins`.
- **Optimization:** Uses **bottom-up DP** with a **1D array**.
- **Complexity:** `O(n * amount)` where `n` is the number of coins.

---

## 2. Coin Change II (Leetcode 518)
**Problem:** Given `coins` and an `amount`, find the number of ways to make up the amount using given coins (unlimited usage).

### **Increased Difficulty**
- **New objective:** Count combinations instead of minimizing coins.
- **State:** `dp[i] = number of ways to make amount i`.
- **Transition:** `dp[i] += dp[i - coin]` for each coin in `coins`.
- **Optimization:** Uses a **1D DP array**, updating from smallest to largest amount to avoid recomputation.
- **Complexity:** `O(n * amount)`, but different transition logic from 322.

---

## 3. Minimum Cost to Make Change (Leetcode 1039 - Variant)
**Problem:** Given `coins` and `amount`, but each coin has an associated cost, find the minimum cost to make up `amount`.

### **Increased Difficulty**
- **New constraint:** Coins have an associated usage cost.
- **State:** `dp[i] = min cost to make amount i`.
- **Transition:** `dp[i] = min(dp[i - coin] + cost[coin])` for each coin.
- **Optimization:** Uses **priority queue** (Dijkstra-like approach) for efficiency.

---

## 4. Coin Change with Limited Supply (Leetcode 1845 - Variant)
**Problem:** Each coin has a limited number of times it can be used to make up `amount`.

### **Increased Difficulty**
- **New constraint:** Each coin has a usage limit.
- **State:** `dp[i][j] = min coins needed to make amount i using first j coins`.
- **Transition:** `dp[i] = min(dp[i - coin] + 1, dp[i])`, but bounded by the limit.
- **Optimization:** Uses **Knapsack-like DP** with **2D or compressed 1D array**.

---

## 5. Coin Change with Exact K Coins (Leetcode 1449 - Variant)
**Problem:** Find the maximum number (as a string) that can be formed using exactly `K` coins.

### **Increased Difficulty**
- **New constraint:** Must use exactly `K` coins.
- **State:** `dp[i][j] = max number formed using `i` amount and `j` coins`.
- **Transition:** `dp[i][j] = max(dp[i - coin][j - 1] + digit)`.
- **Optimization:** **Digit-based DP** instead of sum-based.

---

## **Summary of Complexity Increase**
| Problem | Constraints & Complexity |
|---------|-------------------------|
| **Coin Change (322)** | Min coins for amount (1D DP, `O(n * amount)`) |
| **Coin Change II (518)** | Count ways to make amount (1D DP, `O(n * amount)`) |
| **Min Cost to Make Change (1039 Variant)** | Each coin has a cost (Dijkstra-like DP) |
| **Coin Change with Limited Supply (1845 Variant)** | Limited coin usage (Knapsack-like DP) |
| **Coin Change with Exact K Coins (1449 Variant)** | Exact `K` coins constraint (Digit DP) |

The increasing difficulty comes from:
- **New constraints** (limited usage, associated costs, exact number of coins).
- **Different objectives** (min coins vs. counting ways vs. maximizing value).
- **More efficient data structures** (priority queue, Knapsack DP, digit-based DP).

