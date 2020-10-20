from abc import ABCMeta, abstractmethod, abstractproperty


class IQueue(metaclass=ABCMeta):
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
        '''返回队首元素'''
        pass

    @abstractmethod
    def offer(self, x):
        '''将数据元素x插入到队列成为队尾元素'''
        pass

    @abstractmethod
    def poll(self):
        '''队首元素删除并返回其值'''
        pass

    @abstractmethod
    def display(self):
        pass


class CircleQueue(IQueue):
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.queueElem = [None] * self.maxSize
        self.front = 0  # 队首指针，指向队首元素
        self.rear = 0  # 队尾指针，指向队尾元素的下一个

    def clear(self):
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.rear == self.front

    def length(self):
        return (self.rear - self.front + self.maxSize) % self.maxSize

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.queueElem[self.front]

    def offer(self, x):
        if (self.rear + 1) % self.maxSize == self.front:
            raise Exception("队列已满")
        self.queueElem[self.rear] = x
        self.rear = (self.rear + 1) % self.maxSize

    def poll(self):
        if self.isEmpty():
            return None
        p = self.queueElem[self.front]
        self.front = (self.front + 1) % self.maxSize
        return p

    def display(self):
        i = self.front
        while i != self.rear:
            print(self.queueElem[i], end=' ')
            i = (i + 1) % self.maxSize


rab = CircleQueue(3)
rab.offer(1)
rab.offer(2)
month = eval(input("第几个月?\n"))
num = 0
if month == 1:
    num = 1
elif month == 2:
    num = 2
else:
    i = 3
    while month >= i:
        num = rab.poll() + rab.peek()
        rab.offer(num)
        i += 1
print("有%d对兔子" % num)
