# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None or head.next is None:
            return None

        p1 = head
        p2 = head
        prev = head

        while p2 and p2.next:
            prev = p1
            p1 = p1.next
            p2 = p2.next.next
        
        prev.next = p1.next
        return head
        



# Solution
# count the nodes
# calculate the middle node,
# and then remove the middle node

# input = 
# [1,3,4,7,1,2,6,4,4,3,2,4,5,6,7,8,9]
#                  ^
#                                  ^
# len(input) = 17 // 2 = 8
# pointer_1 = 8
# pointer_2 = 16
# O(n/2)

#               *  
# head = [1,2,3,4,5,6]
#             ^
#                   ^

# head = [2,1]
# p1.     ^
# p2.     ^