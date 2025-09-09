#https://leetcode.com/problems/coin-change/description/
from common_types import *

"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.


Input: coins = [1,2,5], amount = 11

Output: 3
Explanation: 11 = 5 + 5 + 1



Input: coins = [2], amount = 3
Output: -1

coins: [y1, y2, y3]

minCoinsToValue = [float('inf")] * (amount + 1)

minCoinsToValue[0] = 0

if amount == 0:
    return 0

take min:

100000

[100]

1 -> 100000

for x in range(amount+1):
if x >= y1
    minCoinsToValue[x] = min(minCoinsToValue[x], minCoinsToValue[x-y1] + 1)
if x >= y2
    minCoinsToValue[x] = min(minCoinsToValue[x], minCoinsToValue[x-y2] + 1)
if x >= y3
    minCoinsToValue[x] = min(minCoinsToValue[x], minCoinsToValue[x-y3] + 1)

if minCoinsToValue[-1] == float('inf')
    return -1

return minCoinsToValue[-1]

"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> float:
        if amount == 0:
            return 0
        minCoinsToValue = [float('inf')] * (amount + 1)
        minCoinsToValue[0] = 0
        for currValue in range(1, amount + 1):
            for coinValue in coins:
                if currValue < coinValue:
                    continue
                minCoinsToValue[currValue] = min(minCoinsToValue[currValue], minCoinsToValue[currValue - coinValue] + 1)
        if minCoinsToValue[-1] == float('inf'):
            return -1
        return minCoinsToValue[-1]



class SolutionTopDown:
    def _minCoinsToValue(self, coins, amount, minCoinsToValue) -> float:
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        if minCoinsToValue[amount] != -1:
            return minCoinsToValue[amount]
        currMinCoins = float('inf')
        for coinValue in coins:
            currMinCoins = min(currMinCoins, self._minCoinsToValue(coins, amount - coinValue, minCoinsToValue) + 1)
        minCoinsToValue[amount] = currMinCoins
        return minCoinsToValue[amount]

    def coinChange(self, coins: List[int], amount: int) -> float:
        minCoinsToValue = [-1] * (amount + 1)
        minCoins = self._minCoinsToValue(coins, amount, minCoinsToValue)
        if minCoins == float('inf'):
            return -1
        return minCoins