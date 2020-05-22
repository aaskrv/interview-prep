"""
- DAY 3 -
- Maximum Subarray -

Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Ex:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution 
using the divide and conquer approach, which is more subtle.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending = max_current = nums[0]

        for i in nums[1:]:
            max_ending = max(i, max_ending + i)
            max_current = max(max_current, max_ending)
        return max_current
