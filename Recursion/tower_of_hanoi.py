#GFG - https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1

#IMPORTANT PROBLEM 
#Think if we want the number of steps for n then how can we break this problem for n-1 disks.
# if problem is n disks from, to using helper then we can break it to - n-1 disks from, to helper using to then n-1 disks from helper, to to using from

class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):

        def hanoi(n,fromm,to,aux,count):
            if n == 0:
                return 
    
            hanoi(n-1, fromm, aux, to,count)
            count[0] += 1
            hanoi(n-1, aux, to, fromm,count)
            

            
        count = [0]
        hanoi(n,fromm,to,aux,count)
        
        return count[0]
