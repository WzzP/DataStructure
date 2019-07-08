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
        prev = self.head
        next = self.head.next
        while i != index:
            prev = n
            next = n.next
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


if __name__ == '__main__':
    llist = LinkList()
    def pp():
        for i in llist:
            print(i, end=' ')
        print()
    llist.append('a')
    llist.append('b')
    pp()
    llist[0]
    llist[1]
    # llist[2] = 3
    llist.append('c')
    del llist[1]
    pp()
    print(llist.pop())
    pp()
    print(len(llist))
    print('b' in llist)
    print('a' in llist)
    print('c' in llist)
