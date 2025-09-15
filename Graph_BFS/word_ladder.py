class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """ 
        We need a way to find words that differ from one character: 
        hot -> [dot, lot, hit] 

        One way is to use * to mask the changed position, and use that as the dictionary key
        hot -> [*ot, h*t, ho*]
        *ot maps to [hot, lot, dot], ... etc (iterate all of them) 

        after that we can simply perform a BFS until we find the ans or return 0 at the end. 
        """

        # impossible 
        if endWord not in wordList: 
            return 0 
        
        # adjacency list to stroe words that differ by one character
        # they can be stored with a shared key with *: 
        # dog -> *og, d*g, do* 
        graph = defaultdict(list) 
        wordList.append(beginWord)
        for word in wordList: 
            for i in range(len(word)): 
                pattern = word[:i] + '*' + word[i+1:] 
                graph[pattern].append(word) 
        
        # BFS 
        q = deque([beginWord]) 
        visited = set() 
        ans = 1 
        while q: 
            for _ in range(len(q)): 
                cur = q.popleft() 

                # reached end 
                if cur == endWord: 
                    return ans 
                
                # visited 
                if cur in visited: 
                    continue 

                # iterate the possible masked sequences of cur 
                for i in range(len(cur)): 
                    pattern = cur[:i] + '*' + cur[i+1:] 
                    q.extend(graph[pattern])  # add all words that match the pattern into the queue 
                visited.add(cur) 

            ans += 1 
        
        # sequence not found 
        return 0

