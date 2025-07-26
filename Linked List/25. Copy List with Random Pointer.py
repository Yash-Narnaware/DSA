#Leetcode - https://leetcode.com/problems/copy-list-with-random-pointer/description/

#Used array and hashmap. hashmap to store the index of original nodes. also store the original nodes in copied nodes and then later we can change them to copied version of them using hashmap.

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return head
            
        ll = []
        mp = {}

        idx = 0
        while head:
            mp[head] = idx
            idx += 1

            n = Node(head.val)
            n.next = head.next
            n.random = head.random
            ll.append(n)

            head = head.next
        
        for i in range(len(ll)-1):
            ll[i].next = ll[i+1]
            if ll[i].random != None:
                ll[i].random = ll[mp[ll[i].random]]
        
        if ll[-1].random != None:
            ll[-1].random = ll[mp[ll[-1].random]]

        return ll[0]

        
