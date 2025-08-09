#GFG - https://www.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1

class Solution:
    def minPartition(self, N):
 
        coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        res = []
        
        for i in range(len(coins) - 1, -1, -1):
            while N >= coins[i]:
                res.append(coins[i])
                N -= coins[i]
                
        return res
                
