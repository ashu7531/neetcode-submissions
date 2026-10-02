# class MinStack:

#     def __init__(self):
#         self.lst = []
#     def push(self, val: int) -> None:
#         new_min = val if not self.lst else min(self.lst[-1][1], val)
#         self.lst.append((val, new_min))
    
#     def pop(self) -> None:
#         self.lst.pop()

#     def top(self) -> int:
#         return self.lst[-1][0]

#     def getMin(self) -> int:
#         result = self.lst[-1][1]
#         return result

class MinStack:

    def __init__(self):
        self.lst = []  # Stack to hold (value, current minimum)
    
    def push(self, val: int) -> None:
        # Calculate the new minimum
        new_min = val if not self.lst else min(val, self.lst[-1][1])
        self.lst.append((val, new_min))
    
    def pop(self) -> None:
        if self.lst:
            self.lst.pop()

    def top(self) -> int:
        if self.lst:
            return self.lst[-1][0]

    def getMin(self) -> int:
        if self.lst:
            return self.lst[-1][1]
