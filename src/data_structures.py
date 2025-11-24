class Stack:
    def __init__(self):
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("В стэке нет элементов!")
        return self.items.pop()

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("В стэке нет элементов!")
        return self.items[-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def __len__(self) -> int:
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, x: int) -> None:
        self.items.append(x)

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError("В очереди нет элементов!")
        return self.items.pop(0)

    def front(self) -> int:
        if self.is_empty():
            raise IndexError("В очереди нет элементов!")
        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def __len__(self) -> int:
        return len(self.items)