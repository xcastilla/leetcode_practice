"""
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
Runtime: 144 ms, faster than 89.70% of Python3 online submissions for Most Stones Removed with Same Row or Column.
Memory Usage: 15.1 MB, less than 64.35% of Python3 online submissions for Most Stones Removed with Same Row or Column.
"""

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def find(u, parent):
            while parent[u] != u:
                u = parent[u]
            return u
        
        def union(u, v, parent, rank):
            x = find(u, parent)
            y = find(v, parent)

            # If parents are the same, 
            if x == y:
                return
            
            if rank[x] > rank[y]:
                parent[x] = y
            elif rank[x] < rank[y]:
                parent[y] = x
            else:
                parent[x] = y
                rank[y] += 1
            self.count += 1
            return
    
        parent = [0] * len(stones)
        for i in range(len(stones)):
            parent[i] = i
            
        rank = [0] * len(stones)
        
        # Row and col keep track of the id of stones we've seen in the same row/col
        row = {}
        col = {}
        self.count = 0
        for i, (r, c) in enumerate(stones):
            if r in row:
                # if we've seen a stone in this row, union the current id with the one seen before and count it as deleted
                union(i, row[r], parent, rank)
            else:
                row[r] = i
                 
            if c in col:
                union(i, col[c], parent, rank)
            else:
                col[c] = i

                
        return self.count
            
                
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        
        