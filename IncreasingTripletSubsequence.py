class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = float('inf')
        min2 = float('inf')

        for n in nums:
            if n <= min1:
                min1 = n
            elif n <= min2:
                min2 = n
            else:
                return True
        return False
            



# If the numbers are sorted is there 
# 3 numbers in ascending order

# Pointers for:
# i = first index
# j = 0
# k = 0 
# 
# Return false if 