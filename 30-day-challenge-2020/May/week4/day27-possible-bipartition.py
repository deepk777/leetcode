# from collections import defaultdict
# Possible Bipartition
#
# Given a set of N people(numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
# Each person may dislike some other people, and they should not go into the same group.
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
# Return true if and only if it is possible to split everyone into two groups in this way.


# Example 1:
# Input: N = 4, dislikes = [[1, 2], [1, 3], [2, 4]]
# Output: true
# Explanation: group1[1, 4], group2[2, 3]

# Example 2:
# Input: N = 3, dislikes = [[1, 2], [1, 3], [2, 3]]
# Output: false

# Example 3:
# Input: N = 5, dislikes = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
# Output: false

# Constraints:
# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# dislikes[i].length == 2
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# There does not exist i != j for which dislikes[i] == dislikes[j].


from collections import defaultdict


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """

        color = {}
        graph = defaultdict(list)
        
        # Make undirected graph using adjacency list
        for s, d in dislikes:
            graph[s].append(d)
            graph[d].append(s)

        def dfs(node, c=0):
            # Check if node is already colored
            # If yes than return True is node has
            # expected coloring else return False.
            if node in color:
                return color[node] == c
            color[node] = c

            for neighbour in graph[node]:
                # Do dfs with the toggle value for c to change color
                if not dfs(neighbour, c ^ 1):
                    return False

            return True

        # Main idea is that we start coloring nodes and if any time
        # we are back to node with same color as last one than we
        # are trapped and we can't find the bipartition possible.
        # We check this for each connected component in graph.
        for node in range(1, N+1):
            if node not in color and not dfs(node):
                return False

        return True
