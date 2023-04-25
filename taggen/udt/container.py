# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/4/25 10:08

# class DataBlock:
#     NON_RETAIN = True
#
#     def __init__(self, title, version='0.1'):
#         self.title = title
#         self.version = version
#         self._struct = []
#
#     @property
#     def struct(self):
#         return tuple(self._struct)
#
#     def append(self, __object) -> None:
#         self._struct.append(__object)


class DBList(list):
    """
    数据块列表
    """
    pass


class StructDict(dict):
    """
    结构字典
    """
    pass


class UDTDict(dict):
    """
    UDT字典
    """
    pass


def test():
    db_list = DBList()
    pass


if __name__ == '__main__':
    test()
