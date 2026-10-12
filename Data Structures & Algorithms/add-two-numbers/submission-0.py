# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # make a new list?
        head = ListNode(0)
        curr_fin = head
        curr1 = l1
        curr2 = l2
        carry = 0
        # While either node or a leftover carry value
        while curr1 or curr2 or carry:
            # We need a check to make sure curr1/curr2 have a value
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            total = val1 + val2 + carry
            curr_fin.next = ListNode(total % 10)
            curr_fin = curr_fin.next
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
            carry = total // 10
        return head.next

        # We will need to deal with the second example
        # We need to use a carry value?
        # We can keep modding it by ten