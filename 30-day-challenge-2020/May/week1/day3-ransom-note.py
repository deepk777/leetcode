# Ransom Note
# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines
# otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# Constraints:
# You may assume that both strings contain only lowercase letters.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        dic1 = {}
        dic2 = {}
        for r in ransomNote:
            try:
                dic1[r] += 1
            except:
                dic1[r] = 1

        for m in magazine:
            try:
                dic2[m] += 1
            except:
                dic2[m] = 1

        for k, v in dic1.items():
            if k in dic2:
                if v > dic2[k]:
                    return False
            else:
                return False

        return True
