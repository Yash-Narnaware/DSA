#GFG = https://www.geeksforgeeks.org/problems/find-xor-of-numbers-from-l-to-r/1

#just observe the pattern for xor till n from 1 depending upon n % 4 values. and for xor from l to r - calculate xor from 1to r then xor it with xor from 1 to l-1.

class Solution:
    def findXOR(self, l, r):
     
        #function to get xor value from 1 to n
        def func(n):
            
            if n % 4 == 1:
                return 1
            if n % 4 == 2:
                return n + 1
            if n % 4 == 3:
                return 0
            if n % 4 == 0:
                return n
                
        return func(r) ^ func(l-1)
