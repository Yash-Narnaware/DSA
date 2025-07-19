#Leetcode - https://leetcode.com/problems/subarray-sum-equals-k/description/

#Use hashmap to count the sum frequencies while we calculate the prefix sum. at any index if we have prefix sum till that index - k in hashmap that means we found the required subarray and freq of pref_sum - k will be the number of arrays we found.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        #Sum - > freq
        map1 = {0: 1}

        res = 0
        sum1 = 0
        for i in nums:
            sum1 += i

            if sum1 - k in map1:
                res += map1[sum1 - k]

            if sum1 in map1:
                map1[sum1] += 1
            else:
                map1[sum1] = 1

        return res

        
