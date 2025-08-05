#Leetcode - https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

#To find kth largest element create a min heap and then only keep k elements in it(pop excess elements) that way at top of the heap is kth largest element. and for each new element add it to heap and if len of heap > k then pop element and return the top of the heap.

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
      
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        

    def add(self, val: int) -> int:
        
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
