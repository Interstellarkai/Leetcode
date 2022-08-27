#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start

import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        T : O(V+E) 54.95% | 159ms
        S : O(V) 58.41% | 15.7mb
        """
        # Intialize the graph
        graph = collections.defaultdict(list) # outdegree
        indegree = collections.defaultdict(int)
        visited = set()
        ordering = []

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        # Topological Sort
        stack = [i for i in range(numCourses) if indegree[i] == 0]
        while stack:
            course = stack.pop()
            if course in visited:
                continue
            visited.add(course)
            ordering.append(course)

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    stack.append(neighbor)

        return ordering if len(ordering) == numCourses else None
        # @lc code=end
