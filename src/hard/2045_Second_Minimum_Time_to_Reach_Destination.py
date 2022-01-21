"""
https://leetcode.com/problems/second-minimum-time-to-reach-destination/
Runtime: 2216 ms, faster than 86.12% of Python3 online submissions for Second Minimum Time to Reach Destination.
Memory Usage: 24.6 MB, less than 13.18% of Python3 online submissions for Second Minimum Time to Reach Destination.
"""

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
            
        q = [(1, 0, 0)]
        best_t = None
        visited = [0] * (n + 1)
        while q:
            new_q = []
            new_q_s = set()
           
            while q:
                node, t, w = q.pop()
                if node == n:
                    if best_t is None:
                        best_t = t
                    elif t > best_t:
                        return t
                
                # how much do we wait
                if ((t + time + w) // change) % 2 == 0:
                    new_w = 0
                else:
                    new_w = change - ((t + time + w) % change)

                for neigh in graph[node]:
                    if neigh not in new_q_s and visited[neigh] < 2:
                        visited[neigh] += 1
                        new_q_s.add(neigh)
                        new_q.append((neigh, t + time + w, new_w))
            q = new_q
                
        return -1
                
                
            
        
        