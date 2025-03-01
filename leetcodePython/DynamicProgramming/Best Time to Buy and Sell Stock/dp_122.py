#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# infinite transactions

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
                
        return max_profit
    
    def maxProfit2(self, prices: List[int]) -> int:
        # bottom-up approach
        if len(prices) <= 1:
            return 0
        # dp[i][0] = max profit on day i with no stock in hand
        # dp[i][1] = max profit on day i with stock in hand
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        
        # base case
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            
        return dp[-1][0]
    
    def maxProfit3(self, prices: List[int]) -> int:
        # top-down approach
        def _recur(prices, i, stock_in_hand, memo):
            if i >= len(prices):
                return 0
            
            if (i, stock_in_hand) in memo:
                return memo[(i, stock_in_hand)]
            
            if stock_in_hand:
                memo[(i, stock_in_hand)] = max(_recur(prices, i+1, 0, memo) + prices[i], _recur(prices, i+1, stock_in_hand, memo))
            else:
                memo[(i, stock_in_hand)] = max(_recur(prices, i+1, 1, memo) - prices[i], _recur(prices, i+1, stock_in_hand, memo))
            
            return memo[(i, stock_in_hand)]
        
        return _recur(prices, 0, 0, {})