#https://leetcode.com/problems/regular-expression-matching/description/

from common_types import *
import functools

"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".


Input: s = "aa" => p = "a*"
            "a", "aaa", "abcdef"



Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

"" not match ".*" 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

* complicated, it can match any length and character
"""

class Solution:
    # * => "", ".", "..."

    @functools.lru_cache(maxsize=128)
    def isMatch(self, s: str, p: str) -> bool:

        # check s & p is matching
        if not p and not s:
            return True
        if not p and s or not s and p:
            return False

        isFirstMatch = False
        #'.' Matches any single character.​​​​
        # check if curr first char matches
        if p[0] == '.' or s[0] == p[0]:
            isFirstMatch = self.isMatch(s[1:], p[1:])  
        
        #'*' Matches zero or more of the preceding element         
        if p[0] == '*':
            # skip preceeding char + '*' or move on and keep the '*'
            return self.isMatch(s, p[2:]) or (isFirstMatch and self.isMatch(s[1:], p[:]))
        else:
            return isFirstMatch and self.isMatch(s[1:], p[1:])