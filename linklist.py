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

    def reverse(self):
        """反转链表
        思路： 新建一个链表， 然后循环插入
        """
        p = None
        while self._head is not None:
            q = self._head # 从开头弹出
            self._head = self._head.next  # 并将next 赋值给 head
            q.next = p
            p = q
        self._head = p

    def sort(self):
        """排序""" 
        if self._head is None:
            return
        crt = self._head.next
        while crt is not None:
            x = crt.elem
            p = self._head
            while p is not crt and p.elem <= x:
                p = p.next
            while p is not crt:
                y = p.elem
                p.elem = x
                x = y
                p = p.next
            crt.elem = x
            crt = crt.next

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


class DLNode(Node):
    """双链表结点"""
    def __init__(self, elem, prev=None, next=None):
        super(DLNode, self).__init__(elem, next=next)
        self.prev = prev

class DLList(LList):
    """双链表"""
    def __init__(self):
        super(DLList, self).__init__()
        self._rear = None

    def prepend(self, elem):
        """前端插入"""
        p = DLNode(elem, next=self._head)
        if self.is_empty(): # 空表
            self._rear = p
        else:
            p.next.prev = p
        self._head = p

    def append(self, elem):
        """后端插入"""
        p = DLNode(elem, self._rear)
        if self.is_empty(): # 空表
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop(self):
        """前端弹出"""
        if self.is_empty():
            raise IndexError('pop from empty Dllist')
        p = self._head
        self._head = self._head.next
        if self._head is not None:
            self._rear.prev = None
        return  p.elem

    def pop_last(self):
        """后端弹出"""
        if self.is_empty():
            raise IndexError('pop from empty Dllist')
        p = self._rear
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return  p.elem





if __name__ == '__main__':
    dl = DLList()
    dl.append(1)
    dl.append(2)
    dl.append(3)
    dl.for_each(print)
    print(dl.pop())
    print(dl.pop())
    print(dl.pop())
    dl.prepend(1)
    dl.prepend(2)
    dl.prepend(3)
    print(dl.pop_last())
    print(dl.pop_last())
    print(dl.pop_last())
