# 155. Min Stack
class MinStack:

    def __init__(self):
        self.stack = []
        self.mins =  []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.mins[-1] if self.mins else val)
        self.mins.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]