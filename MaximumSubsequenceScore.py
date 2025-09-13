class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = []
        index = 0
        while index < len(nums1):
            pairs.append([nums1[index], nums2[index]])
            index += 1

        def get_second_value(pair):return pair[1]

        pairs.sort(key=get_second_value, reverse=True)
        minHeap = []
        n1Sum = 0
        res = 0

        for n1, n2 in pairs:
            n1Sum += n1
            heapq.heappush(minHeap, n1)

            if len(minHeap) > k:
                n1Pop = heapq.heappop(minHeap)
                n1Sum -= n1Pop
            if len(minHeap) == k: res = max(res, n1Sum * n2)
        return res
