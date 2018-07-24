# -*- coding:utf-8 -*-
class Array(object):
    __data = []
    __size = 0

    """
    构造函数，传入数组的容量capacity
    """
    def __init__(self, capacity=10, arr=None):
        self.__data = [0 for i in range(capacity)]
        if(arr != None):
            self.__data = [i for i in range(len(arr))]
            self.__size = len(arr)

    """
    将类的实例变成str
    """
    def __str__(self):
        res = ('Array:size = %d，capacity = %d\n') % (self.__size, len(self.__data))
        res +="["
        for i in range(self.__size):
            res += str(self.__data[i])
            if i != self.__size -1:
                res += ","
        res+="]"
        return res

    """
    获取数组的容量
    """
    def getCapacity(self):
        return len(self.__data)

    """
    获取数组中元素的个数
    """
    def getSize(self):
        return self.__size

    """
    返回数组是否为空
    """
    def isEmpty(self):
        return self.__size == 0

    """
    向所有元素后添加一个新元素
    """
    def addLast(self, e):
        self.add(self.__size, e)

    """
    在所有元素前添加一个新元素
    """
    def addFirst(self, e):
        self.add(0, e)

    """
    在第index位置插入一个元素e
    """
    def add(self, index, e):
        if index < 0 or index > self.__size:
            print("Add failed.Require index >=0 and index < size.")
            return
        if self.__size == int(len(self.__data)-1):
            self._resize(2*len(self.__data))

        for i in range(self.__size, index-1, -1):
            self.__data[i+1] = self.__data[i]
        self.__data[index] = e
        self.__size += 1

    """
    动态数组扩容/缩容
    """
    def _resize(self, capacity):
        __newData = [0 for i in range(capacity)]
        for i in range(self.__size):
            __newData[i] = self.__data[i]
        self.__data = __newData

    """
    读取index索引位置的元素 
    """
    def get(self, index):
        if index <0 or index >= self.__size:
            print("Get Failed.Index is illegal.")
            return
        return self.__data[index]

    def getFirst(self):
        return self.get(0)

    def getLast(self):
        return self.get(self.__size-1)

    """
    修改index索引位置的元素为e
    """
    def set(self, index, e):
        if index < 0 or index >= self.__size:
            print("Set Failed.Index is illegal.")
            return
        self.__data[index] = e

    """
    查找数组中是否有元素e
    """
    def contains(self,e):
        for i in range(self.__size):
            if self.__data[i] == e:
                return True
                break
        return False

    """
    查找数组中元素e所在的索引，如果不存在元素e，则返回-1
    """
    def find(self,e):
        for i in range(self.__size):
            if self.__data[i] == e:
                return i
                break
        return -1

    """
    从数组中删除index位置的元素，并且返回删除的元素
    """
    def remove(self, index):
        if index <0 or index >= self.__size:
            print("Remove Failed.Index is illegal.")
            return
        res = self.__data[index]
        for i in range(index+1, self.__size):
           self.__data[i-1] = self.__data[i]
        self.__size -= 1
        if int(self.__size) == int(len(self.__data) / 4):
            self._resize(int(len(self.__data)/2))
        return res

    """
    从数组中删除第一个元素，返回删除的元素
    """
    def removeFirst(self):
        return self.remove(0)
    """
    从数组中删除最后一个元素，返回删除的元素
    """
    def removeLast(self):
        return self.remove(self.__size-1)

    """
    从数组中删除e
    """
    def removeElement(self, e):
        index = self.find(e)
        if index != -1:
            self.remove(index)

    def swap(self, i, j):
        """
        元素i和元素j进行交换
        :param i:
        :param j:
        :return:
        """
        if(i < 0 or i >= self.__size or j < 0 or j>= self.__size):
            print("Index is illegal.")
            return
        t = self.__data[i]
        self.__data[i] = self.__data[j]
        self.__data[j] = t

    """
   主函数
    """
if __name__ == '__main__':
    array = Array(2)
    array.addLast(11)
    array.addLast(22)
    print(array)
    array.addLast(33)
    print(array)
    array.addLast(44)
    print(array)
    array.addLast(55)
    array.addLast(66)
    print(array)
    array.addLast(77)
    print(array)
    array.remove(0)
    print(array)
    array.addLast(88)
    print(array)
    array.addLast(99)
    print(array)
    array.removeFirst()
    print(array)
    array.add(0,11)
    print(array)
    array.add(1,22)
    print(array)
    array.removeFirst()
    print(array)
    array.removeFirst()
    print(array)
    array.removeFirst()
    print(array)
    array.removeFirst()
    print(array)
    array.removeFirst()
    print(array)
    array.removeFirst()
    print(array)

    """
    array.add(2, 333)
    print(array)
    array.set(1, '22x')
    print(array)
    array.remove(1)
    print(array)
    array.removeLast()
    print(array)
    array.removeElement(11)
    print(array)
    """