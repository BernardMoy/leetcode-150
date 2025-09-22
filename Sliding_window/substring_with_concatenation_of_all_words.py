class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        Brute force

        Maintain a sliding window of length Ntotal (total length of each word concatenated)
        As each word is of the same size. 

        use Counter(a) == Counter(b) to check if a substring (window) is a permutation of the words array. 
        """ 

        c = Counter(words) 
        N = len(words[0])       # length of each word 
        Ntotal = len(words)*N   # total length of all words

        ans = [] 

        for start in range(0, len(s)-Ntotal+1): 
            cur = [] 
            for i in range(start, start+Ntotal, N): 
                cur.append(s[i:i+N])
            
            if Counter(cur) == c: 
                ans.append(start)
        
        return ans 