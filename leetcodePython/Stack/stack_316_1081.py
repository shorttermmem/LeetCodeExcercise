class Solution316:
    def removeDuplicateLetters(self, s: str) -> str:
        increaseChars = []
        seen = set()
        lastIndexOfCh = {}

        # store the last index of each character s = "bcabc"
        for i, c in enumerate(s):
            lastIndexOfCh[c] = i # {'b': 3, 'c': 4, 'a': 2}

        for i in range(len(s)):
            # using a set to track visited characters is unique.
            if s[i] not in seen:
                # if the current character is smaller than the last character in the stack
                while increaseChars and s[i] < increaseChars[-1] and i < lastIndexOfCh[increaseChars[-1]]: #
                    seen.discard(increaseChars.pop())
                seen.add(s[i])
                increaseChars.append(s[i])
        return ''.join(increaseChars)


class Solution1081:
    def smallestSubsequence(self, s: str) -> str:
        increaseChars = []
        seen = set()
        lastIndexOfCh = {}

        for i, c in enumerate(s):
            lastIndexOfCh[c] = i

        for i in range(len(s)):
            if s[i] not in seen:
                while increaseChars and s[i] < increaseChars[-1] and i < lastIndexOfCh[increaseChars[-1]]:
                    seen.discard(increaseChars.pop())
                seen.add(s[i])
                increaseChars.append(s[i])
        return ''.join(increaseChars)
