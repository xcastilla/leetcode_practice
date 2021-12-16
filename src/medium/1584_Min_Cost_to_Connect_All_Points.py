"""
Runtime: 1052 ms, faster than 91.74% of Python3 online submissions for Min Cost to Connect All Points.
Memory Usage: 82.7 MB, less than 74.33% of Python3 online submissions for Min Cost to Connect All Points.
"""

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(parent, u):
            if parent[u] == u:
                return u
            return find(parent, parent[u])
        
        def union(parent, rank, u, v):
            xroot = find(parent, u)
            yroot = find(parent, v)
            
            if rank[xroot] > rank[yroot]:
                parent[xroot] = yroot
            elif rank[yroot] > rank[xroot]:
                parent[yroot] = xroot
            else:
                parent[xroot] = yroot
                rank[yroot] += 1
            
        # Create a priority list of all edges in graph
        q = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(q, (dist, i, j))
        
        e_added = 0
        cost = 0 
        uf_set = [i for i in range(len(points))]
        rank = [0 for _ in range(len(points))]
        
        while e_added < len(points) - 1:
            dist, src, dst = heapq.heappop(q)
            x = find(uf_set, src)
            y = find(uf_set, dst)
            if x != y:
                e_added += 1
                cost += dist
                
                union(uf_set, rank, x, y)
            
        return cost
            