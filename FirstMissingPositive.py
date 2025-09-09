class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for index in range(len(nums)):
            if nums[index] < 0: nums[index] = 0
        for index in range(len(nums)):
            val = abs(nums[index]) 
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
        for index in range(1, len(nums) + 1):
            if nums[index - 1] >= 0:
                return index
        return len(nums) + 1

# just keep walking the list