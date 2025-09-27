#https://leetcode.com/problems/stone-game/
from common_types import *

"""
Alice and Bob play a game with piles of stones. 

There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. 
The total number of stones across all the piles is odd, so there are no ties.

Alice and Bob take turns, with Alice starting first. 

Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. 

This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

 

Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.

A 5 B 5, A 4, B 3



Example 2:

Input: piles = [3,7,2,3]
Output: true

A3, B3, A7, B2 

alicePickAt[left] = bobPickAt[left - 1]
alicePickAt[right] = bobPickAt[left - 1]

@cache
def pick(left, right, isPlus):
if left > right:
    return 0

maxRelativeScore
if isPlus:
    maxRelativeScore = max(maxRelativeScore, pick(left+1, right, !isPlus) + pile[left])
    maxRelativeScore = max(maxRelativeScore, pick(left, right-1, !isPlus) + pile[right])
else:
    maxRelativeScore = max(maxRelativeScore, pick(left+1, right, !isPlus) - pile[left])
    maxRelativeScore = max(maxRelativeScore, pick(left, right-1, !isPlus) - pile[right])

return maxRelativeScore


relativeScore = pick(0, len(piles)-1, true)

return relativeScore > 0
    
pile[left] + pick()

bobPickAt[]

Constraints:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles[i]) is odd.



"""
from functools import *

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @cache
        def pick(left, right, isPlus: bool) -> int:
            if left > right:
                return 0
            maxRelativeScore = 0                
            if isPlus:
                maxRelativeScore = max(maxRelativeScore, pick(left+1, right, not isPlus) + piles[left])
                maxRelativeScore = max(maxRelativeScore, pick(left, right-1, not isPlus) + piles[right])
            else:
                maxRelativeScore = max(maxRelativeScore, pick(left+1, right, not isPlus) - piles[left])
                maxRelativeScore = max(maxRelativeScore, pick(left, right-1, not isPlus) - piles[right])

            return maxRelativeScore

        relativeScore = pick(0, len(piles)-1, True)

        return relativeScore > 0
    

        def pick(l, r) -> int:
            if (l, r) in cache:
                return cache[(l, r)]
            if l > r:
                return 0
            if l == r:
                return piles[l]
            
            """ 
            assume current player is player 1, then if player 1 chooses piles[l], 
            self.helper(piles, l + 1, r, cache) will return the maximum stones player 2 
            can get more than player 1 from the rest (piles[l + 1] ... piles[r]), then
            by subtracting it from piles[l], we get how many stones player 1 can get
            more than player 2. Since we want to maximize final result, we choose the
            max of both options player 1 can make (pick piles[l] or piles[r])
            """
            res = max(piles[l] - pick(piles, l + 1, r, cache), piles[r] - pick(piles, l, r - 1, cache))
            cache[(l, r)] = res
            return res
    

class SolutionBottomUp:
    def stoneGame(self, piles: List[int]) -> bool:
        # 2Players, 1Action -> 1D

        # 2D
        n = len(piles)
        dp = [[0] * n for i in range(n)]
        for i in range(n): dp[i][i] = piles[i]

        for d in range(1, n):
            for l in range(n - d):
                r = l + d
                dp[l][r] = max(piles[l] - dp[l + 1][r], piles[r] - dp[l][r - 1])
        #return dp[0][-1] > 0
        

        # 1D
        n = len(piles)
        dp = piles[:]
        for d in range(1, n):
            for l in range(n - d):
                r = l + d
                dp[l] = max(piles[l] - dp[l + 1], piles[r] - dp[l])
        return dp[0] > 0





























    