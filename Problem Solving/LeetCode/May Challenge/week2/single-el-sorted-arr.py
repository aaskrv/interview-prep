"""
- DAY 12 -
- Single Element in a Sorted Array -

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

Ex1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Ex2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:
* 1 <= nums.length <= 10^5
* 0 <= nums[i] <= 10^5
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    l = mid + 2
                else:
                    r = mid
            else:
                if nums[mid] == nums[mid - 1]:
                    l = mid + 1
                else:
                    r = mid
        
        return nums[l]