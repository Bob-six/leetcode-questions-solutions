class Solution:
    def reverse(self, x: int) -> int:
        result = []
        sign = -1 if x < 0 else 1
        
        x = abs(x)
        
        if x < 10:
            return sign * x
        
        while x > 0:
            result.append(str(x % 10))
            x //= 10
        
        reversed_num = sign * int("".join(result))
        
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num


print(Solution().reverse(-1))

# Optimized Solution


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_num = 0
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        reversed_num *= sign
        
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num
