class Solution:
    def isValid(self, s: str) -> bool:
        openBracketStack = []
        openBracketTypes = {"{", "[", "("}
        bracketMap = {"}": "{", "]": "[", ")": "("}
        for ch in s:
            if ch in openBracketTypes:
                openBracketStack.append(ch)
            elif openBracketStack and bracketMap[ch] == openBracketStack[-1]:
                openBracketStack.pop()
            else:
                return False
        return not openBracketStack


"""_summary_

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

--------------------------------------------------
- Use stack to keep track of open brackets
- Use dictionary to map close bracket to open bracket

"""