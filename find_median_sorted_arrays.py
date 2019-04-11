import math
from typing import List
# Requirement: time complexity = log(m + n)
# cost 80 ~ 116ms  with 13.3MB
#
# 使用二分查找降低时间复杂度到logN
# 对输入进行数据处理，标准化流程，达到简化的目的
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2, nums1, nums2 = self.switch_list_by_length(nums1, nums2)
        max_index_1 = len1 - 1
        max_index_2 = len2 - 1
        continue_flag = True

        if continue_flag:
            continue_flag, result = self.check_if_one_list_is_empty(len1, nums1, nums2)

        if continue_flag:
            continue_flag, result = self.check_if_lists_are_sequential(len2, max_index_1, max_index_2, nums1, nums2)

        if continue_flag:
            result = self.calculate_median(len1, len2, max_index_1, max_index_2, nums1, nums2)
        return result

    def calculate_median(self, len1, len2, max_index_1, max_index_2, nums1, nums2):
        middle1 = (len1 + 1) // 2 - 1
        middle2 = (len2 + 1) // 2 - 1
        move_steps = 0
        start, end = 0, len1
        while True:
            middle1 = middle1 + move_steps
            middle2 = middle2 - move_steps
            move_steps = 0

            if middle2 == 0 and middle1 < max_index_1 and nums2[0] > nums1[middle1 + 1]:
                middle2 = -1
                middle1 += 1
                break
            if middle2 == max_index_2 and nums2[max_index_2] < nums1[middle1 + 1]:
                break

            if middle2 < max_index_2 and middle1 != 0 and nums1[middle1] > nums2[middle2 + 1]:
                end = middle1 - 1
                move_steps = (end + start) // 2 - middle1
                if middle2 - move_steps > max_index_2:
                    move_steps = middle2 - max_index_2
            elif middle1 < max_index_1 and middle2 != 0 and nums2[middle2] > nums1[middle1 + 1]:
                start = middle1 + 1
                move_steps = (end + start) // 2 - middle1
                if middle2 - move_steps < 0:
                    move_steps = middle2 - 0
            if move_steps == 0:
                break

        if len1 % 2 == 0 and len2 % 2 == 0:
            return (max(nums1[middle1], -math.inf if middle2 == -1 else nums2[middle2]) +
                           min(nums1[middle1 + 1], math.inf if middle2 == max_index_2 else nums2[middle2 + 1])) / 2
        elif len1 % 2 != 0 and len2 % 2 != 0:
            median_right = max(nums1[middle1], -math.inf if middle2 < 0 else nums2[middle2])
            median_left = max(min(nums1[middle1], -math.inf if middle2 < 0 else nums2[middle2]),
                              nums1[middle1 - 1] if middle1 else -math.inf,
                              -math.inf if middle2 <= 0 else nums2[middle2 - 1])
            return (median_right + median_left) / 2
        else:
            return float(max(nums1[middle1], -math.inf if middle2 == -1 else nums2[middle2]))

    def check_if_lists_are_sequential(self, len2, max_index_1, max_index_2, nums1, nums2):
        if nums1[max_index_1] <= nums2[0]:
            median_index = (len(nums1) + len(nums2) + 1) // 2 - 1
            if (max_index_1 + max_index_2) % 2 == 0:
                median_left = nums1[median_index]
                median_right = nums2[0] if (median_index == max_index_1) else nums1[median_index + 1]
                return False, (median_right + median_left) / 2
            else:
                return False, float(nums1[median_index])
        if nums1[0] >= nums2[max_index_2]:
            median_index = (len(nums1) + len(nums2) + 1) // 2 - len2 - 1
            if (max_index_1 + max_index_2) % 2 == 0:
                median_left = nums2[max_index_2] if median_index == -1 else nums1[median_index]
                median_right = nums1[median_index + 1]
                return False, (median_left + median_right) / 2
            else:
                return False, float(nums1[median_index])
        return True, None

    def check_if_one_list_is_empty(self, len1, nums1, nums2):
        if not nums2:
            if len1 % 2 == 0:
                return False, (nums1[len1 // 2 - 1] + nums1[len1 // 2]) / 2
            else:
                return False, float(nums1[(len1 + 1) // 2 - 1])
        return True, None

    def switch_list_by_length(self, nums1, nums2):
        len1, len2 = len(nums1), len(nums2)
        if len1 < len2:
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1
        return len1, len2, nums1, nums2


solution = Solution()
assert solution.findMedianSortedArrays([1,6], [2,3,4,5]) == 3.5
assert solution.findMedianSortedArrays([1, 2, 3], [4]) == 2.5
assert solution.findMedianSortedArrays([1, 2, 3], [2, 3]) == 2.0
assert solution.findMedianSortedArrays([1, 2, 3], []) == 2.0
assert solution.findMedianSortedArrays([3], [-2, -1]) == -1.0
assert solution.findMedianSortedArrays([1 ,3], [2]) == 2.0
assert solution.findMedianSortedArrays([1,2], [1,1]) == 1.0
assert solution.findMedianSortedArrays([5], [1,2,3,4,6]) == 3.5
assert solution.findMedianSortedArrays([4], [1,2,3,5]) == 3.0
assert solution.findMedianSortedArrays([6,7], [1,2,3,4,5,8]) == 4.5
assert solution.findMedianSortedArrays([2], [1,3,4]) == 2.5
assert solution.findMedianSortedArrays([1,2,4], [3,5,6]) == 3.5
assert solution.findMedianSortedArrays([6,7,9], [1,2,3,4,5,8]) == 5.0
assert solution.findMedianSortedArrays([1,2,3,6], [4,5,7,8,9]) == 5.0
