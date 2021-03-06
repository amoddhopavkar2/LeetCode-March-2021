# Saturday, 6th March 2021
# Short Encoding of Words

class TrieNode:
    def __init__(self):
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ends = []
        
    def insert(self, word):
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        self.ends.append((root, len(word) + 1))
        
        
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie, result = Trie(), 0
        
        for word in set(words):
            trie.insert(word[::-1])
            
        return sum(depth for node, depth in trie.ends if len(node.children) == 0)