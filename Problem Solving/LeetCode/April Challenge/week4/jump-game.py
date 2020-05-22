"""
- DAY 25 -
- Jump Game -

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Ex1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Ex2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:

1 <= nums.length <= 3 * 10^4
0 <= nums[i][j] <= 10^5
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        
        if l <= 1: return True
        elif nums[0] == 0: return False
        
        steps = max_reach = nums[0]
        jumps = 1
        
        for i in range(1, l):
            if i == l-1: return True
            
            max_reach = max(max_reach, i + nums[i])
            steps -= 1
            
            if steps == 0:
                jumps += 1
                if i >= max_reach: return False
            
            steps = max_reach - i
        
        return False