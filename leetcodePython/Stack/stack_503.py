from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        greater = [-1] * len(nums)
        decreaseNumIndex = []
        for i in range(len(nums)*2):
            index = i % len(nums)
            while decreaseNumIndex and nums[index] > nums[decreaseNumIndex[-1]]:
                greater[decreaseNumIndex.pop()] = nums[index]
            decreaseNumIndex.append(index)
        return greater

#-------------------------------------------------- extend the array trick
#                                                   less prone to indx error,
#                                                   same runtime, bad memory
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Input: nums = [1,2,1]
        # Output: [2,-1,2]
        
        # next greater of 1 is 2
        # next greater of 2 is -1
        # next greater of 1 is 2 circular wrap to the left

        # circular uses mod op
        # only search to the right and wrap, not left search

        # OR simpler way is to extend nums to the right to simulate wrapped numbers

        # this contains duplicate numbers unlike L496, index is necessary

        extended_nums = nums + nums[:-1]

        greaters = [-1] * len(extended_nums)
        decreStk = []
        print(extended_nums)
        for i in range(len(extended_nums)):

            while decreStk and extended_nums[decreStk[-1]] < extended_nums[i]:
                prev_idx = decreStk.pop()
                greaters[prev_idx] = extended_nums[i]
            decreStk.append(i)

        return greaters[:len(nums)]   