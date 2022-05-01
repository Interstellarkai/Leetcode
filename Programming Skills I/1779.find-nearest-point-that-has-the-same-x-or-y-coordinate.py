#
# @lc app=leetcode id=1779 lang=python3
#
# [1779] Find Nearest Point That Has the Same X or Y Coordinate
#

# @lc code=start
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        """
        Idea: 
        1. Find the valid points via comparison
        2. Find the manhattan distance between myself to the valid points
        3. Get the shortest distance valid point
        4. If there are few points returned. Get the smallest index

        T : O(N)
        S : O(N)
        """
        # Valid points
        validPoints = [point for point in points if (
            point[0] == x or point[1] == y)]

        # Main
        if validPoints:
            # Manhattan distance
            distance = [(abs(x - point[0]) + abs(y - point[1]))
                        for point in validPoints]
            # Shortest Manhattan distance based on the valid point
            minDistance = min(distance)
            # returns the first identified index that has this val
            index = distance.index(minDistance)
            validPoint = validPoints[index]

            # Index from Point List
            index = points.index(validPoint)
            return index

        # Default : If no valid points
        return -1

    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # Initialize
        index, smallest = -1, 99999

        # Enumerate through all points
        for i, (r, c) in enumerate(points):
            dx, dy = x - r, y - c
            # if (dx * dy == 0) --> valid point
            if dx * dy == 0 and abs(dx + dy) < smallest:
                smallest = abs(dx + dy)
                index = i

        return index
# @lc code=end
