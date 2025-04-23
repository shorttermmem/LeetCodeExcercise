#https://leetcode.com/problems/palindrome-partitioning/description/
#Return all possible palindrome partitioning of s.
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(s):
            return s == s[::-1]
        
        def backtrack(start, curr):

            if start == len(s):
                res.append(curr[:])
                return
            for end in range(start + 1, len(s) + 1):
                if isPalindrome(s[start:end]):
                    curr.append(s[start:end])
                    backtrack(end, curr)
                    curr.pop()
        res = []
        backtrack(0, [])
        return res