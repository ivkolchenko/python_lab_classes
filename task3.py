class Stack:
    def __init__(self) -> None:
        self.lst = []

    def push(self, value: int) -> None:
        if len(self.lst) > 0:
            self.lst.append([value, min(self.lst[-1][1], value)])
        else:
            self.lst.append([value, value])

    def pop(self) -> None:
        self.lst.pop()

    def top(self) -> int | None:
        if len(self.lst) > 0:
            return self.lst[-1][0]
        else:
            return None

    def get_min(self) -> int | None:
        if len(self.lst) > 0:
            return self.lst[-1][1]
        else:
            return None

#Проверка
stack = Stack()
stack.push(-2)
stack.push(0)
stack.push(-3)
assert stack.get_min() == -3
stack.pop()
assert stack.top() == 0
assert stack.get_min() == -2