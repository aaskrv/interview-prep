"""
- DAY 4 -
- Move Zeroes -

Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Ex:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations

HINT 1:
In-place means we should not be allocating any space for extra array. 
But we are allowed to modify the existing array. However, as a first step, 
try coming up with a solution that makes use of additional space. 
For this problem as well, first apply the idea discussed using an additional array 
and the in-place solution will pop up eventually.

HINT 2:
A two-pointer approach could be helpful here. The idea would be to have one pointer 
for iterating the array and another pointer that just works on the non-zero elements of the array.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        for i in range(count, len(nums)):
            nums[i] = 0