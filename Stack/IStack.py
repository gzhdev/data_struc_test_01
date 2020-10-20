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

