from abc import ABCMeta, abstractmethod, abstractproperty


class IStack(metaclass=ABCMeta):
    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def length(self):
        pass

    @abstractmethod
    def peek(self):
        '''返回栈顶元素'''
        pass

    @abstractmethod
    def push(self, x):
        '''数据元素x入栈'''
        pass

    @abstractmethod
    def pop(self):
        '''栈顶元素出栈并返回'''
        pass

    @abstractmethod
    def display(self):
        pass


class SqStack(IStack):
    def __init__(self, maxSize):
        self.maxSize = maxSize  # 栈的最大储存单元个数
        self.stackElem = [None] * self.maxSize  # 顺序栈储存空间
        self.top = 0  # 指向栈顶元素的下一个储存单元

    def clear(self):
        self.top = 0

    def isEmpty(self):
        return self.top == 0

    def length(self):
        return self.top

    def peek(self):
        if not self.isEmpty():
            return self.stackElem[self.top - 1]
        else:
            return None

    def push(self, x):
        if self.top == self.maxSize:
            raise Exception("栈已满")
        self.stackElem[self.top] = x
        self.top += 1

    def pop(self):
        if self.isEmpty():
            return None
        self.top -= 1
        return self.stackElem[self.top]

    def display(self):
        for i in range(self.top - 1, -1, -1):
            print(self.stackElem[i], end=' ')


'''
# (1) 初始化一个顺序栈SQS。
SQS = SqStack(100)
# (2) 判断栈是否为空。
print(SQS.isEmpty())
# (3) 将元素1、3、5依次进栈。
q = [1, 3, 5]
for i in range(len(q)):
    SQS.push(q[i])
# (4) 获取栈顶元素。
print(SQS.peek())
# (5) 获取栈的长度。
print(SQS.length())
# (6) 将栈中元素依次出栈并输出。
while SQS.isEmpty() is not True:
    print(SQS.pop())
# (7) 判断栈是否为空。
print(SQS.isEmpty())
'''
