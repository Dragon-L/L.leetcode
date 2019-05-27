# 实现 strStr() 函数。
#
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
#
# 示例 1:
#
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 示例 2:
#
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 说明:
#
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
#
# v1: cost 60 ms and beat 51.73%
# v2: kmp: cost 76ms and beat 30.28%
#
from typing import List
from utils import use_logging


class Solution:
    def strStr_v1(self, haystack: str, needle: str) -> int:
        if 0 == len(haystack) == len(needle):
            return 0
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if self._check_dulplicated(haystack, needle, i):
                return i
        return -1

    def _check_dulplicated(self, haystack, needle, start):
        for i in range(len(needle)):
            if haystack[start + i] != needle[i]:
                return False
        return True

    def strStr_v2(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1

        next = self._init_next(needle)

        h_i = n_i = 0
        while h_i < len(haystack) and n_i < len(needle):

            if n_i == -1 or haystack[h_i] == needle[n_i]:
                h_i += 1
                n_i += 1
            else:
                n_i = next[n_i]
        return h_i - n_i if n_i == len(needle) else -1

    @use_logging
    def _init_next(self, needle: str) -> List[int]:
        next = []
        next.append(-1)
        if len(needle) == 1:
            return next
        next.append(0)
        compare_index = 0
        for i in range(1, len(needle) - 1):
            if needle[i] != needle[compare_index]:
                compare_index = next[compare_index]

            if needle[i] == needle[compare_index]:
                compare_index += 1
                next.append(compare_index)
            else:
                next.append(0)
        return next


def my_test():
    solution = Solution()
    # assert solution.strStr_v2('hello', 'll') == 2
    # assert solution.strStr_v2('aaaaa', 'bba') == -1
    # assert solution.strStr_v2('aaaaa', '') == 0
    # assert solution.strStr_v2('', '') == 0
    # assert solution.strStr_v2('', 'a') == -1
    # assert solution.strStr_v2('aa', 'aaa') == -1
    # assert solution.strStr_v2('a', 'a') == 0
    assert solution.strStr_v2('aabaaabaaac', 'aabaaac') == 4


my_test()
