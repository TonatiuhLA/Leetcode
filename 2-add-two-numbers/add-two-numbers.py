# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sm = self.recurr(l1, 1) + self.recurr(l2, 1)
        st = str(sm)
        leng = len(st)-1
        head = ListNode(int(st[leng]))
        curr = head

        for i in range(leng-1, -1, -1):
            curr.next = ListNode(int(st[i]))
            curr = curr.next

        return head
    
    def recurr(self, head, num):
        if head:
            return (head.val * num) + self.recurr(head.next, (num * 10))
        else:
            return 0
