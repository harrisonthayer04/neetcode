# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]):
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        result = 0
        while slow:
            result = max(result, prev.val+slow.val)
            prev = prev.next
            slow = slow.next
        return result



# One loop over the list nodes to find len(list)
# Loop over the list nodes calculating the twin sums and storing
# the largest value in a variable

# 5 -> 8 -> 9 
# 10 <- 4 -> 2 -> 1 -> 3 -> 10
# ^     ^    ^
# len(ll) = 6
# First half 0 -> (n/2) - 1
# Second half (n/2) -> n - 1
# [5 + 2, 8 + 4, 9 + 10]


# First half 0 -> (n/2) - 1  (first list)
# Second half (n/2) -> n - 1 (second list)
# 5 -> 8 -> 9 
# 10 <- 4 <- 2
# 0.   1.   2.   3.    4.   5
# 5 -> 8 -> 9
# 2 -> 4 -> 10