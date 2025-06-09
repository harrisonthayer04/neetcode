class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Def: takes the piles, the h, and a possible k and verifies the k
        def verifyPossibleK(piles: List[int], h: int, k: int) -> bool:
            hours_necessary = 0
            for pile in piles:
                hours_necessary += (pile + k - 1) // k
            return True if hours_necessary <= h else False



        left   = 1 
        right  = max(piles)
        answer = right

        while left <= right:
            midpoint = (left+right) // 2
            if verifyPossibleK(piles, h, midpoint):
                answer = midpoint
                right = midpoint - 1
            else:
                left = midpoint + 1
        return answer




