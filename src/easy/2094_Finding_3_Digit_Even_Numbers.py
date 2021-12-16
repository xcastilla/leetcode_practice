"""
https://leetcode.com/problems/finding-3-digit-even-numbers/
Runtime: 68 ms, faster than 88.89% of Python3 online submissions for Finding 3-Digit Even Numbers.
Memory Usage: 14.3 MB, less than 66.67% of Python3 online submissions for Finding 3-Digit Even Numbers.
"""

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        def helper(ct, rem):
            if rem == 0:
                return [str(k) for k, v in ct.items() if v > 0 and k % 2 == 0]
            res = []
            for k, v in ct.items():
                if (rem == 2 and k == 0) or v <= 0:
                    continue
                cp_ct = ct.copy()
                cp_ct[k] -= 1
                ret_rec = helper(cp_ct, rem - 1)
                for r in ret_rec:
                    res.append(str(k) + r)
                cp_ct = None
            return res
 
        dic = Counter(digits)
        ret = helper(dic, 2)
        ret = sorted(map(int, ret))
        return ret
