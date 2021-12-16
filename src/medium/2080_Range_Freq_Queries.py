"""
https://leetcode.com/problems/range-frequency-queries/
Runtime: 1542 ms, faster than 77.96% of Python3 online submissions for Range Frequency Queries.
Memory Usage: 53.3 MB, less than 66.26% of Python3 online submissions for Range Frequency Queries.
"""

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.d = defaultdict(list)
        for i in range(len(arr)):
            self.d[arr[i]].append(i)
        

    def query(self, left: int, right: int, value: int) -> int:
        idxl = bisect.bisect_left(self.d[value], left)
        idxr = bisect.bisect(self.d[value], right)
        
        return idxr - idxl


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)