#Leetcode - https://leetcode.com/problems/4sum/description/


#My appraoch
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = set()
        n = len(nums)
        tmp1 = {}

        for i, j in enumerate(nums):
            tmp1[j] = i
        
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    tmp  = target - (nums[i] + nums[j] + nums[k])

                    if tmp in tmp1 and tmp1[tmp] != i and tmp1[tmp] != j and tmp1[tmp] != k:
                        res.add(tuple(sorted([nums[i], nums[j], nums[k], nums[tmp1[tmp]]])))

        return [list(i) for i in res]


#Can be done better by sorting the entire array and then ....
