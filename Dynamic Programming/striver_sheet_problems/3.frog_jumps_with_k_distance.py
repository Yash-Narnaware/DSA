#TUF - https://takeuforward.org/plus/dsa/problems/frog-jump-with-k-distances


class Solution:
    def frogJump(self, heights, k):

        mem = {}
        def func(n):

            if n not in mem:
                if n == 0:
                    mem[n] = 0

                else:
                    res = float('inf')
                    for i in range(1,k+1):
                        if n-i >= 0:
                            res = min(res,func(n-i) + abs(heights[n] - heights[n-i]))

                    mem[n] = res
            return mem[n]
        
        return func(len(heights)-1)
