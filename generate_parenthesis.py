# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#
# cost 60ms and beat 65.17%
#
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self._generate_parenthesis(1, 0, n)

    def _generate_parenthesis(self, current_p: int, used_p: int, max_p: int) -> List[str]:
        result = []
        if current_p == max_p:
            return ['(' + ')' * (max_p - used_p)]
        else:
            for i in range(min(current_p + 1 - used_p, max_p - used_p)):
                result.extend(['(' + ')' * i + str for str in self._generate_parenthesis(current_p + 1, used_p + i, max_p)])
        return result





def test():
    solution = Solution()
    assert solution.generateParenthesis(3) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ]
    assert solution.generateParenthesis(1) == ["()"]
    assert solution.generateParenthesis(0) == []
    assert solution.generateParenthesis(4) == ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())",
                                               "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()",
                                               "()()(())", "()()()()"]


test()
