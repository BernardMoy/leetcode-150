# LeetCode Top Interview 150 Questions 

An attempt on the LeetCode 150 questions over summer 2025, categorised into 23 different topics, and designed for mastering coding interviews. This strengthened my skills on data structures and algorithms, as well as technical problem-solving. 

The questions can be viewed [here](https://leetcode.com/studyplan/top-interview-150/). 

## Language 
Python3

## Notable questions 
The following questions are exceptionally difficult in my opinion, as they require intelligent, problem-specific skills to solve: 

[Container with most water](https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150) / [Trapping rain water](https://leetcode.com/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-interview-150): Two pointers, shrink the side with a smallest height in order to make an attempt to maximise the area. 

[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150): Think of using prefix and postfix (precomputed results) when the division operator can't be used. 

[Majority element](https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150): Use a count variable that increments and decrements. The majority element will never cause the count to go below zero towards the end, caused by other elements. 

[Minimum window substring](https://leetcode.com/problems/minimum-window-substring/description/?envType=study-plan-v2&envId=top-interview-150): Two pointers, instead of comparing two dictionaries everytime, keep a separate required length variable that +1 when a required letter is being removed. 

[LRU Cache](https://leetcode.com/problems/lru-cache/description/?envType=study-plan-v2&envId=top-interview-150): Implement a heap that get min element in O(1) time: use a doubly linked list where the least called elements are shifted to the left side. 

[Binary tree max path sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/?envType=study-plan-v2&envId=top-interview-150): Maintain a global ans variable to check for bending paths, instead of checking them in the dfs. 

[Merge k sorted lists](https://leetcode.com/problems/merge-k-sorted-lists/?envType=study-plan-v2&envId=top-interview-150): Store the index in the heap to keep every entry distinct. 

[Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/description/?envType=study-plan-v2&envId=top-interview-150): N & (N-1) unsets the rightmost set bit in N. 

[Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/?envType=study-plan-v2&envId=top-interview-150): Get trailing zeroes but recursively computing 5 factors. 

[Best time to buy and sell stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/?envType=study-plan-v2&envId=top-interview-150): Maintain 2 DP tables, where sell depends on the value previously bought, and buy depends on the value after selling the previous value. 
