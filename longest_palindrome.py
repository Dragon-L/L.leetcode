#v1: cost 584ms with 13.2MB
#v2: cost 332ms with 13.2MB
#
# 使用边界条件提升某些场景的速度
from typing import Tuple


class Solution:
    def longestPalindrome_v1(self, s: str) -> str:
        if not len(s):
            return ''
        elif len(s) == 1 or len(set(s)) == 1:
            return s

        length = len(s)
        palindrome_even = {}
        palindrome_odd = {}
        longest_palindrome = s[0]
        longest_length = 1
        for i in range(1, len(s)):
            longest_length, longest_palindrome = self.update_palindrome_even(i, length, longest_length, longest_palindrome,
                                                                             palindrome_even, s)

            longest_length, longest_palindrome = self.update_palindrome_odd(i, length, longest_length,
                                                                            longest_palindrome, palindrome_odd, s)

        if longest_length % 2:
            return longest_palindrome[1:][::-1] + longest_palindrome
        else:
            return longest_palindrome[::-1] + longest_palindrome

    def update_palindrome_odd(i, length, longest_length, longest_palindrome, palindrome_odd, input):
        for key in list(palindrome_odd.keys()):
            if (key - (i - key)) >= 0 and input[i] == input[key - (i - key)]:
                palindrome_odd[key] += input[i]
                if i == length - 1 and longest_length < (i - key) * 2 + 1:
                    longest_length = (i - key) * 2 + 1
                    longest_palindrome = palindrome_odd[key]
            else:
                if longest_length < (i - 1 - key) * 2 + 1:
                    longest_length = (i - 1 - key) * 2 + 1
                    longest_palindrome = palindrome_odd[key]
                del palindrome_odd[key]
        if i < length - 1 and input[i - 1] == input[i + 1]:
            palindrome_odd[i] = input[i]
        return longest_length, longest_palindrome

    def update_palindrome_even(i, length, longest_length, longest_palindrome, palindrome_even, input):
        for key in list(palindrome_even.keys()):
            if (key - (i - key) - 1) >= 0 and input[i] == input[key - (i - key) - 1]:
                palindrome_even[key] += input[i]
                if i == length - 1 and longest_length < (i - key + 1) * 2:
                    longest_length = (i - key + 1) * 2
                    longest_palindrome = palindrome_even[key]
            else:
                if longest_length < (i - key) * 2:
                    longest_length = (i - key) * 2
                    longest_palindrome = palindrome_even[key]
                del palindrome_even[key]
        if input[i] == input[i - 1]:
            if longest_length == 1:
                longest_length = 2
                longest_palindrome = input[i]
            palindrome_even[i] = input[i]

        return longest_length, longest_palindrome

    def longestPalindrome_v2(self, s: str) -> str:
        if not len(s):
            return ''
        elif len(s) == 1 or len(set(s)) == 1:
            return s

        len_max, left, right = 0, 0, 0
        for i in range(len(s)):
            len1, left1, right1 = self._expand_around_center(s, i, i)
            len2, left2, right2 = self._expand_around_center(s, i, i + 1)
            if len1 > len_max: len_max, left, right = len1, left1, right1
            if len2 > len_max: len_max, left, right = len2, left2, right2
        return s[left:right+1]

    def _expand_around_center(self, s: str, left: int, right: int) -> Tuple[int, int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1, left + 1, right - 1




solution = Solution()
assert solution.longestPalindrome_v2('babad') == 'bab'
assert solution.longestPalindrome_v2('abbc') == 'bb'
assert solution.longestPalindrome_v2('abcddcer') == 'cddc'
assert solution.longestPalindrome_v2('a') == 'a'
assert solution.longestPalindrome_v2('bb') == 'bb'
assert solution.longestPalindrome_v2('bbb') == 'bbb'
assert solution.longestPalindrome_v2('abb') == 'bb'

