"""
https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies
Runtime: 919 ms, faster than 76.89% of Python3 online submissions for Find All Possible Recipes from Given Supplies.
Memory Usage: 23.3 MB, less than 5.33% of Python3 online submissions for Find All Possible Recipes from Given Supplies.
"""

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        def dfs(node, visited):
            if node not in visited:
                if node not in graph:
                    return False
                visited[node] = 1
                flag = True
                for ing in graph[node]:
                    if not dfs(ing, visited):
                        flag = False
                        break       
                if flag:
                    visited[node] = 2
            return visited[node] == 2

        graph = defaultdict(list)
        for i, r in enumerate(recipes):
            graph[r] = ingredients[i]
        visited = { s: 2 for s in supplies }

        ret = []
        for r in recipes:
            if dfs(r, visited):
                ret.append(r)
        return ret


"""

Runtime: 2200 ms, faster than 19.31% of Python3 online submissions for Find All Possible Recipes from Given Supplies.
Memory Usage: 17.2 MB, less than 24.80% of Python3 online submissions for Find All Possible Recipes from Given Supplies.
"""

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ret = []
        sup = set(supplies)
        added = True
        ingredients = [set(i) for i in ingredients]
        while added:
            i = 0
            l = len(recipes)
            added = False
            while i < l:
                if len(ingredients[i]) == len(ingredients[i].intersection(sup)):
                    sup.add(recipes[i])
                    ret.append(recipes[i])
                    recipes.pop(i)
                    ingredients.pop(i)
                    l -= 1
                    added = True
                else:
                    i += 1
                
        return ret
            
        