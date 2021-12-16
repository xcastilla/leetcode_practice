"""
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
Runtime: 556 ms, faster than 69.29% of Python3 online submissions for Find the City With the Smallest Number of Neighbors at a Threshold Distance.
Memory Usage: 15.4 MB, less than 40.69% of Python3 online submissions for Find the City With the Smallest Number of Neighbors at a Threshold Distance.
"""

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Floyd-Warshall: find distances from all nodes to all nodes
        dist = [[float('inf')] * n for _ in range(n)]
        for edge in edges:
            i, j, w = edge
            dist[i][j] = w
            dist[j][i] = w
        for i in range(n):
            dist[i][i] = 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
        # Find result
        min_cities = float('inf')
        res = -1
        for i in range(n):
            count = 0
            for j in range(n):
                if i == j:
                    continue
                if dist[i][j] <= distanceThreshold:
                    count += 1
            if count < min_cities:
                min_cities = count
                res = i
            elif count == min_cities and i > res:
                res = i
        return res
            
                    
                
        
        
                    
            
        
            
            
        
        