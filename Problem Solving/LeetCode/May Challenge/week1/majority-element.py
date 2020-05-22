"""
- DAY 6 -
- Majority Element -

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Ex1:
Input: [3,2,3]
Output: 3

Ex2:
Input: [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.Counter(nums).most_common()
        return max(count, key = itemgetter(1))[0]