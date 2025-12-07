#https://leetcode.com/problems/shopping-offers

from common_types import *

"""
In LeetCode Store, there are n items to sell. 
Each item has a price. 
However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.

You are given an integer array price where price[i] is the price of the ith item, 
and an integer array needs where needs[i] is the number of pieces of the ith item you want to buy.

You are also given an array special where special[i] is of size n + 1 
where special[i][j] is the number of pieces of the jth item in the ith offer 
and special[i][n] (i.e., the last integer in the array) is the price of the ith offer.

Return the lowest price you have to pay for exactly certain items as given, 
where you could make optimal use of the special offers. 
You are not allowed to buy more items than you want, even if that would lower the overall price. 
You could use any of the special offers as many times as you want.

 Example 1:

Input: price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
Output: 14
Explanation: There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B. 
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.

[2, 5]

[3, 2]

[[3,0,5],[1,2,10]]

output: 14 => [1, 2, 10] 10$, 

[2, 0] => 2*2 = 4$ sum up to 14$


Example 2:

Input: price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1]
Output: 11
Explanation: The price of A is $2, and $3 for B, $4 for C. 
You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C. 
You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C. 
You cannot add more items, though only $9 for 2A ,2B and 1C.

Binary search answer,
DP
Priorityqueue


Constraints:

n == price.length == needs.length
1 <= n <= 6
0 <= price[i], needs[i] <= 10
1 <= special.length <= 100
special[i].length == n + 1
0 <= special[i][j] <= 50
The input is generated that at least one of special[i][j] is non-zero for 0 <= j <= n - 1.

"""

class Solution:
    def shop(self, )
    def shoppingOffers(self, prices: List[int], special: List[List[int]], needs: List[int]) -> int:
        options = special
        for i in range(len(prices)):
            option = [0] * len(special[0])
            option[i] = 1
            option[-1] = prices[i]


        # get maxCost from price and needs
        maxCost = float('inf') #pseudo 2*3 + 5*2
        #.           [3,2]
        # special = [[3,0,5]
        #            [1,2,10]]

        return 0
    



         
        @lru_cache(None)
        def dfs(needs):

            cost = sum( map(mul, needs, tuple(price)) )

            for sp in special:

                spPrice = sp[-1]
                updated_needs = tuple( map(sub, needs, sp[:-1]) )

                if min(updated_needs) < 0:
                    continue #cannot over buy any item
                
                cost = min( cost, dfs(updated_needs) + spPrice)
            
            return cost

        return dfs(tuple(needs))