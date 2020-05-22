"""
- DAY 3 -
- Ransom Note -

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Ex1:
Input: ransomNote = "a", magazine = "b"
Output: false

Ex2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Ex3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
You may assume that both strings contain only lowercase letters.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn = set(ransomNote)
        for char in rn:
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True