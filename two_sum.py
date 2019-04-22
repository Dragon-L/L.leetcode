# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

from typing import List

#v1: 6828ms with 13.8MB
#v2: 56ms and beat 86.80%
#v3: 56ms and beat 86.80%#
# 提前构建map，做快速查询

class Solution:
    def twoSum_v1(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        raise Exception

    def twoSum_v2(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for index in range(len(nums)):
            currrent_num = nums[index]
            if target - currrent_num in nums_dict:
                return [nums_dict[target - currrent_num], index]
            nums_dict[currrent_num] = index
        raise Exception

    def twoSum_v3(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        left, right = 0, len(nums) - 1
        while left<right:
            sum = sorted_nums[left] + sorted_nums[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -=1
            else:
                if sorted_nums[left] != sorted_nums[right]:
                    return [nums.index(sorted_nums[left]), nums.index(sorted_nums[right])]
                else:
                    first_index = nums.index(sorted_nums[left])
                    second_index = nums.index(sorted_nums[right], first_index+1)
                    return [first_index, second_index]
        raise Exception


solution = Solution()
# assert solution.twoSum_v3([2, 7, 11, 15], 9) == [0, 1]
assert solution.twoSum_v3([3, 3], 6) == [0, 1]