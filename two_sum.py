from typing import List

#v1: 6828ms with 13.8MB
#v2: 56ms with 14.3MB
#
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


solution = Solution()
print(solution.twoSum_v2([1, 2, 2], 4))