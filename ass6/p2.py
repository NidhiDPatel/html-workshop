class StackEmptyError(Exception):
    pass


class StackOverflowError(Exception):
    pass


class Stack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def push(self, item):
        if len(self.stack) >= self.capacity:
            raise StackOverflowError("Stack is full!")

        self.stack.append(item)
        print("Pushed:", item)

    def pop(self):
        if len(self.stack) == 0:
            raise StackEmptyError("Stack is empty!")

        item = self.stack.pop()
        print("Popped:", item)
        return item


# Create stack with capacity 3
s = Stack(3)


# Push elements
try:
    s.push(10)
    s.push(20)
    s.push(30)

    # This deliberately causes overflow
    s.push(40)

except StackOverflowError as e:
    print("Overflow Error:", e)


# Pop elements
try:
    s.pop()
    s.pop()
    s.pop()

    # This deliberately causes empty-stack error
    s.pop()

except StackEmptyError as e:
    print("Empty Stack Error:", e)