class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = n
        for index in range(len(flowerbed)):
            if flowerbed[index] == 0 and (index == 0 or flowerbed[index - 1] == 0) and (index == len(flowerbed) - 1 or flowerbed[index + 1] == 0):
                flowers -= 1
                flowerbed[index] = 1
        return flowers <= 0