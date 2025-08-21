#GFG - https://www.geeksforgeeks.org/problems/swap-two-numbers3844/1

#XOR of two numbers store the difference between 2 numbers(XOR bit is 1 if bits are different in a and b)

class Solution:
    def get(self, a: int, b: int) -> tuple[int, int]:

        a = a ^ b
        b = b ^ a
        a = a ^ b
        
        return (a, b)
