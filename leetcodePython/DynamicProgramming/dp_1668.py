#https://leetcode.com/problems/maximum-repeating-substring/description/

# Example 1:
# Input: sequence = "ababc", word = "ab"
# Output: 2
# Explanation: "abab" is a substring in the sequence. 
#              basically asking how many times we can repeat the word in the sequence
    
class Solution:
    # top down with memoization
    def maxRepeating(self, sequence: str, word:str) -> int:
        
        n, m = len(sequence), len(word)
        
        if m == 0 or n < m:
            return 0
        
        memo = {}
        def dfs(i, memo):
            # ababc ab
            # 01234 
            #    i=3 > 5-2=3
            if i > n - m:  # Base case: can't fit `word` anymore
                return 0
            
            if i in memo:
                return memo[i]
            
            ###############################################################
            """ Wrong implementation, returns all the possible values which is 6
            if sequence[i:i + m] == word:
                memo[i] = 1 + dfs(i + m, memo)  # Move forward by word length
                return memo[i]
            
            return dfs(i + 1, memo)  # Move forward one step
            """
            ###############################################################
            if sequence[i:i + m] == word:
                memo[i] = 1 + dfs(i + m, memo)  # Move forward by word length
            else:
                memo[i] = 0
            
            return memo[i] 
            ###############################################################
        
        for i in range(n):
            dfs(i, memo)
            
        return max(memo.values()) 
        
    # bottom up with tabulation
    def maxRepeating2(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)
        dp = [0] * (n + 1)

        # Iterate over the sequence, starting from the word's length
        for i in range(m, n + 1):
            # Check if the substring of length m starting from index i is equal to the word
            if sequence[i-m:i] == word:
                dp[i] = dp[i - m] + 1

        # Return the maximum dp value, which represents the maximum number of times the word can be repeated
        return max(dp)

#------------------ test -------------------
s = Solution()
print(s.maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba"))
print(s.maxRepeating2("ababc", "ab"))