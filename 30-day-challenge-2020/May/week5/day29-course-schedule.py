# Course Schedule
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0, 1]
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
# Example 1:
# Input: numCourses = 2, prerequisites = [[1, 0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
#
# Example 2:
# Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should
# also have finished course 1. So it is impossible.
#
# Constraints:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 1 <= numCourses <= 10 ^ 5

from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.WHITE = 0
        self.GREY = 1
        self.BLACK = 2

    def topoSort(self, graph, node, visited):
        if visited[node] == self.GREY:
            return False

        if visited[node] == self.BLACK:
            return True

        visited[node] = self.GREY
        for adj in graph[node]:
            if visited[adj] == self.GREY:  # this is a cycle
                return False
            elif not self.topoSort(graph, adj, visited):
                return False

        visited[node] = self.BLACK
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        visited = [self.WHITE]*numCourses

        for course, dependency in prerequisites:
            graph[dependency].append(course)

        for course in range(numCourses):
            if not self.topoSort(graph, course, visited):
                return False

        return True
