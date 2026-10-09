# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # I could go to end of the list, get the total len
        # Then I could run through it again and remove that node
        # Lets just do it and see if it works

        # Seems like we will need a base case
        if head.next is None:
            return None

        curr = head
        leng = 0
        while curr.next:
            leng +=1
            curr = curr.next
        # Add one more on for the length, this may cause issues we shall see
        leng += 1

        print("Length of linked list:", leng)
        # get the node to remove
        node_to_remove = leng - n

        # check if head needs to be removed
        if node_to_remove == 0:
            return head.next

        # Now we need to remove the node to remove next, if it exists
        curr = head
        while curr.next and node_to_remove != 1:
            curr = curr.next
            node_to_remove -= 1
        print("Val before node removed:", curr.val)

        # need to check two nodes ahead to see if it exists
        # if it does, then we set curr.next to that
        # else, we set curr.next to None
        if curr.next and curr.next.next:
            curr.next = curr.next.next
        else:
            curr.next = None

        return head


