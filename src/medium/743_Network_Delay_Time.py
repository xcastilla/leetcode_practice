"""
https://leetcode.com/problems/network-delay-time/
Runtime: 1092 ms, faster than 10.96% of Python3 online submissions for Network Delay Time.
Memory Usage: 16.1 MB, less than 90.31% of Python3 online submissions for Network Delay Time.
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Bellman-Ford
        d = [float('inf')] * n
        # nodes from 1 to V, so we offset them by -1
        d[k-1] = 0
        for i in range(n - 1):
            for u, v, w in times:
                if d[u-1] + w < d[v-1]:
                    d[v-1] = d[u-1] + w
        
        m_time = max(d)
        return m_time if m_time != float('inf') else -1


"""
Runtime: 432 ms, faster than 97.04% of Python3 online submissions for Network Delay Time.
Memory Usage: 16 MB, less than 97.33% of Python3 online submissions for Network Delay Time.
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Using Dijkstra
        graph = defaultdict(dict)
        # nodes from 1 to V, so we offset them by -1
        for u, v, w in times:
            graph[u-1][v-1] = w
        
        d = [float('inf')] * n
        d[k-1] = 0
        q = [(0, k-1)]
        
        while len(q):
            dist, node = heapq.heappop(q)
            if dist > d[node]:
                continue
                
            for neigh in graph[node].keys():
                new_dist = dist + graph[node][neigh]
                if new_dist < d[neigh]:
                    d[neigh] = new_dist
                    heapq.heappush(q, (new_dist, neigh))
                    
        max_d = max(d)
        return max_d if max_d != float('inf') else -1
                    
                
                
            
        
        
        
        