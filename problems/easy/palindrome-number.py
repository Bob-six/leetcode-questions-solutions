class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)

        while len(num_str) > 1:
            first = num_str[0]
            last = num_str[-1]
            if first != last:
                return False

            num_str = num_str[1:-1]

        return True


# Second solution


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
