class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        king = min(height[left], height[right]) * (right - left)
        while left < right:
            if(height[left] <= height[right]):
                left += 1
            elif(height[left] > height[right]):
                right -= 1
            current = (min(height[left], height[right]) * (right - left))
            if current > king:
                king = current
        return king


# height = [0,1,2,3]


# Quadratic approach:
# loop over the input array heights
#   inside of the loop we would loop over the heights array again
#   calcualte the areas, maintaining a king


# How do we maximize the area
# area = width x height 


# (0, 1) = 1
# (0, 2) = 2
# (0, 3) = 3
# (0, 4) = 

# height = [1,8,6,2,5,4,8,3,7]
#             1             2