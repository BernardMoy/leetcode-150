class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Classic sort first problem
        If citations[i]> the index, every element following that index is also greater than the H index 
        """ 
        citations.sort() 

        for i in range(len(citations)): 
            if citations[i] >= len(citations) - i: 
                return len(citations)-i
        
        return 0