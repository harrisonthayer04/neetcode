from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Find the final node
        nodes_list = []
        node = head
        while node.next:
            nodes_list.append(node)
            node = node.next
        nodes_list.append(node)
        # Start to reverse the order

        for i in range(len(nodes_list)-1, -1, -1):
            nodes_list[i].next = nodes_list[i-1].next

Node3 = ListNode(3)
Node2 = ListNode(2, Node3)       
Node1 = ListNode(1, Node2)


mySolution =  Solution().reverseList(Node1)
