#Leetcode - https://leetcode.com/problems/online-stock-span/description/

#It is finding previous element problem just store the indices along with value in stack to calculate the number of elements.

class StockSpanner:

    def __init__(self):
        self.stack = []
        self.idx = 0
        

    def next(self, price: int) -> int:
        
        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()

        if self.stack:
            res = self.idx - self.stack[-1][1]
        else:
            res = self.idx + 1
            
        self.stack.append((price, self.idx))
        self.idx += 1
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
