import time
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def node_to_list(list_node: ListNode) -> List:
    list = []
    while list_node:
        list.append(list_node.val)
        list_node = list_node.next
    return list


def list_to_node(list: List) -> ListNode:
    if len(list) == 0:
        return None
    node = ListNode(list[0])
    list_node = node
    for val in list[1:]:
        list_node.next = ListNode(val)
        list_node = list_node.next
    return node


def use_logging(func):
    def add_log(*args):
        start = time.time()
        result = func(*args)
        print('cost %f'%((time.time() - start)*1000))
        return result
    return add_log
