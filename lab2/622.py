class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = [0] * k   # 固定大小数组 / Массив фиксированного размера
        self.k = k         # 队列容量 / Размер очереди
        self.front = 0     # 队头下标 / Индекс начала очереди
        self.count = 0     # 当前元素个数 / Количество элементов сейчас

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():   # 如果满了，不能入队 / Если очередь заполнена, добавить нельзя
            return False

        rear = (self.front + self.count) % self.k  # 计算新元素放的位置 / Вычисляем позицию для нового элемента
        self.q[rear] = value
        self.count += 1
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():   # 如果空了，不能出队 / Если очередь пуста, удалить нельзя
            return False

        self.front = (self.front + 1) % self.k  # 队头向后移动 / Сдвигаем начало очереди
        self.count -= 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():   # 空队列返回 -1 / Если очередь пуста, возвращаем -1
            return -1
        return self.q[self.front]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():   # 空队列返回 -1 / Если очередь пуста, возвращаем -1
            return -1

        rear = (self.front + self.count - 1) % self.k  # 队尾下标 / Индекс конца очереди
        return self.q[rear]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.count == 0   # 没有元素就是空 / Если элементов нет, очередь пуста

    def isFull(self):
        """
        :rtype: bool
        """
        return self.count == self.k   # 元素个数等于容量就是满 / Если count == k, очередь полна


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()