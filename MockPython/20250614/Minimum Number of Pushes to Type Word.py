from common_types import *

class Solution:
    # https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/description/
    """
    Word contains distinct letters
    1 <= word.length <= 26
    word consists of lowercase English letters.
    All letters in word are distinct.
    """
    def minimumPushes(self, word: str) -> int:
        layers = len(word) // 8
        remain = len(word) % 8
        pushes = (1 + layers) * layers // 2 * 8
        pushes += (layers + 1) * remain
        return pushes
    

    #https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/
    """
    Word contains duplicate letters
    1 <= word.length <= 105
    word consists of lowercase English letters.
    """
    def minimumPushesII(self, word: str) -> int:
        freqOf = Counter(word)
        sortedFreq = freqOf.most_common()
        layer = 1
        pushes = 0
        for layer in range(0, len(sortedFreq), 8):
            pushes += sum([freq for _, freq in sortedFreq[layer*8:layer*8+8]]) * (layer + 1) * 8

        
        return pushes
    
        #--------------------------------------------------
        # Count frequencies and sort in descending order
        counts = sorted(Counter(word).values(), reverse=True)
        
        # Calculate total presses: first 8 letters use 1 press, next 8 use 2, etc.
        return sum((i // 8 + 1) * count for i, count in enumerate(counts))