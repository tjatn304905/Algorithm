class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, elem):
        self.data.append(elem)

    def dequeue(self):
        return self.data.pop(0)

    def is_empty(self):
        return not bool(len(self.data))

    # 삭제 없이 단순히 맨 앞의 data 값을 리턴
    def get_front(self):
        if self.is_empty():
            return None
        else:
            return self.data[0]

    # 삭제 없이 단순히 맨 뒤의 data 값을 리턴
    def get_rear(self):
        if self.is_empty():
            return None
        else:
            return self.data[-1]


q = Queue()

q.enqueue(1) # None, q.data => [1]
print(q.data)

q.enqueue(2) # None, q.data => [1, 2]
print(q.data)

print(q.is_empty())

print(q.get_front()) # 1

print(q.get_rear()) # 2

q.dequeue() # 1, q.data => [2]
print(q.data)

q.dequeue() # 2, q.data => []
print(q.data)

print(q.is_empty())

print(q.get_rear())