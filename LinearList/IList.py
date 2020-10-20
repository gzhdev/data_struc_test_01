from abc import ABCMeta, abstractmethod, abstractproperty

class IList(metaclass = ABCMeta):
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
    def get(self, i):
        pass

    @abstractmethod
    def insert(self, i, x):
        pass

    @abstractmethod
    def remove(self, i):
        pass

    @abstractmethod
    def indexOf(self, x):
        pass

    @abstractmethod
    def desplay(self):
        pass
