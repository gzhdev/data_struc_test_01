class Node(object):
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkQueue:
    def __init__(self):
        self.front = None  # 队首指针
        self.rear = None  # 队尾指针

    def clear(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def length(self):
        p = self.front
        i = 0
        while p is not None:
            p = p.next
            i += 1
        return i

    def peek(self):  # 返回队首元素
        if self.isEmpty():
            return None
        else:
            return self.front.data

    def offer(self, x):
        s = Node(x, None)
        if not self.isEmpty():
            self.rear.next = s
        else:
            self.front = s
        self.rear = s

    def poll(self):  # 删除队首元素并返回
        if self.isEmpty():
            return None
        p = self.front
        self.front = self.front.next
        if p == self.rear:
            self.rear = None
        return p.data

    def display(self):
        p = self.front
        while p is not None:
            print(p.data, end=' ')
            p = p.next
