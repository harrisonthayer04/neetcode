class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        if(len(nums) == 1):
            return 1
        while i < len(nums)-1:
            if(i != len(nums)):
                current_value = nums[i]
                next_value = nums[i+1]
                if current_value == next_value:
                    nums.pop(i+1)
                    i -= 1
            i += 1
        return len(nums)


            
        
print(Solution().removeDuplicates([2,10,10,30,30,30]))




'''
nums = [0,1,2,3,3,4,5]
nums_after_algorithm = [0,1,2,3,4,5]
k = nums_after_algorithm.length()
return k

# Safe to assume that nums.length() > 0
# Safe to assume that the numbers are all real integers no 5i 
'''