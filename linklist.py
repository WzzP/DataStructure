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

    def prepend(self, elem):
        """设置head"""
        self.head = Node(elem, self._head)

    def pop(self):
        """从开头弹出"""
        if self.is_empty():
            raise 
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        """插入到最后"""
        if self.is_empty():
            self._head = Node(elem)
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = Node(elem)

    def find(self, pred):
        """根据模式匹配"""
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
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

if __name__ == '__main__':
    pass
        
