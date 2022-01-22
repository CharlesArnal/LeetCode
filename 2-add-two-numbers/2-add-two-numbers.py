# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        firstNode = ListNode()
        currentNode = firstNode
        retenue = 0
        next1 = l1
        next2 = l2
        while next1!= None or next2!=None or retenue!=0:
            v1 = (0 if next1== None else next1.val )
            v2 = (0 if next2== None else next2.val )
            currentNode.val = (v1 + v2 + retenue)%10
            retenue = (1 if v1 + v2 + retenue >9 else 0)
            if next1!=None:
                next1 = next1.next
            if next2!=None:
                next2 = next2.next
            if next1!= None or next2!=None or retenue!=0:
                newNode = ListNode()
                currentNode.next = newNode
                currentNode = newNode
        return firstNode
                
