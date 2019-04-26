# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
# 示例 3:
#
# 输入: "(]"
# 输出: false
# 示例 4:
#
# 输入: "([)]"
# 输出: false
# 示例 5:
#
# 输入: "{[]}"
# 输出: true
#
# cost 52ms and beat 84.53%

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        brackets = []
        for bracket in s:
            if bracket in bracket_map:
                if not brackets or brackets.pop(-1) != bracket_map[bracket]:
                    return False
            else:
                brackets.append(bracket)
        return not brackets


def test():
    solution = Solution()
    assert solution.isValid('') == True
    assert solution.isValid('()') == True
    assert solution.isValid('()[]{}') == True
    assert solution.isValid('(]') == False
    assert solution.isValid('([)]') == False
    assert solution.isValid('{[]}') == True

test()
