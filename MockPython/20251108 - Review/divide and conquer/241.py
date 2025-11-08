#https://leetcode.com/problems/different-ways-to-add-parentheses

from common_types import *

"""
Given a string expression of numbers and operators, 
return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 10^4.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10


Constraints:

1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
The integer values in the input expression do not have a leading '-' or '+' denoting the sign.


2*3-4*5

2 * diffWaysToCompute("3-4*5")
2 * 3 - diffWaysToCompute("4*5")


"""

class Solution:

    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        @lru_cache(None)
        def dc(s) -> List[int]:
            if s.isdigit():
                return [int(s)]

            res = []
            for i, c in enumerate(s):
                if c in '-+*':
                    left = dc(s[:i])
                    right = dc(s[i+1:])
                    for leftResult in left:
                        for rightResult in right:
                            res.extend(eval(f"{leftResult}{c}{rightResult}"))
            return res
        return dc(expression)