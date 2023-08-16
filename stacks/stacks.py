class Stack:
    def __init__(self) -> None:
        self.max_lenght = 100
        self.lenght = 0
        self.stack = []
    
    def is_full(self) -> bool:
        return len(self.stack) == self.max_lenght
    
    def is_empty(self) -> bool:
        return len(self.stack) == 0
    
    def push(self, value: int) -> None:
        if self.is_full():
            raise Exception("Stack is full")
        
        self.stack.insert(self.lenght, value) 
        self.lenght += 1
        return f'Element {self.stack[self.lenght - 1]} added to stack'
        
    def pop(self) -> None:
        if self.is_empty():
            raise Exception("Stack is empty")
        
        self.stack[self.lenght - 1] = None
        self.lenght -= 1
        self.stack = [item for item in self.stack if item is not None]
        
        print(f'Element was removed from stack')
        print(f'Current stack: {self.stack}')
        
stack_instance = Stack()

print(stack_instance.stack)

stack_instance.push(1)
print(stack_instance.stack)

stack_instance.pop()