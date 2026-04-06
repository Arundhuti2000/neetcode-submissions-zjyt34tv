class MinStack:

    def __init__(self):
        self.values = []

    def push(self, val: int) -> None:
        curMin = self.getMin()
        if curMin == None or curMin > val:
            curMin = val
        self.values.append((val, curMin))

    def pop(self) -> None:
        self.values.pop()

    def top(self) -> int:
        return self.values[-1][0] if self.values else None

    def getMin(self) -> int:
        return self.values[-1][1] if self.values else None

