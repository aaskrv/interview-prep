"""
- DAY 18 -
- Permutation in String -

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Ex1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Ex2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

Constraints:
* The input strings only contain lower case letters.
* The length of both given strings is in range [1, 10,000].
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1 = len(s1)
        ls2 = len(s2)
        counter1 = collections.Counter(s1)
        counter2 = collections.Counter(s2[:ls1])
            
        left = 0
        right = ls1
        
        while right < ls2:
            if counter1 == counter2: return True
            
            counter2[s2[left]] -= 1
            
            if counter2[s2[left]] < 1: 
                
                counter2.pop(s2[left]) 
            
            counter2[s2[right]] = counter2.get(s2[right], 0) + 1
            
            left += 1
            right += 1
            
        return counter2 == counter1