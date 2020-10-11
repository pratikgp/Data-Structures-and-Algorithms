# https://leetcode.com/problems/rotate-list/ | Medium

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # base cases
        if head is None:
            return None
        if head.next is None:
            return head
        
        # close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next is not None:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head
        
        # find new tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        new_tail = head
        for _ in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # break the ring
        new_tail.next = None
        
        return new_head

# Complexity Analysis
# Time complexity: O(N) where N is a number of elements in the list
# Space complexity: O(1) since it's a constant space solution