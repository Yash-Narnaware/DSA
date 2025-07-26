#Leetcode - https://leetcode.com/problems/intersection-of-two-linked-lists/description/


#Approach 1 - use set to store the seen nodes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        seen = set()

        while headA and headB:
            if headA == headB:
                return headA
            if headA in seen:
                return headA
            if headB in seen:
                return headB
            seen.add(headA)
            seen.add(headB)
            headA = headA.next
            headB = headB.next

        while headA:
            if headA in seen:
                return headA
            headA = headA.next
        while headB:
            if headB in seen:
                return headB
            headB = headB.next

        return None


#Approach 2: calculate the lenght of both lists and align their lenght(move pointer of big node so that both lists have same number of nodes) and then traverse together

#Appraoch 3: traverse both nodes simultaneously and if we reach end of one list set that pointer to head of another list. do it till both pointers are equal.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        tmp1 = headA
        tmp2 = headB

        while tmp1 != tmp2:
            if tmp1 == None:
                tmp1 = headB
            else:
                tmp1 = tmp1.next
            if tmp2 == None:
                tmp2 = headA
            else:
                tmp2 = tmp2.next
            
        return tmp1
        
