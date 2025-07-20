#Leetcode - https://leetcode.com/problems/palindrome-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head.next:
            return True
        
        #Finding the middle of LL
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Even/ odd elements checking
        if fast:
            cur = slow.next
        else:
            cur = slow

        #Reverse the LL
        prev = None
        nxt = cur.next

        while nxt:
            cur.next = prev
            prev = cur
            cur = nxt
            nxt = nxt.next
        cur.next = prev

        #Check the palindrome
        tmp = head
        while tmp and cur:
            if tmp.val != cur.val:
                return False
            tmp = tmp.next
            cur = cur.next
        return True


        
