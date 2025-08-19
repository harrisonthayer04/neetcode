class RecentCounter:

    def __init__(self):
        self.requests = deque()
        

    def ping(self, t: int) -> int:
        self.requests.append(t)
        minimum = t - 3000 # Window minimum to t

        while self.requests and self.requests[0] < minimum:
            self.requests.popleft()
        return len(self.requests)
        


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

#minimum = t - 3000
#maximum = t

# self.requests = [0, 1, 100, 3001, 3002]
#                          ^