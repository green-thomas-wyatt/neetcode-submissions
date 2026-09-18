class MinStack:

    def __init__(self):
        self.array = []
        self.mins_array = []
        self.index = 0

    def push(self, val: int) -> None:
        self.array.append(val)
        self.index += 1

        if len(self.array) == 1:
            self.mins_array.append(val)
        elif val < self.mins_array[-1]:
            self.mins_array.append(val)
        else:
            self.mins_array.append(self.mins_array[-1])


    def pop(self) -> None:
        self.array.pop()
        self.mins_array.pop()
        self.index -= 1


    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.mins_array[-1]
