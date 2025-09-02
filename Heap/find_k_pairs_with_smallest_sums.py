class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """ 
        Two-pointer like approach - a heap that stores (sum, i, j) (i,j are 2 pointers) 
        Append the sum of (i+1,j) and (i,j+1) and let the heap do its work
        it doesnt matter about storing extra unused pairs in this case 
        """ 

        heap = [(nums1[0] + nums2[0], 0, 0)]   # store (sum, i, j) pairs 
        heapq.heapify(heap) 
        ans = [] 
        visited = set() 

        while len(ans) < k: 
            s, i, j = heapq.heappop(heap) 

            # delete duplicates of (i,j) index
            # nums[i], nums[j] pairs can be duplicated, but not indices
            if (i,j) in visited: 
                continue 
            visited.add((i,j))

            ans.append([nums1[i], nums2[j]])

            # Append both (i+1, j) and (i, j+1) to the heap (Both arrays are sorted) 
            if i<len(nums1)-1: 
                heapq.heappush(heap, (nums1[i+1] + nums2[j], i+1, j))
            
            if j<len(nums2)-1: 
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
        
        return ans 