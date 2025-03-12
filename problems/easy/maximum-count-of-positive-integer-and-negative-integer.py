


from typing import List




# O(n)
class Solution:
  def maximumCount(self, nums: List[int]) -> int:
    pos_count = 0
    neg_count = 0

    for num in nums:
      if num > 0:
        pos_count += 1
      elif num < 0:
        neg_count += 1

    return max(pos_count, neg_count) 
      
  



# --------------------------------- 
# O(log(n))

class Solution:
  def maximumCount(self, nums: List[int]) -> int:
    def binary_search(target: int) -> int:
      left, right = 0, len(nums)

      while left < right:

        mid = (left + right) // 2

        if nums[mid] < target:
          left = mid + 1

        else:
          right = mid

      return left

    neg_count = binary_search(0)

    pos_count = len(nums) - binary_search(1)

    return max(neg_count, pos_count)
      


    