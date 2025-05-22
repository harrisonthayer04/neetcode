

class BrowserHistory:

    def __init__(self, homepage: str):
        self.site_history = [homepage]
        self.history_size = 1
        self.current_position = 0

    def visit(self, url: str) -> None:
        self.current_position += 1   
        if self.current_position == len(self.site_history):
            self.site_history.append(url)
            self.history_size += 1
        else:
            self.site_history[self.current_position] = url
            self.history_size = self.current_position + 1

        

    def back(self, steps: int) -> str:
        self.current_position = max(0, self.current_position - steps)
        return self.site_history[self.current_position]
        

    def forward(self, steps: int) -> str:
        self.current_position = min(self.history_size - 1, self.current_position + steps)
        return self.site_history[self.current_position]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)