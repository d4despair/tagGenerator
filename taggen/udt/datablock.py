# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 15:32

import re

from s7data import S7Data
from s7struct import S7Struct


class DataBlock(S7Struct):
    parent = None
    _db_number = 0
    _struct_dict: dict[S7Struct]

    def __init__(self, title=None, version=None):
        super().__init__(title=title)
        self.version = version
        self._setup()

    def _setup(self):
        self._data = []
        self._struct_dict = {}

    @property
    def data_block(self):
        return self

    @property
    def db_number(self):
        return self._db_number

    @db_number.setter
    def db_number(self, number: int):
        self._db_number = number

    @property
    def struct_title(self):
        return self.title

    @property
    def struct_dict(self):
        return self._struct_dict


class DBList(list[DataBlock]):
    __line = None
    __lines = None
    _struct_dict: dict[S7Struct] = {}

    def __init__(self, filename: str):
        super().__init__()
        self.filename = filename
        self._setup()
        self._release()

    def _setup(self):
        __db = None
        if self.filename.endswith(('.txt', '.db')):
            print('正在处理：{}'.format(self.filename))
        else:
            print('无法处理：{}'.format(self.filename))
            return
        f = open(self.filename, 'r', encoding='utf-8')
        self.__lines = f.readlines()

        # 遍历文件内容
        while True:
            try:
                self.__line = self.__lines.pop(0)
            except IndexError:
                break

            if res := re.search(r'DATA_BLOCK "(.*)"', self.__line):
                __db = DataBlock(title=res[1])
            elif __s7data := self.parse_data(__db):
                __db.append(__s7data)
            elif __s7struct := self.parse_struct(__db):
                __db.append(__s7struct)
            elif re.search(r'END_DATA_BLOCK', self.__line):
                if __db.size > 0:
                    self.append(__db)
                    print(f'DB名称：\'{__db.title}\' 数据个数：{__db.size}')
                else:
                    print(f"无法添加，DB名称：{__db.title} 数据个数：0")
        print(f'处理完成，共 {len(self)} 个DB')

    @property
    def struct_dict(self):
        return self._struct_dict

    def parse_data(self, parent=None, line=None):
        line = line if line else self.__line
        if res := re.search(r'(.*) : (.*);(.*)', line):
            # 变量名
            data_name = self._get_name(res.group(1).strip())

            # 变量类型
            data_type = res.group(2).strip()
            # 变量注释
            data_remark = self._get_remark(res.group(3).strip())

            return S7Data(parent=parent, title=data_name, data_type=data_type, comment=data_remark)

    def parse_struct(self, parent):
        if res := re.search(r'(.*): (Struct.*)', self.__line):
            # 结构名
            st_name = self._get_name(res.group(1))
            # 结构注释
            st_remark = self._get_remark(res.group(2).strip())
            __struct = S7Struct(parent=parent, title=st_name, comment=st_remark)
            self.struct_dict[__struct.data_type] = __struct
            parent.data_block.struct_dict[__struct.data_type] = __struct
        else:
            return

        while not re.search(r'end_struct', self.__line, re.I):
            try:
                self.__line = self.__lines.pop(0)
            except IndexError:
                break

            # 结构里的数据
            if st_data := self.parse_data(parent=__struct):
                __struct.append(st_data)
            # 嵌套结构
            if child_struct := self.parse_struct(parent=__struct):
                __struct.append(child_struct)
        return __struct

    @staticmethod
    def _get_remark(string: str):
        if res := re.search(r'//(.*)', string):
            return res.group(1).strip()
        else:
            return ''

    @staticmethod
    def _get_name(string: str):
        if res := re.search(r'(.*){(.*)}', string):
            return res.group(1).strip()
        else:
            return string.strip()

    def dict(self) -> dict[DataBlock]:
        return {db.title: db for db in self}

    def _release(self):
        self.__line = None
        self.__lines = None


if __name__ == '__main__':
    pass
