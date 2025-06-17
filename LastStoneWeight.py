class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first  = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second) # Because the values are negative
        stones.append(0)
        return abs(stones[0])