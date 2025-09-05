# copy the trienode from the implement trienode problem 
class TrieNode:
    def __init__(self):
        self.children = {} 
        self.end = False  # used for search function to find exact word 

class WordDictionary:
    """ 
    Compared to the trie in the previous question, this uses a dictionary (as we need to iterate each valid char later) 

    when searching, navigate to the next level (using linked-list like way of navigating) 
    and when encountered a . call the helper function that also takes in the root to search from, 
    return True if any paths return True (DFS). 

    one take btw :) 
    """ 

    def __init__(self):
        self.root = TrieNode() 

    def addWord(self, word: str) -> None:
        # traverse the trie in a linked list manner 
        cur = self.root 
        for c in word: 
            if c not in cur.children: 
                cur.children[c] = TrieNode() 
            cur = cur.children[c] 
        
        # at the end, mark cur as ended 
        cur.end = True 

    def search(self, word: str) -> bool:

        # helper function that also take in the root to be searched from 
        def helper(word, root): 
            cur = root
            
            for i in range(len(word)): 
                c = word[i] 

                if c != '.': 
                    if c not in cur.children: 
                        return False 
                    
                    cur = cur.children[c]

                else: 
                    for key, value in cur.children.items(): 
                        if helper(word[i+1::], value): 
                            return True 
                    
                    return False 
            
            return cur.end
        
        return helper(word, self.root)
            

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)