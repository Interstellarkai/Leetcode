#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start

import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        T : O(V+E) 63.60% | 719ms
        S : O(V) 80.74% | 24.6mb
        """
        # Sanity Check
        if n == 1:
            return [0]

        # Build graph
        graph = collections.defaultdict(list)
        for u, v in edges:
            # outdegree (undirected)
            graph[u].append(v)
            graph[v].append(u)

        # Leaves can't be the root
        leaves = [i for i in range(n) if len(graph[i]) == 1]

        # In each iteration, we remove leaves that can't be the root
        while n > 2:
            n -= len(leaves)

            newLeaves = []
            for leaf in leaves:
                # Remove the connection
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    newLeaves.append(neighbor)

            leaves = newLeaves
        return leaves

# @lc code=end
