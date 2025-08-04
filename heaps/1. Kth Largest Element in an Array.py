#Leetcode - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        max_hp = [-i for i in nums]
        heapq.heapify(max_hp)

        for i in range(k-1):
            heapq.heappop(max_hp)
        return -max_hp[0]

        
