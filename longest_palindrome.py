#v1: cost 584ms with 13.2MB

class Solution:
    def longestPalindrome(self, s: str) -> str:
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

    @staticmethod
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

    @staticmethod
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


solution = Solution()
assert solution.longestPalindrome('babad') == 'bab'
assert solution.longestPalindrome('abbc') == 'bb'
assert solution.longestPalindrome('abcddcer') == 'cddc'
assert solution.longestPalindrome('a') == 'a'
assert solution.longestPalindrome('bb') == 'bb'
assert solution.longestPalindrome('bbb') == 'bbb'
assert solution.longestPalindrome('abb') == 'bb'

