class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(0, len(nums)):
            ans.append(nums[i])
        for i in range(0, len(nums)):
            ans.append(nums[i])
        return ans



print(Solution().getConcatenation([1,3,2,1]))