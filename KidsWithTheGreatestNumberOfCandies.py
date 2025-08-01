class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        king = -1
        output = []
        for kid in candies:
            if kid > king:
                king = kid
        for index in range(0, len(candies)):
            if candies[index] + extraCandies >= king:
                output.append(True)
            else:
                output.append(False)
        return output