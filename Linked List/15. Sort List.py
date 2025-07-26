#Leetcode - https://leetcode.com/problems/sort-list/description/

#Use merge sort, insertion sort can also be used but in our case it was giving TLE.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge(head1, head2):
            head = ListNode()
            cur = head
            while head1 and head2:
                if head1.val <= head2.val:
                    cur.next = head1
                    head1 = head1.next
                else:
                    cur.next = head2
                    head2 = head2.next
                cur = cur.next

            while head1:
                cur.next = head1
                head1 = head1.next
                cur = cur.next
            while head2:
                cur.next = head2
                head2 = head2.next
                cur = cur.next

            return head.next

        def merge_sort(node):

            if not node or node.next == None:
                return node

            slow = node
            fast = node.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            tmp = slow.next
            slow.next = None
            
            r1 = merge_sort(node)
            r2 = merge_sort(tmp)

            return merge(r1, r2)
        return merge_sort(head)
                
        
