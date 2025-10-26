#https://leetcode.com/problems/fruit-into-baskets/description/

from common_types import *

"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. 
The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. 

However, the owner has some strict rules that you must follow:

* You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
* Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. 
The picked fruits must fit in one of your baskets.

Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

pick from 0, types 1, pick from 1,  then types 2
try pick 2, type 3 > limit 2

Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
 

Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length


fruitsOfType[type] 
"""
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitsOfType = defaultdict(int)
        left = 0
        totalFruits = 0
        for right in range(len(fruits)):
            currentType = fruits[right]
            fruitsOfType[currentType] += 1
            while len(fruitsOfType) > 2:
                prevType = fruits[left]
                fruitsOfType[prevType] -= 1
                if fruitsOfType[prevType] == 0:
                    del fruitsOfType[prevType]
                left += 1
            totalFruits = max(totalFruits, right - left + 1)
        return totalFruits


    def totalFruitOpt(self, fruits: List[int]) -> int:
        fruitsOfType = defaultdict(int)
        left = 0
        right = 0
        for right in range(len(fruits)):
            currentType = fruits[right]
            fruitsOfType[currentType] += 1
            if len(fruitsOfType) > 2:
                prevType = fruits[left]
                fruitsOfType[prevType] -= 1
                if fruitsOfType[prevType] == 0:
                    del fruitsOfType[prevType]
                left += 1
        return right - left + 1

















