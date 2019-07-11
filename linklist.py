class Node(object):
    def __init__(self, elem=None, next=None):
        self.elem = elem
        self.next = next

class LinkedListUnderflow(Exception):
    pass

class LinkList(object):
    def __init__(self):
        """构造空链表"""
        self.head = None
        self.length = 0

    def append(self, item):
        """尾端插入"""
        e = Node(item)
        if not self:
            self.head = e
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = e
        self.length += 1

    def pop(self):
        """头部弹出"""
        if not self:
            raise LinkedListUnderflow('in pop')
        e = self.head.elem
        self.head = self.head.next
        self.length -= 1
        return e

    def __bool__(self):
        """判断链表空， 为空返回false"""
        return self.head is not None

    def __getitem__(self, index):
        """获取指定索引的元素"""
        if not self:
            raise LinkedListUnderflow('in get')
        if index > self.length-1 or index < 0:
            raise LinkedListUnderflow('link index out of range')
        n = self.head
        i = 0
        while i != index:
            n = n.next
            i += 1
        return n.elem

    def __setitem__(self, index, elem):
        """设置指定索引值"""
        if not self:
            raise LinkedListUnderflow("in set")
        if index > self.length-1 or index < 0:
            raise LinkedListUnderflow('linklist index out of range')
        n = self.head
        i = 0
        while i != index:
            n = n.next
            i += 1
        n.elem = elem

    def __delitem__(self, index):
        """删除指定索引值"""
        if not self:
            raise LinkedListUnderflow("in del")
        if index > self.length-1 or index < 0:
            raise LinkedListUnderflow('Linklist index out of range')
        n = self.head
        i = 0
        if index == 0:
            self.head = self.head.next
            return
        else:
            prev = self.head

        while i != index:
            prev = n
            n = n.next
            i += 1
        prev.next = n.next
        self.length -= 1

    def __iter__(self):
        """迭代链表"""
        n = self.head
        while n is not None:
            yield n.elem
            n = n.next

    def __contains__(self, elem):
        """定义 in 行为"""
        if not self:
            return False
        n = self.head
        while n is not None:
            if n.elem == elem:
                return True
            n = n.next
        return False

    def __len__(self):
        """获取链表长度"""
        return self.length


class LCList(object):
    
    def __init__(self):
        """循环单链表"""
        self.rear = None
        self.length = 0


    def append(self, elem):
        """末尾插入"""
        self.prepend(elem)
        self.rear = self.rear.next

    def prepend(self, elem):
        """前端插入"""
        p = Node(elem)
        if not self:
            p.next = p
            self.rear = p
        else:
            p.next = self.rear.next
            self.rear.next = p
        self.length += 1

    def __getitem__(self, index):
        """获取指定索引的值"""
        if not self:
            raise LinkedListUnderflow('link is None')
        if index > self.length - 1 or index < 0:
            raise LinkedListUnderflow('link index ou of range')
        p = self.rear.next
        i = 0
        while i != index:
            p = p.next 
            i += 1
        return p.elem

    def __setitem__(self, index, elem):
        """设置指定索引的值"""
        if not self:
            raise LinkedListUnderflow('link is None')
        if index > self.length - 1 or index < 0:
            raise LinkedListUnderflow('link index ou of range')
        p = self.rear.next
        i = 0 
        while i != index:
            p = p.next
            i += 1
        p.elem = elem

    def __delitem__(self, index):
        """删除指定索引值"""
        if index > self.length - 1 or index < 0:
            raise LinkedListUnderflow('link index ou of range')
        if index == 0:
            if self.rear is self.rear.next:
                self.rear = None
            else:
                self.rear.next = self.rear.next.next
        else:
            prev = self.rear
            p = self.rear.next
            i = 0
            while i != index:
                prev = p
                p = p.next 
                i += 1
            prev.next = p.next
        self.length -= 1

    def pop(self):
        """首端弹出"""
        if not self:
            raise LinkedListUnderflow('link is None')
        p = self.rear.next
        if self.rear is p:
            self.rear = None
        else:
            self.rear.next = p.next
        return p.elem

    def __len__(self):
        """获取链表长度"""
        return self.length

    def __iter__(self):
        """迭代链表"""
        if not self.rear:
            return
        p = self.rear.next
        while p.next is not self.rear.next:
            yield p.elem
            p = p.next
        yield p.elem

    def __bool__(self):
        """判断表是否为空"""
        return bool(self.rear)

if __name__ == '__main__':
    llist = LCList()
    def pp():
        for i in llist:
            print(i, end=' ')
        print()
    llist.append('a')
    llist.append('b')
    llist.append('c')    
    pp()
    assert llist[0] == 'a'
    assert llist[1] == 'b'
    # llist[2] = 3
    # llist.prepend('c')
    # llist.pop()
    # pp()
    # llist.pop()
    # pp()
    # llist.pop()
    # llist.pop()
    # llist.pop()
    # pp()
    del llist[0]
    del llist[0]
    del llist[0]
    pp()