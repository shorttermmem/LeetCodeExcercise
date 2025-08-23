#https://leetcode.com/problems/decode-ways/
from common_types import *

"""
Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        return 0