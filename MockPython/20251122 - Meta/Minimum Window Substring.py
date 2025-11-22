#https://leetcode.com/problems/minimum-window-substring/description/

from common_types import *

"""
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.


1. char in t in substring s
2. shortest sub,
 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCharFreq = Counter(t)
        subSCharFreq = Counter()
        matchedFreqCount = 0
        left = 0
        result = None
        # extend rightmost letter per run
        for right in range(len(s)):
            newCh = s[right]
            subSCharFreq[newCh] += 1
            
            # set of appearance
            if newCh in tCharFreq and subSCharFreq[newCh] == tCharFreq[newCh]:
                matchedFreqCount += 1

            # excluding leftmost unneeded letters
            while left < right and subSCharFreq[s[left]] > tCharFreq[s[left]]:
                subSCharFreq[s[left]] -= 1
                left += 1

            # while finish we get current min length
            if matchedFreqCount == len(tCharFreq):
                if not result or len(result) > right - left + 1:
                    result = s[left:right+1]

        return "" if not result else result