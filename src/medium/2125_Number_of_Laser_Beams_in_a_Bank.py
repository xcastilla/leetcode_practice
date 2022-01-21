"""
https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
Runtime: 86 ms, faster than 90.00% of Python3 online submissions for Number of Laser Beams in a Bank.
Memory Usage: 16.1 MB, less than 90.00% of Python3 online submissions for Number of Laser Beams in a Bank.
"""

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        devs = 0
        devs_last = bank[0].count("1")
        for i in range(1, len(bank)):
            devs_cur = bank[i].count("1")
            devs += devs_last * devs_cur
            if devs_cur != 0:
                devs_last = devs_cur
        return devs