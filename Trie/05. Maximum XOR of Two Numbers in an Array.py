#Leetcode - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/

#1st bit problem - too many new things - bits. use trie to store the numbers in bit format.
#Get max num function gives the max number possible for a given number with all other array elements.
class Node:

    def __init__(self):
        self.ref = [None]*2
        self.terminal = False

class Trie:

    def __init__(self):
        self.root = Node()

    def contains(self, node, bit):
        return node.ref[bit] != None

    def add_ref(self, node1, bit, node):
        node1.ref[bit] = node

    def get_ref_node(self, node, bit):
        return node.ref[bit]

    def set_terminal(self, node):
        node.terminal = True
    
    def is_terminal(self, node):
        return node.terminal
        

    def insert(self, word: int) -> None:
        tmp = self.root

        for i in range(31, -1, -1):
            bit = (word >> i) & 1

            if not self.contains(tmp, bit):
                self.add_ref(tmp, bit, Node())
            tmp = self.get_ref_node(tmp, bit)

        self.set_terminal(tmp)

    def get_max_num(self, num):

        tmp = self.root
        max1 = 0

        for i in range(31, -1, -1):
            bit = (num >> i) & 1

            if self.contains(tmp, 1 - bit):
                max1 = max1 | (1 << i) 
                tmp = self.get_ref_node(tmp, 1 - bit)
            
            else:
                tmp = self.get_ref_node(tmp, bit)
        
        return max1


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        trie = Trie()

        for i in nums:
            trie.insert(i)

        res = 0

        for i in nums:
            res = max(res, trie.get_max_num(i))
        return res

        
