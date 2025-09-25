class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        output = [0] * len(spells)
        for index in range(0, len(spells)):
            minimum_potion = math.ceil(success / spells[index])
            left = 0
            right = len(potions) - 1
            result = -1
            while left <= right:
                midpoint = ((left + right) // 2)
                if potions[midpoint] >= minimum_potion:
                    result = midpoint
                    right = midpoint - 1
                elif potions[midpoint] < minimum_potion: left = midpoint + 1
                else: right = midpoint - 1
            if result == -1: output[index] = 0
            else: output[index] = len(potions) - result
        return output
                
        

# O(len(potions)*len(spells)) -> if len(potions) = n and len(spells) = m O(n*m)
# if n = m then O(n^2)
# output = [0] * len(spells)
# For each index in spells
#   For each index2 in potions:
#       if(spells[index] * potions[index2]) >= success:
#           output[index] += 1



# Optimized solution idea
# spells.sort() 
# For each index in spells
#   For each index2 in potions:
#       if(spells[index] * potions[index2]) >= success:
#           output[index] += 1


# success = 25 
# required_spell = 4
# potions = [1,2,3,4,5,6,7,8]
#                          ^
# output =  [0, 0, 1, 4, 5, 5, 6, 6]
# spells = [9, 1, 3, 4, 2, 5, 7, 8, 6]
# spells (after sort) = [1,2,3,4,5,6,7,8,9]
#                              ^