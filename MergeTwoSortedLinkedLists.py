from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next

# Alternative solution:
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        l1 = list1
        l2 = list2

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 if l1 else l2
        return dummy.next
    


# Test 1: Both lists are empty
list1 = None
list2 = None
result = Solution().mergeTwoLists(list1, list2)
print("Test 1 (Both empty):", result)  # Expected: None

# Test 2: One list is empty, one is not
nodeA = ListNode(1)
list1 = nodeA
list2 = None
result = Solution().mergeTwoLists(list1, list2)
print("Test 2 (One empty):", result.val if result else None)  # Expected: 1

# Test 3: Both lists have multiple elements
# list1: 1 -> 3
# list2: 2 -> 4
node1 = ListNode(1, ListNode(3))
node2 = ListNode(2, ListNode(4))
result = Solution().mergeTwoLists(node1, node2)
# Print merged list
merged_vals = []
while result:
    merged_vals.append(result.val)
    result = result.next
print("Test 3 (Both non-empty):", merged_vals)  # Expected: [1,2,3,4]
