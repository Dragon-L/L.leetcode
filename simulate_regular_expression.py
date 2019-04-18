# 给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符。
# '*' 匹配零个或多个前面的元素。
# 匹配应该覆盖整个字符串 (s) ，而不是部分字符串。
#
# 说明:
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:
#
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。
# 示例 3:
#
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。
# 示例 4:
#
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。
# 示例 5:
#
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
#
# 使用动态规划，优化迭代（递推），缓存中间结果
# v1: cost 1500ms with 13.2MB
# v2: cost 68ms with 13.3MB

class Solution:
    def isMatch_v1(self, s: str, p: str) -> bool:
        if p == '':
            return s == ''

        is_match_current_letter = s != '' and (s[0] == p[0] or p[0] == '.')

        if len(p) == 1 or p[1] != '*':
            return is_match_current_letter and self.isMatch_v1(s[1:], p[1:])
        else:
            return self.isMatch_v1(s, p[2:]) or (is_match_current_letter and self.isMatch_v1(s[1:], p))

    def isMatch_v2(self, s: str, p: str) -> bool:
        self._cache = [[None for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        return self._match_v2(0, 0, s, p)

    def _match_v2(self, i_s: int, i_p: int, s: str, p: str) -> bool:
        if self._cache[i_s][i_p] is not None:
            return self._cache[i_s][i_p]
        if i_p >= len(p):
            return i_s >= len(s)

        is_match_current_letter = i_s < len(s) and (s[i_s] == p[i_p] or p[i_p] == '.')

        if i_p >= len(p) - 1 or p[i_p + 1] != '*':
            self._cache[i_s][i_p] = is_match_current_letter and self._match_v2(i_s + 1, i_p + 1, s, p)
        else:
            self._cache[i_s][i_p] = (is_match_current_letter and self._match_v2(i_s + 1, i_p, s, p)) or self._match_v2(i_s, i_p + 2, s, p)
        return self._cache[i_s][i_p]


solution = Solution()

# assert solution.isMatch_v2('', '') is True
# assert solution.isMatch_v2('', 'a') is False
# assert solution.isMatch_v2('a', '') is False
# assert solution.isMatch_v2('aa', 'a*') is True
# assert solution.isMatch_v2('aa', '.*') is True
# assert solution.isMatch_v2('aab', 'c*a*b') is True
assert solution.isMatch_v2('mississippi', 'mis*is*p*.') is False
# assert solution.isMatch_v2('aaa', 'a*a') is True

