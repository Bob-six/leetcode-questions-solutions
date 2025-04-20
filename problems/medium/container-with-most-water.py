from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) <= 1:
            return 0
        if len(heights) == 2:
            return min(heights[0], heights[1]) * 1

        left = 0
        right = len(heights) - 1
        highest_found = 0

        while left < right:
            value = min(heights[left], heights[right]) * (right - left)

            if value > highest_found:
                highest_found = value

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return highest_found


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(Solution().maxArea([1, 2, 4, 3]))
