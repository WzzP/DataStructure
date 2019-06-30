# 队列

class Node(object):
    def __init__(self, elem=None, next=None):
        self.elem = elem
        self.next = next

class LQueue(object):
    def __init__(self):
        """基于单链表队列"""
        self.head = None
        self.rear = None

    def is_empty(self):
        """判断队列是否为空"""
        return self.head is None

    def enqueue(self, elem):
        """入队"""
        p = Node(elem)
        if self.is_empty():
            self.head = p
            self.rear = p
            self.head.next = self.rear
        else:
            self.rear.next = p
            self.rear = p 

    def dequeue(self):
        """出队"""
        p = self.head
        if p is None:
            raise IndexError('the Queue is empty')
        else:
            self.head = p.next
        return p.elem
    
    def peek(self):
        """查看队列里最早进入的元素，不删除"""
        if self.is_empty():
            return None
        else:
            return self.head.elem

if __name__ == '__main__':
    q = LQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.peek())