class MinStack:

    def __init__(self):
        self.values = []
        self.minimum_stack  = []

    def push(self, val: int) -> None:
        self.values.append(val)
        if len(self.minimum_stack) == 0:
            self.minimum_stack.append(val)
        elif self.minimum_stack[-1] >= val:
            self.minimum_stack.append(val)

    def pop(self) -> None:
        value = self.values[-1]
        if self.minimum_stack[-1] == value:
            self.minimum_stack.pop()
        self.values.pop()


    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.minimum_stack[-1]
        
