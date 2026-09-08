# 스택으로 큐 구현

class MyQueue:

    def __init__ (self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_stack.pop()         

    def peek(self) -> int: 
        if not self.out_stack:
            while self.in_stack:  ## 뒤집어서 부어준다.
                self.out_stack.append(self.in_stack.pop())
        return self.out.stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
