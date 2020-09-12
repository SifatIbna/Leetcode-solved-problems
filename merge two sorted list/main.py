# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 is None and l2 is None:
            return None

        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        if l1.val > l2.val:

            ansNode = ListNode(l2.val)
            ansNode.next = self.mergeTwoLists(l1, l2.next)
            return ansNode
        else:
            ansNode = ListNode(l1.val)
            ansNode.next = self.mergeTwoLists(l1.next, l2)
            return ansNode