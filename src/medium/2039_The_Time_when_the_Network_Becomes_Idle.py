"""
https://leetcode.com/problems/the-time-when-the-network-becomes-idle
Runtime: 3112 ms, faster than 34.54% of Python3 online submissions for The Time When the Network Becomes Idle.
Memory Usage: 68.4 MB, less than 56.63% of Python3 online submissions for The Time When the Network Becomes Idle.
"""

class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph = defaultdict(list)
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
        
        # bfs to find shortest distance to each node
        visited = [False] * len(patience)
        dist = [float('inf')] * len(patience)
        q = [0]
        dist[0] = 0
        visited[0] = True
        while q:
            el = q.pop(0)
            for neigh in graph[el]:
                if not visited[neigh]:
                    dist[neigh] = dist[el] + 1
                    q.append(neigh)
                    visited[neigh] = True
        
        # find max
        mx = 0
        for i in range(1, len(patience)):
            t = 2 * dist[i]
            if 2 * dist[i] > patience[i]:
                n = (2 * dist[i] - 1) // patience[i]
                t += n * patience[i]
            mx = max(t, mx)
        
        return mx + 1
        