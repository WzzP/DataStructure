import unittest
from linklist import LList, LCList

class test_01_linklist(unittest.TestCase):
    def test_01_linklist(self):
        """单链表"""
        ll = LList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        # ll.for_each(print)
        ll.pop()
        ll.pop()
        ll.pop()
        # ll.for_each(print)
        self.assertEqual(ll.is_empty(), True)

    def test_02_lclist(self):
        """循环单链表"""
        lc = LCList()
        lc.append(1)
        lc.append(2)
        lc.append(3)
        # lc.for_each(print)
        lc.pop()
        lc.pop()
        lc.pop()
        self.assertEqual(lc.is_empty(), True)
        lc.prepend(1)
        lc.prepend(2)
        lc.prepend(3)
        # lc.for_each(print)
        lc.pop()
        lc.pop()
        lc.pop()
        self.assertEqual(lc.is_empty(), True)

if __name__ == '__main__':
    unittest.main()