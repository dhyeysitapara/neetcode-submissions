# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:


        # Find the middle

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next


        # Reverse the second part

        prev = None

        while slow:

            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # Compare

        first = head
        second = prev

        while second:

            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True

        