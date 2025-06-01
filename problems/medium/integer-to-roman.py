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
    def intToRoman(self, num: int) -> str:
        res = []

        while num > 0:
            for symbol, number in symbols:
                if number <= num:
                    res.append(symbol)
                    num -= number
                    break

        return "".join(res)


# 3749
#
