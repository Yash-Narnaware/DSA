#Leetcode - https://leetcode.com/problems/subsets-ii/description/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)

        def func(n1, current_arr, res):

            if n1 == n:
                res.add(tuple(current_arr[:]))
                return

            #include
            current_arr.append(nums[n1])
            func(n1 + 1, current_arr, res)
            current_arr.pop()

            #exclude
            func(n1 + 1, current_arr, res)

        res = set()
        func(0, [], res)

        return list(res)
        
