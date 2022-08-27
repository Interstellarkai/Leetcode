#
# @lc app=leetcode id=2115 lang=python3
#
# [2115] Find All Possible Recipes from Given Supplies
#

# @lc code=start

import collections


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        Ref : https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/discuss/1664405/Beginners-Friendly-oror-Well-Explained-oror-94-Faster
        T : O(V+E , Receipes + Ingredients)
        T : O(V)
        """
        graph = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)

        for recipe, ingredient in zip(recipes, ingredients): # Tuple of (recipe, and its ingredients) combo
            for i in ingredient:
                graph[i].append(recipe) # Recipe's indegree (recipe needs all the indegree to be present)
                in_degree[recipe] += 1

        queue = supplies[::] # Pass by reference, ingredients that are available and unlimited
        res = []
        while queue:
            ingredient = queue.pop(0)
            # E.g., Bread; Bread + Meat = Sandwich
            if ingredient in recipes:
                res.append(ingredient)

            for neighbor in graph[ingredient]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return res
# @lc code=end
