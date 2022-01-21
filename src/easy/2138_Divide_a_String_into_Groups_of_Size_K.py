"""
https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
Runtime: 42 ms, faster than 63.30% of Python3 online submissions for Divide a String Into Groups of Size k.
Memory Usage: 14.4 MB, less than 22.30% of Python3 online submissions for Divide a String Into Groups of Size k.
"""

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ret = [s[i:i+k] for i in range(0, len(s), k)]
        if len(ret[-1]) < k:
            ret[-1] += fill * (k - len(ret[-1]))
        return ret