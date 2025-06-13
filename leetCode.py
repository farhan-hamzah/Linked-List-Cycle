# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next         # bergerak satu langkah
            fast = fast.next.next    # bergerak dua langkah

            if slow == fast:
                return True          # ada siklus

        return False                 # tidak ada siklus
