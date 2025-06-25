#Leetcode - https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        n = len(candidates)
        def func(n1, current_sum, current_arr, res):

            if current_sum > target or n1 == n:
                return
            if current_sum == target:
                res.append(current_arr[:])
                return

            #include
            current_arr.append(candidates[n1])
            func(n1, current_sum + candidates[n1], current_arr, res)
            current_arr.pop()

            #exclude
            func(n1 + 1, current_sum, current_arr, res)

        res = []
        func(0, 0, [], res)

        return res
        
