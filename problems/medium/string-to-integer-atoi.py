class Solution:
    def is_whitespace(self, char: str):
        return (
            char == " "
            or char == "\n"
            or char == "\t"
            or char == "\r"
            or char == "\r\n"
        )

    def is_sign(self, char: str):
        return char == "+" or char == "-"

    def myAtoi(self, s: str) -> int:
        number = ""
        sign: int = 1

        is_parsing = False

        for char in s:
            if self.is_whitespace(char):
                if is_parsing:
                    break

                continue

            if self.is_sign(char):
                if is_parsing:
                    break
                is_parsing = True

                sign = 1 if char == "+" else -1

            elif char.isdigit():
                if is_parsing is False and char == "0":
                    is_parsing = True
                    continue

                is_parsing = True
                number += char
            else:
                break

        if not number:
            return 0
        number_as_int = int(number) * sign
        int_min, int_max = -(2**31), 2**31 - 1

        if number_as_int < int_min:
            return int_min
        if number_as_int > int_max:
            return int_max

        return number_as_int


print(Solution().myAtoi("    -042"))
