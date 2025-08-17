#TUF - https://takeuforward.org/plus/dsa/problems/number-of-distinct-substrings-in-a-string

#Trie is used to reduce the space complexity. oherwise this question can be done in O(n^2) with hashmap - generating all substrings and check if it is already seen.


#Add trie template here
#Here insert is returning 1 if while inserting a sub string we have to create a node. otherwise search the sub str in trie and if it is not present increase the count and add sub str in trie.
class Solution:
    def countDistinctSubstring(self, s):
        # Your code goes here

        trie = Trie()
    
        res = 1
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub_str = s[i:j+1]

                res += trie.insert(sub_str)
        return res
