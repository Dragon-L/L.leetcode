# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
#
#
# v1: cost 148ms and beat 67.07%
# v2: cost 76ms and beat 96.70%
#
# 双指针遍历
# 初始化更有意义的值
#
from bisect import bisect_left
from typing import List


class Solution:
    def threeSumClosest_v1(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                temp_sum = nums[i] + nums[left] + nums[right]
                if abs(temp_sum - target) < abs(closest_sum - target):
                    closest_sum = temp_sum
                if temp_sum < target:
                    left += 1
                elif temp_sum > target:
                    right -= 1
                else:
                    return target
        return closest_sum

    def threeSumClosest_v2(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            right = len(nums) - 1
            left = max(i + 1, bisect_left(nums, target - nums[i] - nums[right], i + 1) - 2)
            while left < right:
                temp_sum = nums[i] + nums[left] + nums[right]
                if abs(temp_sum - target) < abs(closest_sum - target):
                    closest_sum = temp_sum
                if temp_sum < target:
                    left += 1
                elif temp_sum > target:
                    right -= 1
                else:
                    return target
        return closest_sum


solution = Solution()

# assert solution.threeSumClosest_v2([-1,2,1,-4], 1) == 2
assert solution.threeSumClosest_v2([1, 1 ,1, 0], 100) == 3
