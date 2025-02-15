## Best Time to Buy and Sell Stock Problems

These "Best Time to Buy and Sell Stock" problems on LeetCode introduce additional constraints and variations that progressively increase the difficulty. Below is a structured breakdown of how they evolve:

---

### **1. Problem #121: Best Time to Buy and Sell Stock (One Transaction)**
**🔹 Difficulty:** Easy  
**🔹 Constraints:** Only **one** transaction (one buy, one sell).  
**🔹 Approach:**  
- Track the minimum price so far.
- Compute the max profit if selling at the current price.

**🔹 State Transition:**  
Let `min_price` be the minimum price seen so far and `max_profit` be the max profit at any step.  
```
max_profit = max(max_profit, price[i] - min_price)
min_price = min(min_price, price[i])
```

**🔹 Complexity:** \(O(n)\), single pass.

---

### **2. Problem #122: Best Time to Buy and Sell Stock II (Infinite Transactions)**
**🔹 Difficulty:** Medium  
**🔹 Constraints:** Can make **multiple** transactions (buy-sell multiple times).  
**🔹 Approach:**  
- The goal is to accumulate profit whenever the price goes up.
- Greedy approach: Buy at local minima and sell at local maxima.

**🔹 State Transition:**  
Define `dp[i][0]` (holding stock) and `dp[i][1]` (not holding stock).  
```
dp[i][0] = max(dp[i-1][0], dp[i-1][1] - price[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] + price[i])
```
Can be optimized to \(O(1)\) space.

**🔹 Complexity:** \(O(n)\).

---

### **3. Problem #123: Best Time to Buy and Sell Stock III (At Most Two Transactions)**
**🔹 Difficulty:** Hard  
**🔹 Constraints:** **At most two** transactions.  
**🔹 Approach:**  
- Use **four states**:  
  - `firstBuy`: Best profit after **first buy**.
  - `firstSell`: Best profit after **first sell**.
  - `secondBuy`: Best profit after **second buy**.
  - `secondSell`: Best profit after **second sell**.

**🔹 State Transition:**  
```
firstBuy = max(firstBuy, -price[i])
firstSell = max(firstSell, firstBuy + price[i])
secondBuy = max(secondBuy, firstSell - price[i])
secondSell = max(secondSell, secondBuy + price[i])
```

**🔹 Complexity:** \(O(n)\), single pass.

---

### **4. Problem #188: Best Time to Buy and Sell Stock IV (At Most K Transactions)**
**🔹 Difficulty:** Hard  
**🔹 Constraints:** **At most k** transactions.  
**🔹 Approach:**  
- Use `dp[i][j]`: max profit on day `i` with `j` transactions.  
- Use a variation of the `Buy-Sell` DP transitions.

**🔹 State Transition:**  
```
dp[i][j] = max(dp[i-1][j], max(dp[l][j-1] + price[i] - price[l] for l in range(i)))
```
Optimized with a **holding state**:
```
max_buy = max(max_buy, dp[i-1][j-1] - price[i])
dp[i][j] = max(dp[i-1][j], price[i] + max_buy)
```

**🔹 Complexity:** \(O(nk)\), uses 2D DP.

---

### **5. Problem #309: Best Time to Buy and Sell Stock with Cooldown**
**🔹 Difficulty:** Medium  
**🔹 Constraints:** **Cooldown of 1 day** after selling.  
**🔹 Approach:**  
- Introduces a new **cooldown state**.  
- Three states:
  - `hold`: Max profit if holding stock.
  - `sold`: Max profit if just sold.
  - `rest`: Max profit if in cooldown.

**🔹 State Transition:**  
```
hold[i] = max(hold[i-1], rest[i-1] - price[i])
sold[i] = hold[i-1] + price[i]
rest[i] = max(rest[i-1], sold[i-1])
```

**🔹 Complexity:** \(O(n)\), uses three states.

---

### **6. Problem #714: Best Time to Buy and Sell Stock with Transaction Fee**
**🔹 Difficulty:** Medium  
**🔹 Constraints:** Each transaction **costs a fixed fee**.  
**🔹 Approach:**  
- Modify the `sell` transition to subtract the transaction fee.  
- Two states:
  - `hold`: Holding stock.
  - `cash`: Not holding stock.

**🔹 State Transition:**  
```
hold[i] = max(hold[i-1], cash[i-1] - price[i])
cash[i] = max(cash[i-1], hold[i-1] + price[i] - fee)
```

**🔹 Complexity:** \(O(n)\).

---

### **Summary of How Complexity Increases**

| Problem | Transactions | Constraints | Complexity | Key States |
|---------|-------------|-------------|------------|------------|
| **121** | 1 | None | \(O(n)\) | `min_price`, `max_profit` |
| **122** | ∞ | None | \(O(n)\) | `dp[i][0]`, `dp[i][1]` |
| **123** | 2 | None | \(O(n)\) | `firstBuy`, `firstSell`, `secondBuy`, `secondSell` |
| **188** | k | None | \(O(nk)\) | `dp[i][j]`, `max_buy` |
| **309** | ∞ | Cooldown | \(O(n)\) | `hold`, `sold`, `rest` |
| **714** | ∞ | Fee per transaction | \(O(n)\) | `hold`, `cash` |

Each variation introduces new **state dependencies**, requiring more advanced DP transitions. The key to solving them is understanding how each constraint affects transaction choices and how states interact.
