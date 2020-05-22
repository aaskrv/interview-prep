"""
- DAY 16 -
- Valid Parenthesis String -

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
5. An empty string is also valid.

Ex1:
Input: "()"
Output: True

Ex2:
Input: "(*))"
Output: True

Note:
The string size will be in the range [1, 100].
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        
        if n == 0 or s == "*": return True
        elif n == 1: return False 
        
        l_count = r_count = 0
        
        for i in range(0, n):
            if s[i] == ")": l_count -= 1
            else: l_count += 1
            
            if s[n-i-1] == "(": r_count -= 1
            else: r_count += 1
        
            if l_count < 0  or r_count < 0: return False
        return True