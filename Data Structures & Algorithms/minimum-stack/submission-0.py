class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack and self.minStack[-1] < val:
            return
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        x = self.stack.pop()
        if self.minStack[-1] == x:
            self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
