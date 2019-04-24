# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意：
#
# 答案中不可以包含重复的四元组。
#
# 示例：
#
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
#
# v1: cost 852ms and beat 64.32%
# v2: cost 172ms and beat 84.83%

from typing import List, Dict, Tuple


class Solution:
    def fourSum_v1(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.nums_dict = self._build_nums_dict(nums)
        nums = sorted(set(nums))
        for i in range(len(nums)):
            self._three_sum(nums, i, target - nums[i], nums[i])
        return self.result

    def _three_sum(self, nums: List[int], start_index: int, target: int, num1: int) -> None:
        for i in range(start_index, len(nums)):
            self._two_sum(nums, i, target - nums[i], num1, nums[i])

    def _two_sum(self, nums: List[int], start_index: int, target: int, num1: int, num2: int) -> None:
        for i in range(start_index, len(nums)):
            if target - nums[i] >= nums[i] and target - nums[i] in self.nums_dict:
                num_list = [num1, num2, nums[i], target - nums[i]]
                for num in num_list:
                    if num_list.count(num) > self.nums_dict[num]:
                        break
                else:
                    self.result.append(num_list)

    def fourSum_v2(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.nums_dict = self._build_nums_dict(nums)
        nums = sorted(set(nums))
        self.two_sum = self._build_two_sum(nums)

        for i in range(len(nums)):
            self._three_sum_v2(nums, i, target - nums[i], nums[i])
        return self.result

    def _three_sum_v2(self, nums: List[int], start_index: int, target: int, num1: int) -> None:
        for i in range(start_index, len(nums)):
            if target - nums[i] in self.two_sum:
                for num3, num4 in self.two_sum[target - nums[i]]:
                    if nums[i] <= num3:
                        num_list = [num1, nums[i], num3, num4]
                        for num in num_list:
                            if num_list.count(num) > self.nums_dict[num]:
                                break
                        else:
                            self.result.append(num_list)

    def _build_nums_dict(self, nums: List[int]) -> Dict[int, int]:
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        return nums_dict

    def _build_two_sum(self, nums: List[int]) -> Dict[int, List[Tuple[int, int]]]:
        two_sum = {}
        for i in range(len(nums)):
            for num in nums[i:]:
                if num + nums[i] in two_sum:
                    two_sum[num + nums[i]].append((nums[i], num))
                else:
                    two_sum[(num + nums[i])] = [(nums[i], num)]
        return two_sum


solution = Solution()
# assert solution.fourSum_v2([1, 0, -1, 0, -2, 2], 0) == [[-1,  0, 0, 1],[-2, -1, 1, 2],[-2,  0, 0, 2]]
assert solution.fourSum_v2([0, 0, 0, 0, 0], 0) == [[0, 0, 0, 0]]
assert solution.fourSum_v2([0, 0], 0) == []
assert solution.fourSum_v2([], 0) == []
assert solution.fourSum_v2([1, 2, -2, 3], 0) == []

