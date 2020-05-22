"""
- DAY 9 -
- Valid Perfect Square -

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Ex1:
Input: num = 16
Output: true

Ex2:
Input: num = 14
Output: false

Constraints:
* 1 <= num <= 2^31 - 1
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = 1
        while(n * n <= num): 
            if ((num % n == 0) and (num / n == n)): 
                return True
            n += 1
        return False