#GFG - https://www.geeksforgeeks.org/problems/longest-valid-word-with-all-prefixes/1

#Store all words in Trie and then if the ref node is terminal then only go to that node and maintain the max pref string

#Add trie template here
class Solution:
    def longestValidWord(self, words):
        # code here 
        
        trie = Trie()
        
        for i in words:
            trie.insert(i)
            
        
        def func(node, cur, max1):
            
            
            for j, i in enumerate(node.ref):
                if i and i.terminal:
                    new_str = cur + chr(ord('a') + j)
                    
                    if len(new_str) > len(max1[0]):
                        max1[0] = new_str
                    func(i, new_str, max1)
                    
                    
        res = []
        max1 = ['']
        func(trie.root, '', max1)
        
        return max1[0]
