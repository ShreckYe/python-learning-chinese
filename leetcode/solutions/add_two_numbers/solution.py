"""
Author: Shreck Ye
Date: June 12, 2019
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Creates a head node which will not be included in the final result
        l_head = ListNode(0)

        l = l_head
        carry_over = 0
        # "l1" in boolean expressions is equivalent to "l1 is not None". It's the same way for "l2"s.
        while l1 or l2 or carry_over:
            digit = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry_over
            if digit < 10:
                carry_over = 0
            else:
                digit -= 10
                carry_over = 1

            l.next = ListNode(digit)
            l = l.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return l_head.next


# Test cases
def toArrayList(l: ListNode):
    array_list = list()
    while l is not None:
        array_list.append(l.val)
        l = l.next
    return array_list


s = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print(toArrayList(s.addTwoNumbers(l1, l2)))

print(toArrayList(s.addTwoNumbers(ListNode(5), ListNode(5))))
