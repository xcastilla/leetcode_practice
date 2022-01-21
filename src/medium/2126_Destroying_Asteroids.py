"""
https://leetcode.com/problems/destroying-asteroids/
Runtime: 1324 ms, faster than 63.16% of Python3 online submissions for Destroying Asteroids.
Memory Usage: 27.9 MB, less than 94.74% of Python3 online submissions for Destroying Asteroids.
"""

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids = sorted(asteroids)
        while len(asteroids):
            if mass < asteroids[0]:
                return False
            p = bisect.bisect_right(asteroids, mass)
            mass += sum(asteroids[0:p])
            asteroids = asteroids[p:]
        return True