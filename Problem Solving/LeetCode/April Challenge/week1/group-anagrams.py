"""
- DAY 6 -
- Group Anagrams -

Given an array of strings, group anagrams together.

Ex:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        result = list(list())
        
        for s in strs:
            temp = ''.join(sorted(s))
            
            if temp in anagrams:
                anagrams[temp].append(s)
            else:
                anagrams[temp] = [s]
                
        for i in anagrams:
            result.append(anagrams[i])
            
        return result
