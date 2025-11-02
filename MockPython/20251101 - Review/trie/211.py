#https://leetcode.com/problems/design-add-and-search-words-data-structure

from common_types import *

"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 
"ba", "bc", "bd"

"b"
["a", "c", "d"]
......

Constraints:

1 <= word.length <= 25

word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.


"a"
"a,b"

"""

class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        return

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.is_end = True
        return

    def search(self, word: str) -> bool:
       
        def dfs(node, charIndex):
            if charIndex == len(word) - 1:
                return node.is_end
            nextCharIndex = charIndex + 1
            if word[nextCharIndex] == '.':
                for child in node.children.values():
                    if dfs(child, nextCharIndex):
                        return True
                return False
            else:
                if word[nextCharIndex] not in node.children:
                    return False
            return dfs(node.children[word[nextCharIndex]], nextCharIndex)

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)