class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkStack:
    def __init__(self):
        self.top = None  # 指针指向栈顶

    def clear(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def length(self):
        i = 0
        p = self.top
        while p is not None:
            p = p.next
            i += 1
        return i

    def peek(self):  # 返回栈顶元素
        return self.top

    def push(self, x):  # 入栈
        s = Node(x, self.top)
        self.top = s

    def pop(self):  # 将栈顶元素出栈并返回
        if self.isEmpty():
            return None
        p = self.top
        self.top = self.top.next
        return p.data

    def display(self):
        p = self.top
        while p is not None:
            print(p.data, end=' ')
            p = p.next
