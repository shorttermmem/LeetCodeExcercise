from typing import List

#https://leetcode.com/problems/largest-rectangle-in-histogram/description/
# 84. Largest Rectangle in Histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        increaseHeightIndex = [-1]
        maxArea = 0
        heights.append(0)
        for i in range(len(heights)):                          # 0, 1, 2, 3, 4, 5
            newHeight = heights[i]                             # [2,1,5,6,2,3]
            while increaseHeightIndex[-1] != -1:               # 
                maxHeight = heights[increaseHeightIndex[-1]]   # 
                if newHeight > maxHeight:                      # 
                    break
                increaseHeightIndex.pop()                      # 
                smallerHeightIndex = increaseHeightIndex[-1]   #  
                width = i - smallerHeightIndex - 1             #  
                maxArea = max(maxArea, maxHeight * width)      # 
            increaseHeightIndex.append(i)                      #
        #heights.pop() not needed
        return maxArea
    
    # Cleaner solution
    def largest_rectangle_area(heights: List[int]) -> int:
        # Use a monotonic stack to track bars in increasing height order
        stack = [-1]  # Sentinel to handle left boundary for the first element
        max_area = 0
        heights.append(0)  # Add dummy height to force final cleanup
        
        for current_idx in range(len(heights)):
            current_height = heights[current_idx]
            
            # Pop taller bars from stack while current bar is shorter
            while stack[-1] != -1 and current_height < heights[stack[-1]]:
                # Calculate area for the popped bar (height * width)
                popped_index = stack.pop()
                height = heights[popped_index]               ##
                
                left_bound_idx = stack[-1]  # First smaller bar to the left
                right_bound_idx = current_idx  # First smaller bar to the right
                width = right_bound_idx - left_bound_idx - 1 ##
                
                max_area = max(max_area, height * width)     ##
            
            # Current bar is taller than stack top - maintain increasing order
            stack.append(current_idx)
        
        heights.pop()  # Remove the dummy height we added
        return max_area

"""
[Brute Force]
for each possible pair of i and j, compute the min in that range and calculate the area. But that's O(n^3) time, which is way too slow for n up to 1e5. 

[Monotonic Stack]
Key Insight:
1, Push bar index to the stack if the height is increasing. 
    ( calculate the area for the popped bar using the current index (i) as the right_bound and the new top of the stack as the left_bound.)
2, Equal Heights Are Included in the Width
3, Each bar is pushed and popped once → O(n) operations.
4, No redundant comparisons: Boundaries are resolved in a single pass.

Algorithm:
1, Initialize a stack with a single sentinel index -1.
2, Iterate through the heights array, adding each index to the stack.
3, While the current height is less than the previous height, pop the stack and calculate the area.
4, The width is the difference between the current index and the new top of the stack.
5, Update the maximum area and continue until the stack is empty.
6, Return the maximum area.

Indices: -1 (sentinel) | 0 (2) | 1 (1) | 2 (5) | 3 (6) | 4 (2) | 5 (3)
Stack State: [-1]    → [-1,0] → [-1,1] → [-1,1,2] → [-1,1,2,3] → ...  

------------------------------------------------------------------
When to Avoid
Non-Order-Based Problems: If the problem doesn’t involve relationships based on element order (e.g., frequency counts).
Dynamic Programming Scenarios: Some problems might be better solved with DP (e.g., longest increasing subsequence).

"""