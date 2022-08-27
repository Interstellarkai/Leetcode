#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        T : O(V+E) 54.45% | 154ms
        S : O(V) 70.84% | 15.7mb
        """
        # Initialize graph
        adj_list = collections.defaultdict(list) # outdegree
        indegree = collections.defaultdict(int)
        visited = set()
        for course, pre in prerequisites:
            adj_list[pre].append(course)
            indegree[course] += 1

        # Topological sort (Do as list, and pop for faster runtime)
        queue = collections.deque(
            [i for i in range(numCourses) if indegree[i] == 0])
        while queue:
            course = queue.popleft()
            # Housekeeping
            if course in visited:
                continue
            visited.add(course)
            # Recursive
            for new_courses in adj_list[course]:
                indegree[new_courses] -= 1
                if indegree[new_courses] == 0:
                    queue.append(new_courses)

        return len(visited) >= numCourses
# @lc code=end
