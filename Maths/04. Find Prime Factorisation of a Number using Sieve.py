#TUF - https://takeuforward.org/plus/dsa/problems/prime-factorisation-of-a-number

#use Sieve of Eratosthenes like approach but at each index store the lowest prime factor. and while processing queries find lpf of number add it in prime factorization of that number and then update the number by dividing it by lfp and do it till lpf != number.

class Solution:
    def primeFactors(self, queries):
        #your code goes here

        max_num = max(queries)
        lowest_prime_factor = [i for i in range(max_num + 1)]

        for i in range(2, max_num + 1):
            if lowest_prime_factor[i] == i:

                for j in range(i*i, max_num+1, i):
                    if lowest_prime_factor[j] == j:
                        lowest_prime_factor[j] = i


        res = []
        for i in queries:
            num = i
            tmp = []
            while lowest_prime_factor[num] != num:
                tmp.append(lowest_prime_factor[num])
                num = num // lowest_prime_factor[num]

            tmp.append(num)
            res.append(tmp)

        return res
