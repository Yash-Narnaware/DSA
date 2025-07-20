#Leetcode - https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/


#My initial approach
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #Count nodes
        k = 0
        tmp = head
        while tmp:
            k += 1
            tmp = tmp.next

        from_strt = k - n

        #Edge case when we want to delete head
        if from_strt == 0:
            return head.next

        cnt = 0
        tmp = head
        while tmp:
            cnt += 1

            if cnt == from_strt:
                tmp.next = tmp.next.next
                break

            tmp = tmp.next

        return head 


#Optimal approach - in one pass. flow fast pointer n steps ahead and then move slow pointer from head and fast pointer from its position till fast reaches last node.
#Now slow is at prev node of the node we want to delete

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        tmp = head
        while n:
            tmp = tmp.next
            n -= 1

        if not tmp:
            return head.next
        slow = head

        while tmp.next:
            slow = slow.next
            tmp = tmp.next
        slow.next = slow.next.next

        return head

        

        
        

        
        
