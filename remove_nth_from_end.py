# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？

# Definition for singly-linked list.
#
# cost 56ms and beat 78.02%
#
#
from utils import node_to_list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        previous_node = head
        last_node = head
        for i in range(n):
            last_node = last_node.next
        if last_node == None:
            return head.next
        while last_node.next:
            previous_node = previous_node.next
            last_node = last_node.next
        previous_node.next = previous_node.next.next

        return head


def test():
    node = ListNode(1)
    list_node = node
    for i in range(2, 6):
        list_node.next = ListNode(i)
        list_node = list_node.next

    solution = Solution()
    # assert list_node_to_list(solution.removeNthFromEnd(node, 2)) == [1, 2, 3, 5]
    assert node_to_list(solution.removeNthFromEnd(ListNode(1), 1)) == []


test()
