#https://leetcode.com/problems/implement-trie-prefix-tree/description/
"""
 A trie is a tree where each node represents a single character of a string.
 The root node is typically empty (doesn’t represent any character).
"""
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
class Trie:
    class Node:
        def __init__(self):
            # Stores children nodes and whether node is the end of a word
            self.nextchars = {}
            self.isWord = False

    def __init__(self):
        self.root = Trie.Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.nextchars:
                curr.nextchars[c] = Trie.Node()
            curr = curr.nextchars[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.nextchars:
                return False
            curr = curr.nextchars[c]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.nextchars:
                return False
            curr = curr.nextchars[c]
        return True

class Trie_nested_dict: # better memory
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur:
                cur[letter] = {} # nested dictionary, not Trie Node
            cur = cur[letter]
        cur['*'] = None # dic with '*' marks as is a Word

    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            if letter not in cur:
                return False
            cur = cur[letter]
        return '*' in cur        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            if letter not in cur:
                return False
            cur = cur[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)