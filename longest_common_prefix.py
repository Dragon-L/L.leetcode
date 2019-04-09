from typing import List

# v1: cost 64ms with 13.3MB
# v2: cost 52ms with 13.2MB
# v3: cost 52ms with 13.4MB
#
# zip(*List): 用*来解耦list的每个元素


class Solution:
    def longestCommonPrefix_v1(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        min_len = min([len(str) for str in strs])
        common_prefix = []
        for i in range(min_len):
            current_letter = strs[0][i]

            for str in strs:
                if str[i] != current_letter:
                    return ''.join(common_prefix)

            common_prefix.append(current_letter)

        return ''.join(common_prefix)

    def longestCommonPrefix_v2(self, strs: List[str]) -> str:
        num_of_strs = len(strs)
        if num_of_strs == 0:
            return ''
        elif num_of_strs == 1:
            return strs[0]

        min_len = min([len(str) for str in strs])
        for i in range(min_len):
            current_letter = strs[0][i]

            for str in strs:
                if str[i] != current_letter:
                    return strs[0][:i]

        return strs[0][:min_len]

    def longestCommonPrefix_v3(self, strs: List[str]) -> str:
        num_of_strs = len(strs)
        if num_of_strs == 0:
            return ''
        elif num_of_strs == 1:
            return strs[0]

        common_prefix = ''

        for element in zip(*strs):
            if len(set(element)) == 1:
                common_prefix += element[0]
            else:
                return common_prefix
        return common_prefix

    def longestCommonPrefix_v4(self, strs: List[str]) -> str:
        num_of_strs = len(strs)
        if num_of_strs == 0:
            return ''
        elif num_of_strs == 1:
            return strs[0]

        common_prefix = ''

        for group in zip(*strs):
            for j in range(1, len(group)):
                if group[j] != group[0]:
                    return common_prefix
            common_prefix += group[0]
        return common_prefix


solution = Solution()
print(solution.longestCommonPrefix_v4(['aa', 'a', 'abd']))
