class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                i -= 1
            i += 1
        return len(nums)
        





print(Solution().removeElement([], 11))