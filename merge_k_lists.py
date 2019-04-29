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
from typing import List

from utils import ListNode, list_to_node, node_to_list


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pass

def test():
    solution = Solution()

    assert node_to_list(solution.mergeKLists(
        [list_to_node([1, 4, 5]), list_to_node([1, 3, 4]), list_to_node([2, 6])])) \
           == [1, 1, 3, 4, 4, 5, 6]

test()