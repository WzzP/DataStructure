class StackUnderflow(ValueError):
    """"空栈"""    

class Stack(object):
    def __init__(self):
        """"""
        self._elems = []

    def is_empty(self):
        """是否为空"""
        return  self._elems == []

    def push(self, elem):
        """压入"""
        self._elems.append(elem)
    
    def pop(self):
        """弹出"""
        if self.is_empty():
            raise  StackUnderflow("栈为空")
        return self._elems.pop()            

    def top(self):
        """返回最后压入元素"""
        if self.is_empty():
            raise  StackUnderflow("栈为空")
        return self._elems[-1]

class Node(object):
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

class LStack(object):
    def __init__(self):
        """链表形式栈"""
        self._top = None

    def is_empty(self):
        """判断为空"""
        return self._top is None

    def top(self):
        """返回最后压入元素"""
        if self.is_empty():
            raise  StackUnderflow("栈为空")
        return  self._top.elem

    def pop(self):
        """弹出"""
        if self.is_empty():
            raise  StackUnderflow("栈为空")
        elem = self._top.elem
        self._top = self._top.next
        return  elem


    def push(self, elem):
        """压入"""
        p = Node(elem)
        if self.is_empty():
            self._top = p
        else:
            p.next = self._top
            self._top = p

if __name__ == '__main__':
    st = LStack()
    st.push(1)
    st.push(2)
    st.push(3)
    print(st.pop())
    print(st.pop())
    print(st.pop())
    