# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
# v1: cost 60ms and beat 79.95%
# v2: cost 60ms and beat 79.95%
#

from utils import ListNode, node_to_list, list_to_node

class Solution:
    def mergeTwoLists_v1(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        merged_list = ListNode(0)
        current_node = merged_list
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                current_node.next = l1
                l1 = l1.next
            else:
                current_node.next = l2
                l2 = l2.next
            current_node = current_node.next
        current_node.next = l1 if l2 is None else l2
        return merged_list.next

    def mergeTwoLists_v2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        if l1.val < l2.val:
            merged_list = l1
            merged_list.next = self.mergeTwoLists_v2(l1.next, l2)
        else:
            merged_list = l2
            merged_list.next = self.mergeTwoLists_v2(l1, l2.next)

        return merged_list


def test():
    solution = Solution()
    assert node_to_list(solution.mergeTwoLists_v2(list_to_node([1,2,4]), list_to_node([1,3,4]))) == [1,1,2,3,4,4]
    assert node_to_list(solution.mergeTwoLists_v2(list_to_node([]), list_to_node([1,3,4]))) == [1,3,4]
    assert node_to_list(solution.mergeTwoLists_v2(list_to_node([2]), list_to_node([1]))) == [1,2]

test()