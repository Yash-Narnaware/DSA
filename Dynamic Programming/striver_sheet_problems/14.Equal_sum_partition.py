#Leetcode - https://leetcode.com/problems/partition-equal-subset-sum/


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        target = sum(nums)
        if target % 2 == 1:
            return False
        
        mem = {}
        def func(sum1,n):
            
            if (sum1,n) not in mem:
 
                if sum1 == 0:
                    mem[(sum1,n)] = True
                elif sum1 < 0 or n == 0:
                        mem[(sum1,n)] = False
                else:        
                
                    mem[(sum1,n)] = func(sum1 - nums[n-1], n-1) or func(sum1,n-1)
                    
            return mem[(sum1,n)]
                
        return func(target//2, len(nums))
        
