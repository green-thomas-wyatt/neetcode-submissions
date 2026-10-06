# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # We need a temp node
        # if list 1 <= list 2, then temp = list1.next
        # list1.next = list2.head(current node)

        dummy = ListNode(0)
        tail = dummy

        while list1 is not None and list2 is not None:
            # If list1 is smaller
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            # if list 2 is smaller
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # We now need to deal with the rest
        tail.next = list1 if list1 else list2
            
        
        return dummy.next