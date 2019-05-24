# 给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。
#
# 示例 :
#
# 给定这个链表：1->2->3->4->5
#
# 当 k = 2 时，应当返回: 2->1->4->3->5
#
# 当 k = 3 时，应当返回: 3->2->1->4->5
#
# 说明 :
#
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# cost 64ms and beat 98.57%
#
from utils import ListNode, list_to_node, node_to_list


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pre_head = ListNode(None)
        pre_head.next = head
        pre_node = pre_head

        last_node = self._move(pre_node, k)
        while last_node:
            next_k = last_node.next
            pre_node = self._reverse_sub_list_node(pre_node, next_k, k)
            last_node = self._move(next_k, k - 1)
        return pre_head.next

    def _move(self, list_node: ListNode, k: int) -> ListNode:
        for _ in range(k):
            if list_node is None:
                return None
            list_node = list_node.next
        return list_node

    def _reverse_sub_list_node(self, pre_node: ListNode, next_k: ListNode, k: int) -> ListNode:
        head = new_head = pre_node.next
        next_node = head.next
        new_head.next = next_k

        for _ in range(k - 1):
            temp = next_node.next
            next_node.next = new_head
            new_head = next_node
            next_node = temp
        pre_node.next = new_head
        return head


def my_test():
    solution = Solution()
    assert node_to_list(solution.reverseKGroup(list_to_node([1, 2, 3, 4, 5]), 2)) == [2, 1, 4, 3, 5]
    assert node_to_list(solution.reverseKGroup(list_to_node([1, 2]), 3)) == [1, 2]
    assert node_to_list(solution.reverseKGroup(list_to_node([1, 2]), 2)) == [2, 1]
    assert node_to_list(solution.reverseKGroup(list_to_node([]), 1)) == []


my_test()
