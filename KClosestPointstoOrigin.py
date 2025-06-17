class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclideanDistanceFromOrigin(points) -> int:
            return math.sqrt((points[0])**2 + (points[1])**2)
        min_heap = [(euclideanDistanceFromOrigin(point), point) for point in points]
        heapq.heapify(min_heap)
        
        result = []
        for i in range(k):
            distance, point = heapq.heappop(min_heap)
            result.append(point)
        return result




# Return the closest point
# Store the points in a map
    # Key = Euclidean distance from the origin to the point
    # Value = Actual point itself / Coordinates
# Store the kv pairs in a minheap

# Method that calculates the euclidean distance 