#Leetcode - https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp1 = l1
        tmp2 = l2

        dummy = ListNode()
        cur = dummy
        carry = 0

        while tmp1 and tmp2:
            newnode = ListNode()
            val = tmp1.val + tmp2.val + carry

            newnode.val = val % 10
            carry = val // 10
            
            cur.next = newnode
            cur = newnode

            tmp1 = tmp1.next
            tmp2 = tmp2.next

        while tmp1:
            newnode = ListNode()
            val = carry + tmp1.val
            newnode.val = val % 10
            carry = val // 10
            cur.next = newnode
            cur = newnode

            tmp1 = tmp1.next

        while tmp2:
            newnode = ListNode()
            val = carry + tmp2.val
            newnode.val = val % 10
            carry = val // 10
            cur.next = newnode
            cur = newnode

            tmp2 = tmp2.next

        if carry:
            cur.next = ListNode(1)

        return dummy.next





        
