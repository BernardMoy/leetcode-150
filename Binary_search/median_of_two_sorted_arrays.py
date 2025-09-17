class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """ 
        The job is to find a way to partition the two arrays, which when combined becomes sorted: 
        [1,3,8] [7,9,10,11] -> [1,3  |  8]  [7  |  9, 10, 11] 
        when combined becomes [1,3,7] [8,9,10,11] -> sorted 
        here, minleft1 = 1, maxleft1 = 3, max/minright1 = 8

        when maxleft1 > minright2, the first partition is too far to the right -> encourage left 
        """ 

        # assume len(nums1) <= len(nums2) 
        if len(nums1) > len(nums2): 
            nums1, nums2 = nums2, nums1 
        
        len1, len2 = len(nums1), len(nums2) 
        l, r = 0, len1 

        while l <= r: 
            m1 = (l+r)//2
            m2 = (len1+len2+1)//2 - m1  # m1 + m2 = total number of elements on the left side of the merged arr 
            # +1 so that when the total number of elements is odd, the central value is on the left 

            # initialise max to -inf, and min to inf 
            max_left1 = float('-inf') if m1 == 0 else nums1[m1 - 1]
            min_right1 = float('inf') if m1 == len1 else nums1[m1]
            max_left2 = float('-inf') if m2 == 0 else nums2[m2 - 1]
            min_right2 = float('inf') if m2 == len2 else nums2[m2]

            # this condition mean combining lefts, then merge the combined right ones, result in a sorted array 
            # note that max left 1 <= min right 1 (array is sorted) 
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # even 
                if (len1 + len2)%2 == 0: 
                    return (max(max_left1, max_left2) + min(min_right1, min_right2))/2
                else: 
                    return max(max_left1, max_left2)  # median included in left partition
            
            # max left 1 > min right 2 means the partition is too far to the right -> search the left partition
            elif max_left1 > min_right2: 
                r = m1-1
            else: 
                l = m1+1