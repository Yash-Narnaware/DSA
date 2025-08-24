#Leetcode - https://leetcode.com/problems/max-consecutive-ones-iii/description/

#Expand till possible with flipping the zeros then shrink from left till we can flip 1 zero again and then again expand.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        start = 0
        end = 0
        res = 0
        while end < len(nums):

            if nums[end] == 0:
                if k > 0:
                    k -= 1
                else:
                    res = max(res, end - start)
                    while k == 0:
                        if nums[start] == 0:
                            k += 1
                        start += 1
                    end -= 1

            end += 1

        res = max(res, end - start)

        return res
