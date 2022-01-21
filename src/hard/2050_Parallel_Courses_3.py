"""
https://leetcode.com/problems/parallel-courses-iii
Runtime: 1648 ms, faster than 84.53% of Python3 online submissions for Parallel Courses III.
Memory Usage: 43.4 MB, less than 85.50% of Python3 online submissions for Parallel Courses III.
"""

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int: 
        # find sources and destinations
        in_d = [0] * n
        graph = defaultdict(list)
        for pr, ne in relations:
            graph[pr - 1].append(ne - 1)
            in_d[ne - 1] += 1
        dist = time.copy()
        q = []
        for i in range(n):
            if in_d[i] == 0:
                q.append(i)
        mx = 0
        while q:
            nd = q.pop()
            if len(graph[nd]) == 0:
                mx = max(dist[nd], mx)
            for neigh in graph[nd]:
                if dist[nd] + time[neigh] > dist[neigh]:
                    dist[neigh] = dist[nd] + time[neigh]
                in_d[neigh] -= 1
                # only consider nodes when we have explored all paths to them
                if in_d[neigh] == 0:
                    q.append(neigh)
                    
        return mx
    


"""

Runtime: 4372 ms, faster than 6.23% of Python3 online submissions for Parallel Courses III.
Memory Usage: 43.8 MB, less than 65.89% of Python3 online submissions for Parallel Courses III.
"""
                
        
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int: 
        # find sources and destinations
        in_d = [0] * n
        graph = defaultdict(list)
        for pr, ne in relations:
            graph[pr - 1].append(ne - 1)
            in_d[ne - 1] += 1

        dist = time.copy()
        
        src = []
        for i in range(n):
            if in_d[i] == 0:
                src.append(i)
        
        mx = 0
        for s in src:
            q = [s]
            while q:
                n = q.pop()
                if len(graph[n]) == 0:
                    mx = max(dist[n], mx)
                for neigh in graph[n]:
                    if dist[n] + time[neigh] > dist[neigh]:
                        dist[neigh] = dist[n] + time[neigh]
                        q.append(neigh)

        return mx

        
        
        
        