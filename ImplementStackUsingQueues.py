class MyStack:

    def __init__(self):
        # Hold the queues
        self.Que = deque()
        

    def push(self, x: int) -> None:
        self.Que.append(x)

    def pop(self) -> int:
        for i in range(len(self.Que)-1):
            self.push(self.Que.popleft())
        return self.Que.popleft()


    def top(self) -> int:
        return self.Que[-1]
        

    def empty(self) -> bool:
        return len(self.Que) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()