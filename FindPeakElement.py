class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            midpoint = left + ((right - left) // 2)
            if midpoint > 0 and nums[midpoint] < nums[midpoint - 1]:
                right = midpoint - 1
            elif midpoint < len(nums) - 1 and nums[midpoint] < nums[midpoint + 1]:
                left = midpoint + 1
            else:
                return midpoint


# possible_ouputs = [2, 5]
# nums = [1, 2, 3, 1, 2, 3]
#         ^
#                        ^
#               ^