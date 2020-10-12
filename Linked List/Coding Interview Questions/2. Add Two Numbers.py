# https://leetcode.com/problems/add-two-numbers/ | Medium

import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        p = l1
        q = l2
        curr = dummyHead
        carry = 0
        while p != None or q != None:
            if p != None:
                x = p.val
            else:
                x = 0
            if (q != None):
                y = q.val
            else:
                y = 0
            sum = carry + x + y
            carry = math.floor(sum / 10)
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if (p != None):
                p = p.next
            if (q != None):
                q = q.next
        if (carry > 0):
            curr.next = ListNode(carry)
        return dummyHead.next
        
# Complexity Analysis
# Time complexity : O(max(m,n)). Assume that m and n represents the length of l1 and l2 respectively, the algorithm above iterates at most max(m,n) times.
# Space complexity : O(max(m,n)). The length of the new list is at most max(m,n) + 1.

           