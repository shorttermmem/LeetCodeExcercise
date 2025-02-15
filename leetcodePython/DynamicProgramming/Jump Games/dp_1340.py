#https://leetcode.com/problems/jump-game-v/description/
# longest steps to descent per d steps 
# Example 1:
# Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
# Output: 4
# Explanation: You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.

class Solution:
    # DP - Bottom Up with memoization
    def maxJumps(self, arr: List[int], d: int) -> int:
        def _dfs(i, memo):
            if i in memo:
                return memo[i]
            
            max_jumps = 1
            
            # Move Left
            for j in range(i - 1, max(i - d - 1, -1), -1):  # Move leftward
                if arr[j] >= arr[i]:  
                    break  # Stop when encountering a taller or equal height
                max_jumps = max(max_jumps, 1 + _dfs(j, memo))

            # Move Right
            for j in range(i + 1, min(i + d + 1, len(arr))):  # Move rightward
                if arr[j] >= arr[i]:  
                    break  # Stop when encountering a taller or equal height
                max_jumps = max(max_jumps, 1 + _dfs(j, memo))
            
            memo[i] = max_jumps
            return max_jumps
        
        memo = {}
        return max(_dfs(i, memo) for i in range(len(arr)))  # Compute max for all starting indices
    
    # Top Down DP with tabulation
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1] * n  # Base case: Each index can at least stay in place

        # Sort indices by height (smallest to largest)
        indices = sorted(range(n), key=lambda i: arr[i])

        for i in indices:
            # Check Left
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= arr[i]:  # Stop when encountering a taller or equal height
                    break
                dp[i] = max(dp[i], dp[j] + 1)

            # Check Right
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:  # Stop when encountering a taller or equal height
                    break
                dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)  # Get the max jumps possible