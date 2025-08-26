class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        use the sorted string as keys. 
        ( When comparing whether two strings are anagrams, use sorted(a) == sorted(b). )
        """
        d = defaultdict(list) 

        for s in strs: 
            d[''.join(sorted(s))].append(s) 
        
        ans = [] 
        for v in d.values(): 
            ans.append(v) 
        
        return ans 