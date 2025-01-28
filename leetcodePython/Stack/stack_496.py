from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greaterMap = {}
        decreaseStack = []
        
        # first exmaple that we dont need to use index of the array
        for num in nums2:
            while decreaseStack and num > decreaseStack[-1]:
                prevNum = decreaseStack.pop()
                greaterMap[prevNum] = num
            decreaseStack.append(num)
        answer = []

        # use greaterMap to get the answer, good name for clarity
        for num in nums1:
            if num in greaterMap:
                answer.append(greaterMap[num])
            else:
                answer.append(-1)
        return answer


#-------------------------------------------------- with example
    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
        # Output: [-1,3,-1]

        # no bigger to the right of 4, -1
        # bigger to the right of 1, 3
        # no bigger to the right of 2, -1

        decreStk = []
        greaterMap = {}
        res = []

        for n in nums2:
            
            # bigger than top of stk
            while decreStk and decreStk[-1] < n: # [3, ]
                prevNum = decreStk.pop()
                greaterMap[prevNum] = n
            decreStk.append(n)                   # [3, ]

        for n in nums1:
            if n in greaterMap:
                res.append(greaterMap[n])
            else:
                res.append(-1)

        return res
        