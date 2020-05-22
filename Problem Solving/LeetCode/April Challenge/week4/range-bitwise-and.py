"""
- DAY 23 -
- Bitwise AND of Numbers Range -

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Ex1:
Input: [5,7]
Output: 4

Ex2:
Input: [0,1]
Output: 0
"""

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n: return m
        count = 0
        
        while m != n:
            if m != 0:
                m >>= 1
            n >>= 1
            count += 1
        
        return n << count