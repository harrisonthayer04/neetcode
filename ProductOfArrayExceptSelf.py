class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixes  = [1] * n
        postfixes = [1] * n      
        
        for index in range(1, n):
            prefixes[index] = prefixes[index-1]*nums[index-1]

        for index in range(n-2, -1, -1):
            postfixes[index] = postfixes[index+1] * nums[index+1]

        output = []
        for index in range(n):
            output.append(prefixes[index]*postfixes[index])
        
        return output



# nums    = [1, 2, 3, 4]
# Prefix  = [0, 1, 2, 6]
# Postfix = [24, 12, 4, 0]