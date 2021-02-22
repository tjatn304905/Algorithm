stack1 = []
stack2 = []

class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return False if len(self.data) else True

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            return None

    def __repr__(self):
        result = ''
        for d in self.data:
            result = '| {} |\n'.format(d) + result
        return result

s = Stack()

s.push(1)
s.push(2)
s.push(3)
print(s)

s.pop()
s.pop()
s.pop()
print(s)

# def is_empty(stack):
#     return False if len(stack) else True
#
# def is_full(stack):
#     []
#
# def push(stack, item):
#     stack.append(item)
#
# def pop(stack):
#     if not is_empty():
#         return stack.pop()
#     else:
#         return None
#
# push(stack1, 1)
# pop(stack1)

# 절차 지향 vs 객체 지향(패러다임, 철학)