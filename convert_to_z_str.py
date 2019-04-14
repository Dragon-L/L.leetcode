import numpy as np
# v2: cost 80ms with 13.3MB


class Solution:
    def convert_v1(self, s: str, numRows: int) -> str:
        if not s or len(s) == 1 or numRows == 1:
            return s

        length = len(s)
        numColumns = (length // (numRows + numRows - 2) + 1 ) * 2 if numRows > 2 else (length // numRows + 1)
        num_array = np.zeros((numRows, numColumns)).astype(str)
        left = 0
        for column in range(numColumns):
            if not column % 2 or numRows == 2:
                right = left + numRows
                right = right if right < length else length
                num_array[:right - left, column] = list(s[left:right])
            else:
                right = left + numRows - 2
                right = right if right < length else length
                num_array[1:right - left + 1, column] = list((s[left:right]))
                num_array[:, column] = num_array[:, column][::-1]
            if right >= length:
                break
            left = right

        return ''.join(num_array[num_array != '0.0'])

    def convert_v2(self, s: str, numRows: int) -> str:
        if not s or len(s) == 1 or numRows == 1:
            return s

        length = len(s)
        numColumns = (length // (numRows + numRows - 2) + 1 ) * 2 if numRows > 2 else (length // numRows + 1)
        num_array = [[''] * numRows for _ in range(numColumns)]
        left = 0

        for column in range(numColumns):
            if not column % 2 or numRows == 2:
                right = left + numRows
                right = right if right < length else length
                num_array[column][:right - left] = list(s[left:right])
            else:
                right = left + numRows - 2
                right = right if right < length else length
                num_array[column][1:right - left + 1] = list(s[left:right])
                num_array[column] = num_array[column][::-1]
            if right >= length:
                break
            left = right

        return ''.join([''.join(sub_list) for sub_list in zip(*num_array)])



solution = Solution()
# solution.convert_v2('LEETCODEISHIRING', 4)
#
# assert solution.convert_v2('', 2) == ''
# assert solution.convert_v2('a', 3) == 'a'
# assert solution.convert_v2('LEETCODEISHIRING', 3) == 'LCIRETOESIIGEDHN'
# assert solution.convert_v2('LEETCODEISHIRING', 4) == 'LDREOEIIECIHNTSG'
# assert solution.convert_v2('LEETCODEISHIRING', 1) == 'LEETCODEISHIRING'
# assert solution.convert_v2('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
# assert solution.convert_v2('ABCD', 2) == 'ACBD'
assert solution.convert_v2('ABCDE', 4) == 'ABCED'
