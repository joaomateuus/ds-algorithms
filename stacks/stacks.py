class Stack:
    def __init__(self) -> None:
        self.max_lenght = 100
        self.lenght = 0
        self.stack = []
    
    def is_full(self):
        return len(self.stack) == self.max_lenght
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, value: int):
        if self.is_full():
            raise Exception("Stack is full")
        
        self.stack.insert(self.lenght, value) 
        self.lenght += 1
        
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        
        self.stack[self.lenght - 1] = None
        self.lenght -= 1
        self.stack = [item for item in self.stack if item is not None]
        
stack_instance = Stack()

print(stack_instance.stack)

stack_instance.push(1)
print(stack_instance.stack)

stack_instance.pop()
print(stack_instance.stack)
