# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 示例 1:
#
# 输入: 121
# 输出: true
# 示例 2:
#
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:
#
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 进阶:
#
# 你能不将整数转为字符串来解决这个问题吗？
#
# v1: cost 160ms with 13.4MB
# v2: cost 104ms with 13.4MB
# v3: cost 142ms with 13.1MB


class Solution:
    def isPalindrome_v1(self, x: int) -> bool:
        if x < 0:
            return False
        x_str = str(x)
        left = len(x_str) // 2 - 1
        right = (len(x_str) + 1) // 2
        while right < len(x_str):
            if x_str[left] != x_str[right]:
                return False
            left -= 1
            right += 1
        return True

    def isPalindrome_v2(self, x: int) -> bool:
        if x < 0:
            return False
        x_str = str(x)
        x_reversed = x_str[::-1]
        if x_reversed == x_str:
            return True
        else:
            return False

    def isPalindrome_v3(self, x: int) -> bool:
        if x < 0:
            return False
        x_copy = x
        x_reversed = 0
        while x_copy > 0:
            x_reversed = x_reversed * 10 + x_copy % 10
            x_copy //= 10

        if x_reversed == x:
            return True
        else:
            return False

solution = Solution()
assert solution.isPalindrome_v3(121) == True
assert solution.isPalindrome_v3(-121) == False
assert solution.isPalindrome_v3(10) == False
