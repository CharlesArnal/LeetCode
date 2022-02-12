# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        starting_head = head
        head1 = head
        head2 = head
        
        for i in range(n-1):
            head2 = head2.next
        # n-1 steps of distance
        if head2.next == None:
            if head1 == head2:
                return None
            else:
                return head1.next
        # n steps of distance
        head2 = head2.next
        while head2.next != None:
            head2 = head2.next
            head1 = head1.next
        head1.next = head1.next.next
        return starting_head
        
        