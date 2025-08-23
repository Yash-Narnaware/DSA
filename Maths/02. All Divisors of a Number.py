#GFG - https://www.geeksforgeeks.org/problems/all-divisors-of-a-number/1

#from 2 to sqrt(N) add all divisors and their counterpart (N / divisor) if counterpart is not equal to divisor.

#User function Template for python3
import math
class Solution:
    def print_divisors(self, N):
        # code here
        tmp = []
        for i in range(1,int(math.sqrt(N)) + 1):
            if N % i == 0:
                # res.append(i)
                print(i, end = ' ')
                if N // i != i:
                    tmp.append(N // i)
                
        
        for i in range(len(tmp)-1, -1,-1):
            print(tmp[i], end=' ')
                
            
