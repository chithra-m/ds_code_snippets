class BrowserHistory:

    def _init_(self, homepage: str):
        self.homepage = homepage
        self.history_list = []
        self.history_list.append(self.homepage)
        self.current_index = 0


    def visit(self, url: str) -> None:
        self.current_index += 1
        for i in range(self.current_index, len(self.history_list)):
            self.history_list.pop()
        self.history_list.append(url)
        

    def back(self, steps: int) -> str:
        self.current_index -= steps
        if self.current_index < 0:
            self.current_index = 0
            #return self.history_list[self.current_index]
        return self.history_list[self.current_index]

    def forward(self, steps: int) -> str:
        self.current_index += steps
        if self.current_index >= len(self.history_list):
            self.current_index = len(self.history_list) - 1
            #return self.history_list[len(self.history_list)-1]
        return self.history_list[self.current_index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)