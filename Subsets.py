class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return result

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output: List[List[int]] = []

        def backtrack(index: int, current: List[int]) -> None:
            if index == len(nums):
                output.append(current.copy())
                return
            # Exclude nums[index]
            backtrack(index + 1, current)
            # Include nums[index]
            current.append(nums[index])
            backtrack(index + 1, current)
            current.pop()

        backtrack(0, [])
        return output

    



# nums = [0,1,2], len(nums) = 3
# input = [0,1,2,3,4,5]

# [0]
# [0, 1], [0, 1, 2]
# [0, 2]
"""
    0           1           2           3           4           5
1 2 3 4 5   0 2 3 4 5   0 1 3 4 5   0 1 2 4 5   0 1 2 3 5   0 1 2 3 4


"""