class Stack:
    def _init_(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print("Popped:", self.stack.pop())

    def display(self):
        print("Stack:", self.stack)


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

s.pop()
s.display()