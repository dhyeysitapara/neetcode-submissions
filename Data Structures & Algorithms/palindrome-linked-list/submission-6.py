# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        #Find middle

        slow = head
        fast = head
        

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        
        #Reverse the second half including middle

        current = slow
        prev = None

        while current:
            
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt


        #Compare

        first = head
        second = prev


        while second:

            if first.val != second.val:

                return False

            else:
                first = first.next
                second = second.next

        return True
        