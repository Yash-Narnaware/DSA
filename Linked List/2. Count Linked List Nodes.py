#GFG - https://www.geeksforgeeks.org/problems/count-nodes-of-linked-list/1

#Iterative way
'''
#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        '''
class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):

        cur = head
        cnt = 0
        while cur:
            cnt += 1
            cur = cur.next
        
        return cnt


#Recursive way
'''
#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        '''
class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):

        def func(node, cnt):
            if not node:
                return cnt
                
            return func(node.next, cnt + 1)
            
        return func(head, 0)
            
