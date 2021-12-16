"""
Runtime: 96 ms, faster than 82.05% of Python3 online submissions for Course Schedule.
Memory Usage: 17.4 MB, less than 26.92% of Python3 online submissions for Course Schedule.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(src, visited):
            # Node has permanent mark
            if visited[src] == 2:
                return True
            
            # Node has temporary mark
            if visited[src] == 1:
                return False
            
            # mark node as temporarily visited
            visited[src] = 1
            for neigh in graph[src]:
                if not dfs(neigh, visited):
                    return False
                
            # Mark node as permantently visited
            visited[src] = 2
            return True
        
        # build graph
        graph = defaultdict(list)
        for req in prerequisites:
            graph[req[1]].append(req[0])
        
        visited = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            if visited[i] != 2:
                ret = dfs(i, visited)
                if not ret:
                    return False
        return True
