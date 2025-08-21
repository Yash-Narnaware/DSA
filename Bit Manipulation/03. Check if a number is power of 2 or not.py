#Leetcode - https://leetcode.com/problems/power-of-two/

#Approach 1: check every bit and there should be only 1 set bit
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n < 0:
            return False
        found = False

        for i in range(32):
            if n >> i & 1 == 1:
                if found:
                    return False
                found = True
        return found


#Approach2: we know there should be only 1 set bit in n and if we & n with n - 1 it would remove the rightmost set bit so after this operation if result is 0 then we got power of two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False
        return n & (n - 1) == 0

        
