# Definition for singly-linked list.

#v1: 100ms ~ 180ms with 13MB

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        sum = l1.val + l2.val
        result = ListNode(sum % 10)
        carry_bite = int(sum / 10)

        result_pre = result
        l1_current = l1.next
        l2_current = l2.next

        while l1_current and l2_current:
            l1_current, l2_current, result_pre, carry_bite = self._calculate_node(l1_current, l2_current, result_pre, carry_bite)

        if l1_current is None and l2_current is None:
            if carry_bite == 1:
                result_pre.next = ListNode(1)
            return result

        longer_node = l2_current if l1_current is None else l1_current

        while carry_bite:
            sum = carry_bite + longer_node.val
            result_pre.next = ListNode(sum % 10)
            carry_bite = int(sum / 10)
            longer_node = longer_node.next
            result_pre = result_pre.next
            if longer_node is None and carry_bite:
                result_pre.next = ListNode(carry_bite)
                return result
        result_pre.next = longer_node

        return result

    def _calculate_node(self, l1_current, l2_current, result_pre, carry_bite):
        sum = l1_current.val + l2_current.val + carry_bite
        result_pre.next = ListNode(sum % 10)
        carry_bite = int(sum / 10)
        l1_current = l1_current.next
        l2_current = l2_current.next
        result_pre = result_pre.next
        return l1_current, l2_current, result_pre, carry_bite



solution = Solution()
l1 = ListNode(1)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
# l1.next.next.next = ListNode(4)
l2 = ListNode(9)
l2.next = ListNode(9)
# l2.next.next = ListNode(4)
result = solution.addTwoNumbers(l1, l2)
print(result)
