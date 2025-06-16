#GFG - https://www.geeksforgeeks.org/problems/partitions-with-given-difference/1

#partition array s.t. difference of sum of element in this 2 partitions is equal to d.


#Same as #20 just little change in base condition and return statement

#Also can be done by solving equations - sum1 - sum2 = d and sum1 + sum2 = sum(arr). Derive value for sum1 from it and now it is count of subset sum problem. Have to count the number of subsets whose sum is this target sum.


#Recursive approach

from typing import List
class Solution:
    def countPartitions(self, arr, d):

        sum2 = sum(arr)
        
        def func(sum1,n):
            
            if n == 0:
                if (2*sum1 - sum2) == d:
                    return 1
                else:
                    return 0
                    
            return func(sum1 + arr[n-1],n-1) + func(sum1,n-1)
            
        return func(0,len(arr))
        



#Memoization - Top down

from typing import List
class Solution:
    def countPartitions(self, arr, d):

        sum2 = sum(arr)
        mem = {}
        def func(sum1,n):
            
            if (sum1,n) not in mem:
                if n == 0:
                    if (2*sum1 - sum2) == d:
                        mem[(sum1,n)] = 1
                    else:
                        mem[(sum1,n)] = 0
                else:        
                    mem[(sum1,n)] = func(sum1 + arr[n-1],n-1) + func(sum1,n-1)
            
            return mem[(sum1,n)]
            
        return func(0,len(arr))
        


#Tabulation - Bottom up
#TBD
