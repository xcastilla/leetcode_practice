"""
Runtime: 96 ms, faster than 87.32% of Python3 online submissions for Course Schedule II.
Memory Usage: 17.4 MB, less than 24.18% of Python3 online submissions for Course Schedule II.
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(node, visited):
            # temporary mark
            if visited[node] == 1:
                return False
            # permanent mark
            elif visited[node] == 2:
                return True
            
            # mark as temporarily visited
            visited[node] = 1
            for neigh in graph[node]:
                if not dfs(neigh, visited):
                    return False
            # mark as permanently visited
            visited[node] = 2
            stack.insert(0, node)
            return True
        
        # build graph
        graph = [[] for _ in range(numCourses)]
        for req in prerequisites:
            graph[req[1]].append(req[0])

        stack = []
        visited = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            if visited[i] != 2:
                ret = dfs(i, visited)
                if not ret:
                    return []
        return stack
        
        
        