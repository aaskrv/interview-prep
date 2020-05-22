"""
- DAY 19 -
- Search in Rotated Sorted Array -

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Ex1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Ex2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return -1
        elif len(nums) == 1 and nums[0]  == target: return 0
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target and nums[mid] >= target:
                    r = mid -1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target and nums[r] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1