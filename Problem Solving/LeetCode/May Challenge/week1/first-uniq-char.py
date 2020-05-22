"""
- DAY 5 -
- First Unique Character in a String -

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Ex:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: 
You may assume the string contain only lowercase letters.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0: return -1
        count = collections.Counter(s)
        for idx, c in enumerate(s):
            if count[c] == 1:
                return idx
        return -1