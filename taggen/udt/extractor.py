# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/4/28 17:06
import os
import re

from datablock import DataBlock
from s7data import S7Data
from s7struct import S7Struct
from taggen.udt.udt import UDT


class DBExtractor(list[DataBlock]):
    __line = None
    __lines = None
    _struct_dict: dict[S7Struct] = {}
    _bin: list[DataBlock] = []

    def __init__(self, filename: str, udt_filepath=None):
        super().__init__()
        self.filename = filename
        self._udt_filepath = udt_filepath
        self._setup()

    def _setup(self):
        udt_files = []
        db_files = []
        # 如果是文件夹 优先处理udt
        if os.path.isdir(self.filename):
            for _, _, filenames in os.walk(self.filename):
                for _f in filenames:
                    _file = self.filename + _f
                    if _file.endswith('.udt'):
                        udt_files.append(_file)
                    elif _file.endswith('.db'):
                        db_files.append(_file)
            [self.parse(_f) for _f in udt_files]    # 处理udt
            [self.parse(_f) for _f in db_files]     # 处理db
        else:
            self.parse(self.filename)
        print(f'处理完成，共 {len(self)} 个DB\n')
        print(f'无法添加的DB如下：')
        [print(f'{db.title}: {db.error}') for db in self.bin]

    @property
    def struct_dict(self):
        return self._struct_dict

    def parse(self, filename):
        print()
        if filename.endswith('.db'):
            self.parse_file(filename, DataBlock)
        elif filename.endswith('.udt'):
            self.parse_file(filename, UDT)
        else:
            print(f'无法处理：{filename}')

    def parse_file(self, filename, _class):
        __s7objs = None
        __rel_type = _class.rel_type()

        print('正在处理：{}'.format(filename))
        f = open(filename, 'r', encoding='utf-8')
        self.__lines = f.readlines()

        # 遍历文件内容
        while True:
            try:
                self.__line = self.__lines.pop(0)
            except IndexError:
                f.close()
                self._release()
                break

            if res := re.search(f'{__rel_type} "(.*)"', self.__line):
                __s7objs = _class(title=res[1])
            elif __s7data := self.parse_data(__s7objs):
                __s7objs.append(__s7data)
            elif __s7struct := self.parse_struct(__s7objs):
                __s7objs.append(__s7struct)
            elif re.search(f'END_{__rel_type}', self.__line):
                if __s7objs.generable:
                    print(f'{__rel_type}名称：\'{__s7objs.title}\' 数据个数：{__s7objs.size}')
                    if isinstance(__s7objs, DataBlock):
                        self.append(__s7objs)
                    else:
                        self._struct_dict[__s7objs.title] = __s7objs
                else:
                    self._bin.append(__s7objs)
                    print(f"无法添加，{__rel_type}名称：{__s7objs.title}")

    def parse_data(self, parent=None, line=None):
        line = line if line else self.__line
        if res := re.search(r'(.*) : (.*);(.*)', line):
            # 变量名
            data_name = self._get_name(res.group(1).strip())

            # 变量注释
            data_remark = self._get_remark(res.group(3).strip())

            # 变量类型
            data_type = res.group(2).strip()

            _s7data = S7Data(parent=parent, title=data_name, data_type=data_type, comment=data_remark)

            try:
                if _res := re.search(r'"(.*)"', data_type):
                    _s7data.length = self.get_udt_length(_res[1])
            except KeyError as e:
                _s7data.generable = False
                if _s7data.data_block:
                    _s7data.data_block.generable = False
                    _s7data.data_block.error.append(f'{_s7data.title} 无法获得 {e} 的长度')
                _s7data.length = 0

            return _s7data

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

    @property
    def bin(self):
        return self._bin

    def _release(self):
        self.__line = None
        self.__lines = None

    def get_udt_length(self, _type):
        return self._struct_dict[_type].length
