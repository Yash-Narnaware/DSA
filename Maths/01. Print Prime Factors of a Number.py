#GFG - https://www.geeksforgeeks.org/problems/prime-factors5052/1

#any factor of number n prime or not will come before sqrt(n). so start from 2 till sqrt(n) if current n % num == 0 then keep dividing n by num till remainder is 0 that way we removed all the duplicate non-prime factors from n which are multiple of num then add num to factors list and move on to next factor.

#Edge-case - if n have prime factor > sqrt(n) then after loop check if remaining n is 1 or not if not then add n to factors list.

class Solution:
    def primeFac(self, n):
        # code here
        N = n
        res = []
        for i in range(2, int(n**0.5)+1):
            
            if n % i == 0:
                res.append(i)
                while n % i == 0:
                    n = n / i
                    
        if n != 1:
            res.append(int(n))
            
        return res
                    
        
        
