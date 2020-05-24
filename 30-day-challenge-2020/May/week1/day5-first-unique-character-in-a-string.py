# First Unique Character in a String
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:
# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.

# Note: You may assume the string contain only lowercase letters.


class Solution:
    def firstUniqChar(self, s: str) -> int:

        dictionary = {}
        for c in s:
            try:
                dictionary[c] += 1
            except:
                dictionary[c] = 1

        for c in s:
            if dictionary[c] == 1:
                return s.index(c)

        return -1
