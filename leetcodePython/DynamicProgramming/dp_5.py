#https://leetcode.com/problems/longest-palindromic-substring/description/
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

    # Input: s = "babad"
    # Output: "bab"

    #   j 0 1 2 3 4
    # i   b a b a d
    # 0 b 1 0 1 0 0      
    # 1 a   1 0 1 0 
    # 2 b     1 0 0 
    # 3 a       1 0 
    # 4 d         1 
    
class solution:

    # bottom-up approach with tabulation
    def longestPalindrome(s: str) -> str:
        if not s:
            return ""
        
        # dp[i][j] will be true if the substring s[i...j] is a palindrome.
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        start, max_length = 0, 1
        
        # Base case: single letter palindromes
        for i in range(n):
            dp[i][i] = 1
        
        # Base case: double letter palindromes
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                start = i
                max_length = 2
                break
        
        # The rest of the cases: length 3 to n
        for length in range(3, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                # inner s[l+1 ... r-1]
                # outter s[l ... r]
                # dp[l + 1][r - 1] is true if the substring s[l+1...r-1] is a palindrome
                if s[l] == s[r] and dp[l + 1][r - 1]:
                    dp[l][r] = 1
                    start = l
                    max_length = length
        
        return s[start:start + max_length]
              
    # top-down approach with memoization
    def longestPalindrome(s: str) -> str:

        def _isParlindrom(s, l, r, memo) -> str:
            if (l, r) in memo:
                return memo[(l, r)]    # use tuple as key, similar to dp[i][j]
            
            if l > r:
                return ""
            if l == r:
                return s[l]
            
            if s[l] == s[r]:
                inner = _isParlindrom(l + 1, r - 1, memo)
                # if inner is a palindrome, 
                # then s[l] + inner + s[r] is a palindrome
                if len(inner) == (r - l - 1):
                    memo[(l, r)] = s[l] + inner + s[r]
                    return memo[(l, r)]
            
            left_sub = _isParlindrom(l + 1, r, memo)
            right_sub = _isParlindrom(l, r - 1, memo)
            
            memo[(l, r)] = max(left_sub, right_sub, key=len)
            return memo[(l, r)]
        
        return _isParlindrom(0, len(s) - 1, {})
