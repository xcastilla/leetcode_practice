"""
https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree
TODO: Time Limit Exceeded
"""

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:    
        def union(u, v, parents, rank):
            x = find(u, parents)
            y = find(v, parents)
            
            if x == y:
                return False
            
            if rank[x] > rank[y]:
                parents[x] = y
            elif rank[x] < rank[y]:
                parents[y] = x
            else:
                rank[y] += 1
                parents[x] = y
                
            return True
            
            
        def find(u, parents):
            while parents[u] != u:
                u = parents[u]
            return u
            
            
        def helper(i, parents, rank, included, cost):
            if cost > self.min_tree_cost:
                return
            if len(included) == n - 1:
                # is tree minimal?
                if cost < self.min_tree_cost:
                    self.min_tree_cost = cost
                    self.trees = [set(included)]
                elif cost == self.min_tree_cost:
                    self.trees.append(set(included))
                return
            
            if i >= len(edges):
                return
            
            p = parents.copy()
            r = rank.copy()
            # try including and not including curent edge
            u, v, w = edges[i]
            if union(u, v, p, r):
                helper(i + 1, p, r, included + [i], cost + w)
            helper(i + 1, parents.copy(), rank.copy(), included, cost)
            
            return
                  
        self.min_tree_cost = float('inf')
        parents = [i for i in range(n)]
        rank = [0] * n
        
        helper(0, parents, rank, [], 0)
        inter_set = self.trees[0]
        union_set = self.trees[0]
        for i in range(1, len(self.trees)):
            inter_set = inter_set.intersection(self.trees[i])
            union_set = union_set.union(self.trees[i])
        union_set = union_set.difference(inter_set)

        return [list(inter_set), list(union_set)]
        
            
        
        
        
        
        
        
            