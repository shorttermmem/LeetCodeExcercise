# You are given two strings, s and t.
# You can create a new string by selecting a substring from s (possibly empty) and a substring from t (possibly empty), then concatenating them in order.
# Return the length of the longest palindrome that can be formed this way.

class Solution:
#https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/description/
    # 1 <= s.length, t.length <= 30
    def longestPalindrome_slow(self, s: str, t: str) -> int:
        
        def isPalindrome(string: str) -> bool:
            left, right = 0, len(string) - 1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        max_length = 0
        n, m = len(s), len(t)
        
        # iterate over all start indices of s
        for i in range(n + 1):  # Include empty substring
            # iterate over all end indices of s
            for j in range(i, n + 1):
                s_sub = s[i:j] if i < j else ""
                # iterate over all start indices of t
                for p in range(m + 1):
                    # iterate over all end indices of t
                    for q in range(p, m + 1):
                        t_sub = t[p:q] if p < q else ""
                        # Concatenate and check palindrome
                        concat = s_sub + t_sub
                        if isPalindrome(concat):
                            max_length = max(max_length, len(concat))
        
        return max_length
    

    def longestPalindrome_fast(self, s: str, t: str) -> int:
        def manacher(s: str) -> list:
            """Manacher's algorithm to return longest palindromic substring length starting at each index."""
            ss = "#" + "#".join(s) + "#"
            n = len(ss)
            hlen = [0] * n
            # center = i, rightmost palindrome end = right
            center = right = 0
            for i in range(n):
                if i < right:
                    # Use mirror palindrome length if within current palindrome
                    # hlen[2 * center - i] is the mirror of i
                    # right - i is the distance from i to rightmost palindrome end
                    hlen[i] = min(right - i, hlen[2 * center - i])
                # Expand palindrome at i
                # i - hlen[i] is the start of the palindrome
                # i + hlen[i] is the end of the palindrome
                # ss[i - 1 - hlen[i]] == ss[i + 1 + hlen[i]] is the condition for expanding the palindrome
                while 0 <= i - 1 - hlen[i] and i + 1 + hlen[i] < n and ss[i - 1 - hlen[i]] == ss[i + 1 + hlen[i]]:
                    hlen[i] += 1
                # Update center and rightmost palindrome end if needed
                if right < i + hlen[i]:
                    # Update center to current i
                    # Update right to i + hlen[i]
                    center, right = i, i + hlen[i]
            ans = [0] * len(s)
            # Convert to palindrome lengths starting at each index
            for i, x in enumerate(hlen):
                # x is the half length of the palindrome centered at i
                # i - x is the start of the palindrome
                # i + x is the end of the palindrome
                if (i - x) // 2 < len(s):
                    ans[(i - x) // 2] = x
            return ans
        
        # Compute longest palindrome lengths
        sloc = manacher(s)              # Longest palindrome starting at s[i]
        tloc = manacher(t[::-1])[::-1]  # Longest palindrome ending at t[j]
        
        # Initialize result with single-string palindromes
        ans = max(max(sloc, default=0), max(tloc, default=0))
        
        # DP table: dp[i][j] = longest palindrome using s[0:i+1] and t[j:n]
        m, n = len(s), len(t)
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    # Form palindrome with s[i] and t[j]
                    if i > 0 and j + 1 < n and dp[i - 1][j + 1]:
                        dp[i][j] = 2 + dp[i - 1][j + 1]
                    else:
                        dp[i][j] = 2
                # Consider additional palindrome from s[i+1:] or t[:j]
                extra = 0
                if i + 1 < m:
                    extra = max(extra, sloc[i + 1])
                if j > 0:
                    extra = max(extra, tloc[j - 1])
                ans = max(ans, dp[i][j] + extra)
        
        return ans