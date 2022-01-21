"""
https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/
Runtime: 4889 ms, faster than 63.50% of Python3 online submissions for Minimize the Difference Between Target and Chosen Elements.
Memory Usage: 14.5 MB, less than 90.15% of Python3 online submissions for Minimize the Difference Between Target and Chosen Elements.
"""

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        t = sorted(mat[0])
        for i in range(1, len(mat)):
            new_t = set()
            for n in mat[i]:
                for el in t:
                    new_t.add(el + n)
                    if el + n >= target:
                        break
            t = sorted(list(new_t))
        return min([abs(target - el) for el in t])