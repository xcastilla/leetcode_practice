
"""
https://leetcode.com/problems/two-out-of-three/
Runtime: 72 ms, faster than 57.44% of Python3 online submissions for Two Out of Three.
Memory Usage: 14.4 MB, less than 34.92% of Python3 online submissions for Two Out of Three.
"""
class Solution:
        def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
            f = defaultdict(int)
            for k in set(nums1):
                f[k] += 1
            for k in set(nums2):
                f[k] += 1
            for k in set(nums3):
                f[k] += 1
            return [k for k, v in f.items() if v >= 2]

 
"""
Runtime: 76 ms, faster than 37.26% of Python3 online submissions for Two Out of Three.
Memory Usage: 14.2 MB, less than 88.00% of Python3 online submissions for Two Out of Three.
"""

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        d3 = Counter(nums3)
        
        f = defaultdict(int)
        for k in d1.keys():
            f[k] += 1
        for k in d2.keys():
            f[k] += 1
        for k in d3.keys():
            f[k] += 1
        res = []
        for k, v in f.items():
            if v >= 2:
                res.append(k)
        return res
        