#GFG - https://www.geeksforgeeks.org/problems/shortest-job-first/1

#Sort the array and keep track of delays till now and update the dalay after current process is done(i.e. sum the current process time to delay)

class Solution:
    def solve(self, bt):

        bt.sort()
        delay = 0
        sum_of_delays = 0
        
        for i in range(1, len(bt)):
            
            delay += bt[i-1]
            sum_of_delays += delay
            
        return sum_of_delays // len(bt)
