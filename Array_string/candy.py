class Solution:
    def candy(self, ratings: List[int]) -> int:
        """ 
        A higher rating child only neds to have more candies than their local neighbours, not global
        Iterate from the left to right (check right neighbours) and then right to left (check left neighbours). 
        Initialise the ans array to all 1s. 
        """ 

        arr = [1 for x in range(len(ratings))]

        for i in range(len(ratings)-1): 
            if ratings[i] < ratings[i+1] and arr[i] >= arr[i+1]: 
                arr[i+1] = arr[i]+ 1
        
        for i in range(len(ratings)-2, -1, -1): 
            if ratings[i] > ratings[i+1] and arr[i] <= arr[i+1]:
                arr[i] = arr[i+1]+1
        
        return sum(arr)