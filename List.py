class List(object):

    def __init__(self):
        """创建空表"""

    def __nonzero__(self):
        """判断是否空表"""

    def __len__(self):
        """获取表长度"""

    def append(self):
        """尾端插入"""

    def __setitem__(self, index, item):
        """按索引位置替换"""

    def __getitem__(self, index, default=None):
        """按索引位置获取"""

    def __delitem__(self, index):
        """删除指定索引位置"""

    def __contains__(self, item):
        """判断值是否存在"""
    