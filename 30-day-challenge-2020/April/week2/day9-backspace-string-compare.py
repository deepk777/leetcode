# Backspace String Compare
# # means a backspace character.
# Given two strings S and T, return if they are equal when both are typed into empty text editors.

# Note that after backspacing an empty text, the text will continue empty.

# Example 1:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:

# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:

# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:

# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# Follow up:

# Can you solve it in O(N) time and O(1) space?


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_hash_count = t_hash_count = 0
        final_S = final_T = ""

        for i in range(len(S)-1, -1, -1):
            if S[i] == '#':
                s_hash_count += 1
            elif s_hash_count:
                s_hash_count -= 1
            else:
                final_S = S[i] + final_S

        for i in range(len(T)-1, -1, -1):
            if T[i] == '#':
                t_hash_count += 1
            elif t_hash_count:
                t_hash_count -= 1
            else:
                final_T = T[i] + final_T

        return final_T == final_S
