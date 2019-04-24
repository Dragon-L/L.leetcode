# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
# cost 748ms and beat 91.56%
#
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.nums_dict = {}
        result = []

        for num in nums:
            if num in self.nums_dict:
                self.nums_dict[num] += 1
            else:
                self.nums_dict[num] = 1

        nums = sorted(set(nums))

        for i in range(len(nums)):
            sum_list = self._two_sum(nums, -nums[i], i)
            if sum_list:
                result.extend(sum_list)
        return result

    def _two_sum(self, nums: List[int], target: int, start_index: int) -> List[List[int]]:
        result = []
        for i in range(start_index, len(nums)):
            if target - nums[i] >= nums[i] and target - nums[i] in self.nums_dict:
                num_list = [-target, nums[i], target - nums[i]]
                for num in num_list:
                    if num_list.count(num) > self.nums_dict[num]:
                        break
                else:
                    result.append([-target, nums[i], target - nums[i]])
        return result


solution = Solution()

assert solution.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
assert solution.threeSum([0, 0]) == []
# assert solution.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]]
assert solution.threeSum([]) == []
assert solution.threeSum([1, 2, -2, -1]) == []
