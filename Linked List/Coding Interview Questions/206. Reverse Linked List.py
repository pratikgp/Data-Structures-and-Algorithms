# https://leetcode.com/problems/reverse-linked-list/ | Easy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while (curr != None):
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev
    
    
    '''
        curr = head
        reverse = None
        while curr != None:
                second = curr.next
                curr.next = reverse
                reverse = curr
                curr = second
        return reverse
    '''

# Complexity analysis
# Time complexity : O(n) Assume that n is the list's length, the time complexity is O(n).
# Space complexity : O(1)