"""
- DAY 14 -
- Perform String Shifts -

You are given a string s containing lowercase English letters, and a matrix shift,
where shift[i] = [direction, amount]

- direction can be 0 (for left shift) or 1 (for right shift)
- amount is the amount by which string s is to be shifted
- a left shift by 1 means remove the first character of s and append it to the end
- similarly, a right shift by 1 means remove the last character of s and add it to the beginning

Return the final string after all operations.

Ex1:
Input: s = 'abc', shift = [[0, 1], [1, 2]]
Output: 'cab'
Explanation:
[0, 1] means shift to left by 1. 'abc' -> 'bca'
[1, 2] means shift to right by 2. 'bca' -> 'cab'

Constraints:
- 1 <= s.length <= 100
- s only contains lower case English letters
- 1 <= shift.length <= 100
- shift[i].length == 2
- 0 <= shift[i][0] <= 1
- 0 <= shift[i][1] <= 100
"""

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        sfts = 0
        
        for sft in shift:
            if sft[0] == 0:
                sfts -= sft[1]
            else:
                sfts += sft[1]
        
        if sfts > 0:
            r = sfts % len(shift)
            return s[-r:] + s[:-r]
        else:
            l = abs(sfts) % len(shift)
            return s[l:] + s[:l]