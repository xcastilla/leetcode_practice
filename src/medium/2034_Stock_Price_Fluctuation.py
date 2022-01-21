"""
https://leetcode.com/problems/stock-price-fluctuation
Runtime: 784 ms, faster than 88.58% of Python3 online submissions for Stock Price Fluctuation .
Memory Usage: 62.5 MB, less than 19.69% of Python3 online submissions for Stock Price Fluctuation .
"""

class StockPrice:

    def __init__(self):
        self.max_h = []
        self.min_h = []
        self.d = {}
        self.latest_t = 0
        
    def update(self, timestamp: int, price: int) -> None:            
        self.d[timestamp] = price
        heapq.heappush(self.max_h, (-price, timestamp))
        heapq.heappush(self.min_h, (price, timestamp))
        self.latest_t = max(self.latest_t, timestamp)

    def current(self) -> int:
        return self.d[self.latest_t]

    def maximum(self) -> int:
        el = self.max_h[0]
        if -el[0] != self.d[el[1]]:
            heapq.heappop(self.max_h)
            return self.maximum()
        return -el[0]
            
    def minimum(self) -> int:
        el = self.min_h[0]
        if el[0] != self.d[el[1]]:
            heapq.heappop(self.min_h)
            return self.minimum()
        return el[0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()