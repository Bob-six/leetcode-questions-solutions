symbols = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
]


class Solution:

    def romanToInt(self, s: str) -> int:
        res = 0

        while s:
            for symbol, number in symbols:
                if s.startswith(symbol):
                    s = s[len(symbol) :]
                    res += number
                    break

        return res
