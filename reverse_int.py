# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#  示例 2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2**31,  2**31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

# cost 60ms with 13.2MB


class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        reversed_x = int(str(abs(x))[::-1])
        reversed_x = -reversed_x if is_negative else reversed_x
        if reversed_x < - 2 ** 31 or reversed_x > 2 ** 31 - 1:
            return 0
        else:
            return reversed_x

        # if (is_negative and reversed_x > 2 ** 31) or (not is_negative and reversed_x > 2 ** 31 - 1):
        #     return 0
        # elif is_negative:


solution = Solution()
assert solution.reverse(123) == 321
assert solution.reverse(-123) == -321
assert solution.reverse(120) == 21
assert solution.reverse(1) == 1
