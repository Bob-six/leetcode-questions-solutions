from typing import List


phone_numbers_chars = {
    "1": [],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


class Solution:

    def letterCombinations(self, digits: str, hash_table=None) -> List[str]:
        res = []

        if hash_table is None:
            hash_table = {}

        if len(digits) == 0:
            return res

        if len(digits) == 1:
            return phone_numbers_chars[digits[0]]

        chars = phone_numbers_chars[digits[0]]

        for char in chars:
            combinations = self.letterCombinations(digits[1:])

            for combination in combinations:
                res.append(char + combination)

        for record in res:
            hash_table[digits] = record

        return res
