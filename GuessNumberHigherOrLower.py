# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        # Create a range from 1 to n
        left  = 1 
        right = n

        while left <= right:
            midpoint = (left + right) // 2
            result = int(guess(midpoint))
            if result == -1:
                right = midpoint - 1
            elif result == 1:
                left = midpoint + 1
            else:
                return midpoint
        