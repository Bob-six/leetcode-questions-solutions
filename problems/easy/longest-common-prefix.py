class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""

        first = strs[0]

        for string in strs[1:]:
            while not string.startswith(first):
                first = first[:-1]

                if not first:
                    return ""

        return first