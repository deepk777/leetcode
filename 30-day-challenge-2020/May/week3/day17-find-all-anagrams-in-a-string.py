# Find All Anagrams in a String
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20, 100.
# The order of output does not matter.
#
# Example 1:
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
#
# Example 2:
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        ans = []
        ana_map = defaultdict(int)
        p_len = len(p)

        if not s:
            return []

        for c in p:
            ana_map[c] += 1

        si = ei = 0

        while ei < len(s):
            flag = False

            if s[ei] in ana_map:
                ana_map[s[ei]] -= 1

            if ei - si + 1 == p_len:
                for _, v in ana_map.items():
                    if v != 0:
                        flag = False
                        break
                    else:
                        flag = True

                # If flag is True that means we have a found a anagram
                if flag:
                    ans.append(si)

                # Shift the window by one step from start if len was match
                if s[si] in ana_map:
                    ana_map[s[si]] += 1
                si += 1

            # Keep shifting the window by one step from end.
            ei += 1

        return ans
