#TUF - https://takeuforward.org/plus/dsa/problems/count-all-subsequences-with-sum-k


class Solution:
    def countSubsequenceWithTargetSum(self, nums, k):

        n = len(nums)
        def func(n1, current_sum):

            if n1 == n:
                if current_sum == k:
                    return 1
                else:
                    return 0

            r1 = func(n1 + 1, current_sum + nums[n1])
            r2 = func(n1 + 1, current_sum)

            return r1 + r2

        return func(0, 0)
