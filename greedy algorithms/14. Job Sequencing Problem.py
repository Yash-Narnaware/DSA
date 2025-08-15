#GFG - https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1

#Solved using greedy approach - created the time slots array and sort the profits in reverse order and iterate through it and place it in first available slot left to it.
#Have to optimize using DSU


class Solution:
    def jobSequencing(self, deadline, profit):
    
        comb = [[profit[i], deadline[i]] for i in range(len(profit))]
        comb.sort(reverse=True, key=lambda x: x[0])
        
        time_slots = [-1]*(max(deadline)+1)
        res = [0, 0]
        
        for prof, ddl in comb:
            temp = ddl
            while temp > 0 and time_slots[temp] != -1:
                temp -= 1
            if temp != 0:
                res[0] += 1
                res[1] += prof
                time_slots[temp] = 0
                
        return res
                
            
        
        
