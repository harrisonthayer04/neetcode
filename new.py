from typing import Optional

class Solution:
    def sortColors(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0]*3
        for number in nums:
            counts[number] += 1

        index = 0
        for i in range(3):
            while counts[i]:
                counts[i] -= 1
                nums[index] = i
                index += 1

# Soln from neetcode.io
myItem = Solution()
Solution.sortColors([2,1,0])
