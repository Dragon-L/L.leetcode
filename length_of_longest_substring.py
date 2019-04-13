class Solution:
    # V1: cost 332 ms with 13.4 MB
    # V2: cost 92 ms with 13.2 MB
    #
    # 慎用set做重复性验证
    # 记住重复字符的index，来避免不必要验证

    def length_of_longest_substring_v1(self, s: str) -> int:
        start = 0
        end = 1
        len_of_substring = 0

        while end <= len(s):
            sub_str = s[start:end]

            if len(set(sub_str)) != len(sub_str):
                start += 1
            else:
                len_of_substring = max(end - start, len_of_substring)
                end += 1

        return len_of_substring

    def length_of_longest_substring_v2(self, s: str) -> int:
        if s == '':
            return 0

        start = 0
        end = 1
        len_of_substring = 1

        while end < len(s):
            duplicated_index = s.find(s[end], start, end)
            if duplicated_index != -1:
                start = duplicated_index + 1
            else:
                len_of_substring = max(len_of_substring, end - start + 1)
            end += 1

        return len_of_substring


solution = Solution()
print(solution.length_of_longest_substring_v2("abcabcbb"))







