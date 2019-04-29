# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
#
# v1： over time
#
#
from math import inf
from typing import List, Tuple

from utils import ListNode, list_to_node, node_to_list


class Solution:
    def mergeKLists_v1(self, lists: List[ListNode]) -> ListNode:
        merged_list = ListNode(None)
        current_node = merged_list
        while True:
            index, val = self._find_min(lists)
            if index is None:
                break
            current_node.next = lists[index]
            current_node = current_node.next
            lists[index] = lists[index].next
        return merged_list.next

    def _find_min(self, lists: List[ListNode]) -> Tuple[int, int]:
        index, val = None, inf
        for i in range(len(lists)):
            if lists[i] is not None and lists[i].val < val:
                index, val = i, lists[i].val
        return index, val

    def mergeKLists_v2(self, lists: List[ListNode]) -> ListNode:
        merged_list = ListNode(None)
        current_node = merged_list
        while True:
            self._sort_lists(lists)

    def _sort_lists(self, lists: List[ListNode]) -> List[Tuple[int, int]]:
        pass


def test():
    solution = Solution()

    assert node_to_list(solution.mergeKLists_v1(
        [list_to_node([1, 4, 5]), list_to_node([1, 3, 4]), list_to_node([2, 6])])) \
           == [1, 1, 2, 3, 4, 4, 5, 6]

    assert node_to_list(solution.mergeKLists_v1([None, None, None])) == []
    assert node_to_list(solution.mergeKLists_v1([None, list_to_node([1]), None])) == [1]
    assert node_to_list(solution.mergeKLists_v1([None, list_to_node([1, 2]), None])) == [1, 2]

test()