"""
- DAY 13 -
- Remove K Digits -

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
* The length of num is less than 10002 and will be ≥ k.
* The given num does not contain any leading zero.

Ex1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Ex2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k: return '0'
        res = []
        
        def findMin(self, number, n):
            if n == 0: 
                res.append(number)
                return
            l = len(number)
            
            if l <= n: return
            
            min_idx = 0
            for i in range(1, n+1):
                if number[i] < number[min_idx]:
                    min_idx = i
                    
            res.append(number[min_idx])
            
            new_num = number[min_idx + 1:]
            
            findMin(self, new_num, n - min_idx)
            
        findMin(self, num, k)
        
        min_number = ''.join(res)
        
        return str(int(min_number))

