#https://leetcode.com/problems/longest-palindromic-substring/description/
from common_types import *

"""
Given a string s, return the longest palindromic substring in s.



"""

class Solution:
    # 0 1
    # 
    def _expandFromCenter(self, left, right, s: str) -> tuple[int, int]:

        if left != right:
            if s[left] != s[right]:
                return 

        while left >=0 and right < len(s):
            if s[left-1] != s[right+1]:
                break
            left -= 1
            right += 1
    
    
        left = left + 1
        return left, right

    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        subStr = ""
        for i in range(len(s)):
            left1, right1 = self._expandFromCenter(i, i, s)
            length1 = right1 - left1 + 1
            if maxLength < length1:
                subStr = s[left1:right1+1]
            left2, right2 = self._expandFromCenter(i, i+1, s)
            length2 = right2 - left2 + 1
            if maxLength < length2:
                subStr = s[left2:right2+1]
        return subStr