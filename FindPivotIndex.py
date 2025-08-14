class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixes  = [0] * len(nums)
        postfixes = [0] * len(nums)
        
        for index in range(0, len(nums)):
            if index > 0:
                prefixes[index] = prefixes[index - 1] + nums[index - 1]
        for index in range(len(nums) - 1, -1 , -1):
            if index < len(nums) - 1:
                postfixes[index] = postfixes[index + 1] + nums[index + 1]
        for index in range(0, len(nums)):
            if (prefixes[index] == postfixes[index]):
                return index
        return -1


# More optimal on memory solution
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        array_total = sum(nums)
        left = 0

        for index, value in enumerate(nums):
            if left == array_total - left - value:
                return index
            left += value
        return -1







# Naive solution
# Input: nums = [1, 7, 3, 6, 5, 6]
# prefixes =    [0, 1, 8, 11, 17, 23]
# postfixes =   [27, 20, 17, 11, 6, 0]
# total =       [27, 21, 25, 22, 23, 23]

#Input: nums = [2,1,-1]
# prefixes  = [0, 2, 3]
# postfixes = [0, -1, 0]





# Naive solution
# Input: nums = [1, 7, 3, 6, 5, 6]
# prefixes =    [0, 1, 8, 11, 17, 23]
# postfixes =   [27, 20, 17, 11, 6, 0]
# total =       [27, 21, 25, 22, 23, 23]

#Input: nums = [2,1,-1]
# prefixes  = [0, 2, 3]
# postfixes = [0, -1, 0]