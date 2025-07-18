#Leetcode - https://leetcode.com/problems/3sum/description/

#Used hashmap - better appraoch possible.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        map = {}
        res = set()
     
        for i,num in enumerate(nums):
            map[num] = i

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                target = -nums[i] - nums[j]

                if target in map:
                    if map[target] != i and map[target] != j:

                        res.add(tuple(sorted([nums[i],nums[j],target])))

        return list(res)
        
