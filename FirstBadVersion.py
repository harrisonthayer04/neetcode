# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Binary search

        left  = 1
        right = n

        while left <= right:
            midpoint = (left + right) // 2
            if isBadVersion(midpoint) and isBadVersion(midpoint - 1):
                right = midpoint - 1
            elif not isBadVersion(midpoint):
                left = midpoint + 1
            else:
                return midpoint