class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stepLeft = k
        remainDigits = []
        for digit in num:
            while stepLeft and remainDigits and digit < remainDigits[-1]:
                remainDigits.pop()
                stepLeft -= 1
            remainDigits.append(digit)

        if stepLeft > 0:
            remainDigits = remainDigits[:-stepLeft]

        numStr = "".join(remainDigits).lstrip('0')
        return numStr if numStr else "0"


#------------------------------------------------- Cleaner solution
    def removeKdigits2(self, num: str, k: int) -> str:
        # num = "1432219", k = 3
        # keep lexicographically order similar to 316
        increStk = []
        # greedy works 

        for curr in range(len(num)):
            # increStk [1, 4], curr 2, num[curr] 3
            # len(num) 7, curr 2, len(increStk) 2 : 3 > 3
            while increStk and num[curr] < increStk[-1] and k > 0:
                increStk.pop()
                k-=1
            increStk.append(num[curr])

        if k > 0:
            increStk = increStk[:-k]


        res = ''.join(increStk).lstrip('0')
        return res if res else '0'