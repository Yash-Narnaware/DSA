#Leetcode - https://leetcode.com/problems/count-primes/description/

#Use Sieve of Eratosthenes

class Solution:
    def countPrimes(self, n: int) -> int:

        primes = [1]*n

        for i in range(2, int(n**0.5) + 1):
            tmp = i*i
            if primes[i] == 1:
                while tmp < n:

                    primes[tmp] = 0
                    tmp += i

        return sum(primes[2:])
