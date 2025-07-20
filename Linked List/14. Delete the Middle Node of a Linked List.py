#Leetcode - https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/

#Find middle also keep track of prev pointer to slow pointer because thats the node we have to alter

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head.next:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = prev.next.next

        return head
        
