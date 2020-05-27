# Find the Town Judge
#
# In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.
#
# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody(except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.
#
# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
#
#
# Example 1:
# Input: N = 2, trust = [[1, 2]]
# Output: 2
#
# Example 2:
# Input: N = 3, trust = [[1, 3], [2, 3]]
# Output: 3
#
# Example 3:
# Input: N = 3, trust = [[1, 3], [2, 3], [3, 1]]
# Output: -1
#
# Example 4:
# Input: N = 3, trust = [[1, 2], [2, 3]]
# Output: -1
#
# Example 5:
# Input: N = 4, trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
# Output: 3
#
#
# Constraints:
# 1 <= N <= 1000
# 0 <= trust.length <= 10 ^ 4
# trust[i].length == 2
# trust[i] are all different
# trust[i][0] != trust[i][1]
# 1 <= trust[i][0], trust[i][1] <= N

from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        trust_count = {i: 0 for i in range(1, N+1)}
        max_trust = (0, 1)
        votes = [0]*(N+1)

        for t in trust:
            trust_count[t[1]] += 1
            votes[t[0]] = 1
            if trust_count[t[1]] > max_trust[0]:
                max_trust = (trust_count[t[1]], t[1])

        if max_trust[0] == N-1 and votes[max_trust[1]] == 0:
            return max_trust[1]

        return -1
