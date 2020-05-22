"""
- DAY 13 -
- Contiguous Array -

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Ex1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Ex2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note:
The length of the given binary array will not exceed 50,000.
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_len = 0
        counts = {0:-1}
        
        for idx, num in enumerate(nums):
            if num == 1: count += 1
            else: count -= 1
                
            if count not in counts:
                counts[count] = idx
            else:
                max_len = max(max_len, idx - counts[count])
        
        return max_len