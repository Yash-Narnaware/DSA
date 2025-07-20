#GFG - https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1

'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''
class Solution:
    def reverseDLL(self, head):
        #return head of reverse doubly linked list
        prev = None
        while head:
            head.next, head.prev = head.prev, head.next
            prev = head
            head = head.prev
        
        return prev
