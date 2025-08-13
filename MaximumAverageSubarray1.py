class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k - 1

        temp = sum(nums[left:right+1])
        best = temp

        while right + 1 < len(nums):
            right += 1
            temp += nums[right] - nums[left]
            left  += 1
            best = max(best, temp)
        return best/k

        