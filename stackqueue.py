class Queue(object):
    def __init__(self):
        self.data = []

    def inqueue(self, item):
        self.data.append(item)

    def outqueue(self):
        if len(self.data)!=0:
            return self.data.pop(0)
        else:
            return -1
    def top(self):
        if len(self.data)!=0:
            return self.data[0]
        else:
            return -1

    def have(self, item):
        return item in self.data

    def len(self):
        return len(self.data)

"""
列表类，pop函数出队，top函数返回队首元素
当列表长度为0时执行pop和top会返回-1
"""
class Stack(object):
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data)!=0:
            return self.data.pop(-1)
    def top(self):
        if len(self.data)!=0:
            return self.data[-1]

    def have(self, item):
        return item in self.data
    
    def len(self):
        return len(self.data)
    
    def empty(self):
        if(len(self.data) == 0):
            return True
"""
栈
"""