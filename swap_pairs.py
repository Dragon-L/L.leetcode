# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# 示例:
#
# 给定
# 1->2->3->4, 你应该返回
# 2->1->4->3.
#
# v1: cost 52ms and beat 84.16%
#
#
from utils import *


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        pre_head = ListNode(None)
        pre_head.next = head
        pre_node = pre_head

        while pre_node.next is not None and pre_node.next.next is not None:
            l2 = pre_node.next.next
            self._swap_pair(pre_node, l2)
            pre_node = pre_node.next.next
        return pre_head.next

    def _swap_pair(self, l1: ListNode, l2: ListNode) -> None:
        l1.next.next = l2.next
        l2.next = l1.next
        l1.next = l2


def atest():
    solution = Solution()
    assert node_to_list(solution.swapPairs(list_to_node([1, 2, 3, 4]))) == [2, 1, 4, 3]
    assert node_to_list(solution.swapPairs(list_to_node([1, 2, 3]))) == [2, 1, 3]
    assert node_to_list(solution.swapPairs(list_to_node([1, 2]))) == [2, 1]
    assert node_to_list(solution.swapPairs(list_to_node([1]))) == [1]
    assert node_to_list(solution.swapPairs(list_to_node([]))) == []


atest()