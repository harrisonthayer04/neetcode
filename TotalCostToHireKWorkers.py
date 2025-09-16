class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []
        total_cost = 0

        for index in range(candidates):
            heapq.heappush(heap, (costs[index], index))
        front_pointer = index
        back_pointer = max(front_pointer + 1, len(costs) - candidates)
        for index2 in range(back_pointer, len(costs)):
            heapq.heappush(heap, (costs[index2], index2))

        while k > 0:
            cost, index3 = heapq.heappop(heap)
            total_cost += cost
            k -= 1
            if front_pointer < back_pointer - 1:
                if index3 <= front_pointer:
                    front_pointer += 1
                    heapq.heappush(heap, (costs[front_pointer], front_pointer))
                else:
                    back_pointer -= 1
                    heapq.heappush(heap, (costs[back_pointer], back_pointer))
        return total_cost
