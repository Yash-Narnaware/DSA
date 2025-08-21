#Leetcode - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/

#My approach - since xor is 1 if the bits are different therefore xor start and goal and then count set bits

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        flips = 0
        diff = start ^ goal

        while diff > 0:
            flips += diff & 1
            diff = diff >> 1
        return flips
