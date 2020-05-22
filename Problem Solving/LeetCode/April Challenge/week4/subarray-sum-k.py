"""
- DAY 22 -
- Subarray Sum Equals K -

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Ex1:
Input:nums = [1,1,1], k = 2
Output: 2

Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = dict()
        
        current_sum = count = 0
        
        for i in range(len(nums)):
            current_sum += nums[i]
            
            if current_sum == k: count += 1
            
            if (current_sum - k) in sums:
                count += sums[current_sum - k]
                
            if current_sum in sums:
                sums[current_sum] += 1
            else:
                sums[current_sum] = 1
            
        return count