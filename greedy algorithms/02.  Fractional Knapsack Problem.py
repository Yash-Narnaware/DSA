#GFG - https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1

#check val / weight ratio for each object and put items in bag according to it.

class Solution:
    def fractionalknapsack(self, val, wt, capacity):
        #put object with largest val / weight ratio
        
        tmp = []
        
        for i in range(len(val)):
            tmp.append([val[i] / wt[i], val[i], wt[i]])
            
        tmp.sort(reverse=True)
        res = 0
        for _, val, wt in tmp:
            if wt <= capacity:
                res += val
                capacity -= wt
            else:
                res += (capacity / wt)*val
                break
                
        
        return res
