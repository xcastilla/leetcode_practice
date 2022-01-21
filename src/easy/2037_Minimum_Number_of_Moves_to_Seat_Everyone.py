"""
https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone
Runtime: 60 ms, faster than 81.51% of Python3 online submissions for Minimum Number of Moves to Seat Everyone.
Memory Usage: 14.1 MB, less than 82.93% of Python3 online submissions for Minimum Number of Moves to Seat Everyone.
"""

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        tot = 0
        for i in range(len(seats)):
            tot += abs(seats[i] - students[i])
        return tot