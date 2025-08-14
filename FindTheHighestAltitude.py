class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = max(0, gain[0])
        for index in range(0, len(gain)):
            if index > 0:
                gain[index] = gain[index] + gain[index - 1]
                highest = max(highest, gain[index])
        return highest
# input = [-10]
# elevations = [0, -10]



# Better solution
# Use the previous altitude to find the current altitude
# Input: gain = [-5,1,5,0,-7] len(gain) = 5
# Step 1: Insert a 0 in the first index [0,-5,1,5,0,-7]
# Step 2: Start looping over and summing: [0,-5,1,5,0,-7]
#   [0,-5,-4,5,0,-7]
#   [0,-5,-4,1,0,-7]
#   [0,-5,-4,1,1,-7]
#   [0,-5,-4,1,1,-6]
# Step 3: Loop over the altitude array, and find the largest entry 
# Alternative: maintain the highest altitude while calculating the altitudes


# Naive solution:
# At every spot in the input array:
# Calculated the altitude of that spot
# Loop over the array and return the highest altitude
# O(n^2) 
# Outter loop loops over the WHOLE array
# Inner loop only sometimes loops over the whole array