"""
- DAY 15 -
- Maximum Sum Circular Subarray -

Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

Ex1:
Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3

Ex2:
Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

Ex3:
Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

Note:
* -30000 <= A[i] <= 30000
* 1 <= A.length <= 30000

Hint 1:
For those of you who are familiar with the Kadane's algorithm, think in terms of that. 
For the newbies, Kadane's algorithm is used to finding the maximum sum subarray from a given array. 
This problem is a twist on that idea and it is advisable to read up on that algorithm first before starting this problem. 
Unless you already have a great algorithm brewing up in your mind in which case, go right ahead!
"""

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if len(A) == 0: return 0
        maxTotal = A[0]
        maxSoFar = A[0]
        minSoFar = A[0]
        minTotal = A[0]
        s = A[0]
        
        for i in range(1, len(A)):
            maxSoFar = max(A[i], maxSoFar + A[i])
            maxTotal = max(maxTotal, maxSoFar)            
            
            minSoFar = min(A[i], minSoFar + A[i])            
            minTotal = min(minTotal, minSoFar)            
            s += A[i]
            
        if(s == minTotal):return maxTotal
        
        return max(s - minTotal, maxTotal)