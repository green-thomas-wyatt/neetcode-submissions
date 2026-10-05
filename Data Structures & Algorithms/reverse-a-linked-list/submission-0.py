# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## hmmmm how to do this
        # how to reverse two nodes
        # store the previous val in a temp node
        # set self.next to temp
        # 

        #[0,1]
        # [1,]


        # Three pointers
        # prev
        # curr
        # temp/next node

        # Save upcoming node
        # reverse current nodes pointer
        # Move pointers forward

        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

