# copy the trienode from the implement trienode problem 
class TrieNode:
    def __init__(self):
        self.children = {} 
        self.end = False
    
    def insert(self, word: str) -> None:
        # traverse the trie similar to linked list 
        cur = self 
        for char in word: 
            if char not in cur.children: 
                cur.children[char] = TrieNode() 
            # navigate to next level 
            cur = cur.children[char] 
        
        # for the last char, mark end 
        cur.end = True

class Solution:
    """ 
    First add all words into a trie 
    The DFS function here builds from an empty string, and find words from a starting position
    that match the structure of the trie
    Early prune if the current position not in the trie (if board[i][j] not in trie.children). 

    Then we can try dfs from each starting position (i,j) and return all words that can be found
    """ 
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode() 
        # Insert all words from the list of words into the trie 
        for word in words: 
            trie.insert(word) 

        ROWS, COLS = len(board), len(board[0])
        visited = set() 
        ans = [] 

        # compared to word search I, also pass in the current trie node 
        def dfs(i,j,word,node): 
            if (i,j) in visited or board[i][j] not in node.children: 
                return False 
            
            # dfs its possible neighbours 
            visited.add((i,j)) 

            # navigate trie to the next level 
            node = node.children[board[i][j]]
            word += board[i][j]

            if node.end: 
                ans.append(word)

            nei = [] 
            if i > 0:
                nei.append((i-1, j)) 
            if j < COLS-1: 
                nei.append((i, j+1)) 
            if i < ROWS-1:
                nei.append((i+1, j)) 
            if j > 0:
                nei.append((i, j-1)) 
            
            for a,b in nei: 
                if dfs(a,b,word,node): 
                    return True 
            
            visited.remove((i,j))
            return False 
        

        for i in range(ROWS): 
            for j in range(COLS): 
                dfs(i,j,"",trie)
        
        return list(set(ans)) 

