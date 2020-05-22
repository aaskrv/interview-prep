"""
- DAY 7 -
- Counting Elements -

Given an integer array arr, count element x such that
x + 1 is also in arr.

If there're duplicates in arr, count them separately.

Ex1:
Input: arr = [1,3, 2, 3, 5, 0]
Output: 3
Explanation: 0, 1 and 2 are counted cause 1, 2, 3 are in arr.

Ex2:
Input: [1, 1, 3, 3, 5, 5]
Output: 0
Explanation: No numbers are counted.
"""

class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        for i in range(0, len(arr)):
            x = arr[i] + 1
            if x in arr: count += 1
                
        return count
