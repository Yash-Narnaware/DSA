#Leetcode - https://leetcode.com/problems/combination-sum-iii/description/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def func(n1, current_sum, current_arr, res):

            if current_sum > n or len(current_arr) > k:
                return 
            if n1 == 10:
                if current_sum == n and len(current_arr) == k:
                    res.append(current_arr[:])
                return
            
            #include
            current_arr.append(n1)
            func(n1 + 1, current_sum + n1, current_arr, res)
            current_arr.pop()

            #exclude
            func(n1 + 1, current_sum, current_arr, res)

        res = []
        func(1, 0, [], res)

        return res
