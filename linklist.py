class LinkedListUnderflow(Exception):
    pass

class Node(object):
    def __init__(self, elem=None, next=None):
        self.elem = elem
        self.next = next


class LList(object):
    def __init__(self):
        """初始化表"""
        self._head = None

    def is_empty(self):
        """判断是否为空"""
        return self._head is None

    def pop(self):
        """从开头弹出"""
        if self.is_empty():
            raise IndexError('pop from empty llist') 
        p = self._head
        if self._head.next is None:
            self._head = None
        else:
            self._head = self._head.next
        return p.elem

    def append(self, elem):
        """插入到最后"""
        if self.is_empty():
            self._head = Node(elem)
        else:
            p = self._head
            while True:
                if p.next is None:
                    p.next = Node(elem)
                    break
                else:
                    p = p.next

    def printAll(self):
        """打印全表"""
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')

    def for_each(self, proc):
        """遍历全表"""
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next


class LCList(object):
    """循环单链表"""
    def __init__(self):
        self._rear = None

    def is_empty(self):
        """判断是否为空"""
        return self._rear is None

    def prepend(self, elem):
        """前端插入""" 
        p = Node(elem)
        if self.is_empty():
            p.next = p 
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):
        """尾端插入"""
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):
        """前端弹出"""
        if self.is_empty():
            raise IndexError('pop from empty lclist')
        p = self._rear.next
        if p is self._rear:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def for_each(self, proc):
        """循环全表"""
        if self.is_empty():
            return 
        p = self._rear.next
        while True:
            proc(p.elem)
            if p is self._rear:
                break
            p = p.next

if __name__ == '__main__':
    ll = LList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.for_each(print)
    ll.pop()
    ll.pop()
    ll.pop()
    ll.pop()
    ll.for_each(print)