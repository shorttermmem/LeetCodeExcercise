from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        decreaseTempIndex = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while decreaseTempIndex and temperatures[i] > temperatures[decreaseTempIndex[-1]]:
                smallTempIndex = decreaseTempIndex.pop()
                answer[smallTempIndex] = i - smallTempIndex
            decreaseTempIndex.append(i)
        return answer

    # My one time solution
    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        
        # Use a monotonic stack to track bars in decreasing temperature order
        decStack = []
        
        # default to zero days for higher temperatures if not found according to question
        ans = [0] * len(temperatures)

        for curr_idx in range(len(temperatures)):
            curr_temp = temperatures[curr_idx]

            # Pop lower temperatures while curr temp is higher
            while decStack and curr_temp > temperatures[decStack[-1]]:
                
                popped_idx = decStack.pop()

                number_of_days_till_higher = curr_idx - popped_idx 

                # popped_idx is the index of the lower temperature that is looking for the next higher temperature
                ans[popped_idx] = number_of_days_till_higher
            
            # curr temp is lower than stack top - maintain decreasing order
            decStack.append(curr_idx)
        
        return ans
