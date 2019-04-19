# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。
# 示例:
#
# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49

# cost 80ms with 14.5MB

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            w = right - left
            if height[left] < height[right]:
                h = height[left]
                left += 1
            else:
                h = height[right]
                right -= 1
            max_area = max(max_area, h * w)
        return max_area


solution = Solution()

assert solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert solution.maxArea([]) == 0
assert solution.maxArea([1]) == 0

