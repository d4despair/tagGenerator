# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/16 9:54
import math
import os

import udt
from udt import *


class UDT:

    def __init__(self, udt_type='', author='', name='', version='', length=0, struct=[]):
        self.udt_type = udt_type
        self.author = author
        self.name = name
        self.version = version
        self.length = length
        self.struct = struct

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        if key in self.__dict__:
            self.__setattr__(key, value)
        else:
            print('No such field: "{}" in {}'.format(key, self.__class__))


def get_udt_from_txt(file_path: str):
    if file_path.endswith('.txt'):
        print('正在处理: {}'.format(file_path))
        f = open(file_path, 'r', encoding='utf-8')
        lines = f.readlines()

        while True:
            temp_line = lines.pop(0)
            if 'DATA_BLOCK' in temp_line:
                print('目前无法处理DB文件')
                return -1
            if 'TYPE' in temp_line:
                break

        new_udt = UDT()
        struct = []
        # udt 类型
        new_udt.udt_type = temp_line[temp_line.find('"') + 1:temp_line.rfind('"')].strip()

        udt_fd = list(new_udt.__dict__)
        # print(udt_fd)

        # udt 作者 描述 版本号
        for i in range(1, 4):
            temp_line = lines.pop(0)
            # print('udt_fd[{}]: , new_udt[{}]'.format(i, udt_fd[i])
            new_udt[udt_fd[i]] = temp_line[temp_line.find(':') + 1:temp_line.rfind('\n')].strip().lower()

        # 读变量
        offset = 0
        pre_type = ''
        while len(lines) > 0:
            temp_line = lines.pop(0)
            if 'END_TYPE' in temp_line:
                break
            elif ':' not in temp_line:
                continue

            new_tag = read_tag(temp_line)

            if udt.is_bool(pre_type):
                if udt.is_bool(new_tag.type):
                    if offset * 10 % 10 > 7:
                        offset = math.floor(offset) + 1
                else:
                    offset = math.floor(offset)
                    if offset % 2 == 1:
                        offset += 1
                    else:
                        offset += 2
            if udt.is_bool(new_tag.type):
                new_tag.offset = '%.1f' % offset
            else:
                new_tag.offset = '%d' % offset

            offset += udt.tag_types[new_tag.type.lower()]
            pre_type = new_tag.type
            struct.append(new_tag)
            new_udt.struct = struct

        # udt 长度
        if udt.is_bool(pre_type):
            offset = math.floor(offset)
            if offset % 2 == 1:
                offset += 1
            else:
                offset += 2
        new_udt.length = offset

        f.close()
        print('处理完毕')
        return new_udt
    else:
        print('无法处理: {}'.format(file_path))

    return -1


def get_udt_from_path(file_path: str):
    udt_dict = {}
    for parent, dirnames, filenames in os.walk(file_path):
        pass
    for f in filenames:
        # print(f)
        temp_udt = get_udt_from_txt(file_path + '\\' + f)
        if temp_udt != -1:
            udt_dict[temp_udt.udt_type] = temp_udt
    return udt_dict


def read_tag(temp_line: str):
    new_tag = UDTTag()
    end_name_index = temp_line.find(':')
    start_type_index = end_name_index + 1
    end_type_index = temp_line.find(';')
    # 变量名
    new_tag.name = temp_line[0:end_name_index].strip()
    # 变量类型
    new_tag.type = temp_line[start_type_index:end_type_index].strip()
    # 注释
    if '//' in temp_line:
        new_tag.comment = temp_line[temp_line.find('//') + 2: temp_line.find('\n')].strip()
    return new_tag


def read_struct(temp_line: str):
    pass
