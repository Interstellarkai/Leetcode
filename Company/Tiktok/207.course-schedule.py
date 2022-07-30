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
        Kahn's algorithm
        T : O(V+E) 93.11% | 103ms
        S : O(V) 76.06% | 15.5mb
        """
        adj_list = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for pre in prerequisites:
            # 1. initialize the graph
            # key: node, value: list of neighbors that points to node
            adj_list[pre[1]].append(pre[0])
            # 2. initialize the in-degree of each node. (no. of connections pointing inward at a vertex)
            # key: node, value: in-degree.
            indegree[pre[0]] += 1
        # 3. initialize the queue
        # start off with nodes with no incoming edges (i.e. Must take this course first then can take any other course)
        starts = [i for i in range(numCourses) if not indegree[i]]
        # 4. initialize a set to track visited nodes
        visited = set()
        # 5. while the queue is not empty
        while starts:
            # 6. pop a node from the queue
            node = starts.pop()
            if node in visited:
                continue
            # 7. Add the visited nodes
            visited.add(node)
            # 8. for each of the neighbors of node
            for neigh in adj_list[node]:
                # 9. decrement the in-degree of the neighbor
                indegree[neigh] -= 1
                # 10. if the in-degree of the neighbor is zero
                if not indegree[neigh]:
                    # 11. add neighbor to the queue
                    starts.append(neigh)
        # 12. if the number of visited nodes is equal to the total number of nodes
        return len(visited) == numCourses

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
        Topological Sort via DFS / BFS.

        Topological Sort Algorithm (TopSort)
        1. Pick an unvisited node
        2. Beginning with the selected node, do a Depth First Search (DFS) exploring only unvisited nodes.
        3. On the recursive callback of the DFS, add the current node to the topological ordering in reverse order.
        T : O(V+E)
        S : O(V)
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        # create graph
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)
        # visit each node
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True

    def dfs(self, graph, visited, i):
        # if ith node is marked as being visited, then a cycle is found
        if visited[i] == -1:
            return False
        # if it is done visted, then do not visit again
        if visited[i] == 1:
            return True
        # mark as being visited
        visited[i] = -1
        # visit all the neighbours
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        # after visit all the neighbours, mark it as done visited
        visited[i] = 1
        return True


# @lc code=end
