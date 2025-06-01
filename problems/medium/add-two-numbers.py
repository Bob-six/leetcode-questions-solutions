from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumberWrapper(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        carry = 0

        if l1 is not None and l2 is not None:
            base_sum = l1.val + l2.val

            previous_sums = self.addTwoNumberWrapper(l1.next, l2.next)

            base_sum += previous_sums[1]

            if base_sum >= 10:
                base_sum -= 10
                carry = 1

            return [base_sum, *previous_sums[0]], carry

        if l1 is None and l2 is not None:
            base_sum = l2.val
            previous_sums = self.addTwoNumberWrapper(l1, l2.next)

            return [base_sum, *previous_sums[0]], carry

        if l2 is None and l1 is not None:
            base_sum = l1.val
            previous_sums = self.addTwoNumberWrapper(l1.next, l2)

            return [base_sum, *previous_sums[0]], carry

        return [], 0

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):

        sum, carry = self.addTwoNumberWrapper(l1, l2)

        if carry > 0:
            sum = [1, *sum]

        return sum
