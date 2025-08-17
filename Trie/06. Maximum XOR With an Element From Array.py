#Leetcode - https://leetcode.com/problems/maximum-xor-with-an-element-from-array/description/

#💀, use trie and sort queries according to limit and sort nums. while processing a query only add nums which are <= lim in trie and then find max XOR

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

        for j in range(31, -1, -1):
            bit = (num >> j) & 1

            if self.contains(tmp, 1 - bit):
                max1 = max1 | (1 << j) 
                tmp = self.get_ref_node(tmp, 1 - bit)
            
            else:
                tmp = self.get_ref_node(tmp, bit)
        
        return max1


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        trie = Trie()

        queries1 = [[queries[i][0], queries[i][1], i] for i in range(len(queries))]
        queries1.sort(key=lambda x: x[1])
        
        nums.sort()
        nums_idx = 0

        res = [-1]*len(queries1)
        for num, lim, idx in queries1:

            while nums_idx < len(nums) and nums[nums_idx] <= lim:
                trie.insert(nums[nums_idx])
                nums_idx += 1
            
            #Non empty trie
            if nums_idx != 0:
                res[idx] = trie.get_max_num(num)

        return res
        
