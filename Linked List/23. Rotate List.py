#Leetcode - https://leetcode.com/problems/rotate-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        ll_len = 1
        tail1 = head

        while tail1.next:
            ll_len += 1
            tail1 = tail1.next
        
        eff_rot = k % ll_len

        if eff_rot == 0:
            return head
        
        tail = head
        idx = 1

        while idx != ll_len - eff_rot:
            tail = tail.next
            idx += 1
        
        nxt = tail.next
        tail.next = None
        tail1.next = head

        return nxt
        
