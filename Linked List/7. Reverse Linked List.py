#Leetcode - https://leetcode.com/problems/reverse-linked-list/description/

#Iterative way
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        prev = None
        cur = head
        nxt = cur.next

        while nxt:
            cur.next = prev
            prev = cur
            cur = nxt
            nxt = nxt.next

        cur.next = prev
        return cur

#Recursive way

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def rev(cur, prev, nxt):
            if not nxt:
                cur.next = prev
                return cur

            cur.next = prev
            prev = cur
            cur = nxt

            return rev(cur, prev, nxt.next)

        return None if not head else rev(head, None, head.next)

            

        
