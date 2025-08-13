class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = result = 0

        start = 0

        for end, num in enumerate(nums):
            zeros += (1 if num == 0 else 0)
    
            while zeros > 1:
                zeros -= (1 if nums[start] == 0 else 0)
                start += 1
            result = max(result, end - start)
        return result
