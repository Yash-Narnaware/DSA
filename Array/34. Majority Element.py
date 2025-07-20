#Leetcode - https://leetcode.com/problems/majority-element/description/

#Moore's voting algorithm
#Coube be solved using sorting and then returning the nid element.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        cur = nums[0]
        cnt = 0

        for i, j in enumerate(nums):
            if cnt == 0:
                cur = j
            if j == cur:
                cnt += 1
            else:
                cnt -= 1
        return cur
        
