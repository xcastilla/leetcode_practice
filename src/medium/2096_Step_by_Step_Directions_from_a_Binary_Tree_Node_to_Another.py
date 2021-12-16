"""
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
Runtime: 870 ms, faster than 77.57% of Python3 online submissions for Step-By-Step Directions From a Binary Tree Node to Another.
Memory Usage: 151.9 MB, less than 36.92% of Python3 online submissions for Step-By-Step Directions From a Binary Tree Node to Another.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def helper(root, acc):
            if root is None:
                return
            if root.val == startValue: d[startValue] = acc.copy()
            elif root.val == destValue: d[destValue] = acc.copy()
            if d[startValue] is not None and d[destValue] is not None:
                return
            acc.append('L')
            helper(root.left, acc)
            acc.pop()
            acc.append('R')
            helper(root.right, acc)
            acc.pop()
            return
        
        d = {startValue: None, destValue: None}
        helper(root, [])
        
        # Find Lowest common ancestor
        i = 0
        while i < len(d[startValue]) and i < len(d[destValue]) and d[startValue][i] == d[destValue][i]:
            i += 1
        if i == len(d[startValue]):
            path = ''.join(d[destValue][i:])
        elif i == len(d[destValue]):
            path = 'U' * len(d[startValue][i:])
        else:
            path = 'U' * len(d[startValue][i:])
            path += ''.join(d[destValue][i:])
        return path
            
        
        
        
            
            
            
            
                
            
            
            
            
            
            
            
        
            
            
            
                
                
                
                
                
            
    
        