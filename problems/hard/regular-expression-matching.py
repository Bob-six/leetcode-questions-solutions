class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return len(s) == 0

        if len(p) == 1 or p[1] != "*":
            if not s:
                return False

            pattern = p[0]

            if pattern == ".":
                return self.isMatch(s[1:], p[1:])

            return pattern == s[0] and self.isMatch(s[1:], p[1:])

        # Its a god damn * sign again
        buffer = []
        pattern = p[0]

        while len(s) and (pattern == "." or pattern == s[0]):
            buffer.append(s[0])
            s = s[1:]

        while buffer:
            if self.isMatch(s, p[2:]):
                return True

            s = buffer.pop() + s

        return self.isMatch(s, p[2:])


print(Solution().isMatch("aa", "a"))
print(Solution().isMatch("aa", "a*"))
print(Solution().isMatch("ab", ".*"))
print(Solution().isMatch("aab", "c*a*b"))
print(Solution().isMatch("a", "ab*"))
print(Solution().isMatch("bbbba", ".*a*a"))
print(Solution().isMatch("abbbcd", "ab*bbbcd"))


# Optimzed Solution (With the help of chatgpt)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # DP table where dp[i][j] represents if s[0:i] matches p[0:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # Both strings are empty, so they match

        # Handle the case where p has '*' (matching empty string with pattern)
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]  # Case where '*' acts as zero occurrence
                    if p[j - 2] == s[i - 1] or p[j - 2] == ".":
                        dp[i][j] |= dp[i - 1][
                            j
                        ]  # Case where '*' acts as one or more occurrences

        return dp[m][n]
