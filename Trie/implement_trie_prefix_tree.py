"""
Main point is the trie node: an array for 26 alphabet children and a flag to mark if the word ends there.
Then, just traverse the trie like how you traverse a linked list using cur pointer 
"""
class TrieNode:
    def __init__(self):
        self.children = [None]*26  # store all child in an array 
        self.end = False  # used for search function to find exact word 

class Trie:
    def __init__(self):
        self.root = TrieNode() 

    def insert(self, word: str) -> None:
        # traverse the trie similar to linked list 
        cur = self.root 
        for char in word: 
            index = ord(char) - ord('a')
            if not cur.children[index]: 
                cur.children[index] = TrieNode() 
            cur = cur.children[index] 
        
        # for the last char, mark end 
        cur.end = True

    def search(self, word: str) -> bool:
        # traverse the trie 
        cur = self.root 
        for char in word: 
            index = ord(char) - ord('a')
            if not cur.children[index]: 
                return False 
            cur = cur.children[index] 
        
        # The last node has to mark as end 
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        # traverse the trie 
        cur = self.root 
        for char in prefix: 
            index = ord(char) - ord('a')
            if not cur.children[index]: 
                return False 
            cur = cur.children[index] 
        
        # This does not require the last node to be marked as end. 
        return True 


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)