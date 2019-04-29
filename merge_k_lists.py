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
# v2: 100ms and beat 80.74%
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
        self._merge_k_lists(lists, current_node)
        return merged_list.next

    def _merge_k_lists(self, lists: List[ListNode], current_node: ListNode) -> None:
        lists.sort(key=lambda x: inf if x is None else x.val)
        second_smallest_val = inf
        for i in range(len(lists)):
            if lists[i] is None or second_smallest_val < lists[i].val:
                break

            current_node.next = lists[i]
            current_node = current_node.next
            lists[i] = lists[i].next

            if lists[i] is not None and lists[i].val < second_smallest_val:
                second_smallest_val = lists[i].val
        if second_smallest_val == inf:
            return
        else:
            self._merge_k_lists(lists, current_node)




def test():
    solution = Solution()

    assert node_to_list(solution.mergeKLists_v2(
        [list_to_node([1, 4, 5]), list_to_node([1, 3, 4]), list_to_node([2, 6])])) \
           == [1, 1, 2, 3, 4, 4, 5, 6]

    assert node_to_list(solution.mergeKLists_v2([None, None, None])) == []
    assert node_to_list(solution.mergeKLists_v2([None, list_to_node([1]), None])) == [1]
    assert node_to_list(solution.mergeKLists_v2([None, list_to_node([1, 2]), None])) == [1, 2]

test()