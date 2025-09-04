#Leetcode - https://leetcode.com/problems/subarrays-with-k-different-integers/description/

#got TLE using brute force. then applied logic of exactly k distinct element sub array = atmost k distinct subarrays - atmost k-1 distinct subarrays.

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
      
        def func(k):
            freq = {}
            start = 0
            end = 0
            res = 0

            while end < len(nums):

                if nums[end] in freq:
                    freq[nums[end]] += 1
                else:
                    freq[nums[end]] = 1

                while len(freq) > k:
                    freq[nums[start]] -= 1
                    if freq[nums[start]] == 0:
                        del freq[nums[start]]
                    start += 1
                
                #Number of sub-arrays ending with nums[end]
                res += end - start + 1

                end += 1

            return res

        return func(k) - func(k - 1)
        
