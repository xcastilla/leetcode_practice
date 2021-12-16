"""
https://leetcode.com/problems/watering-plants/
Runtime: 48 ms, faster than 85.28% of Python3 online submissions for Watering Plants.
Memory Usage: 14.4 MB, less than 77.94% of Python3 online submissions for Watering Plants.
"""

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cost = 0
        rem = capacity
        for i in range(len(plants)):
            rem -= plants[i]
            if i < len(plants) - 1 and plants[i + 1] > rem:
                cost += 2 * i + 3
                rem = capacity
            else:
                cost += 1
        return cost
        