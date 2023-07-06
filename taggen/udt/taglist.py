# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/6/20 15:29

import re

from taggen.udt.extractor import DBExtractor
from taggen.tag.tag import HMITag
from taggen.udt.util import is_datablock, is_udt, is_struct, is_array, is_int, is_bool, is_real, DATA_GENERABLE

hmi_addr_prefix = {
    'bool': 'X',
    'int': 'INT',
    'real': 'REAL',
    'dint': 'DINT',
    'word': 'INT',
}


class TagList:
    datablock = None

    def __init__(self, hmi_disc=None, hmi_int=None, hmi_real=None):
        self.disc_list = hmi_disc if hmi_disc else []
        self.int_list = hmi_int if hmi_int else []
        self.real_list = hmi_real if hmi_real else []

    def traverse(self, data_struct, udt_dict, st_dict, init_offset=None, init_prefix=None, init_comment=None):
        if not data_struct.generable:
            return
        if is_datablock(data_struct):
            parent_offset = data_struct.offset
            parent_prefix = data_struct.prefix
            parent_comment = data_struct.comment
            self.datablock = data_struct
        else:
            parent_offset = init_offset if init_offset else 0
            parent_prefix = init_prefix if init_prefix else ''
            parent_comment = init_comment if init_comment else ''
        print(f'====== {parent_prefix}  {parent_comment}======')
        print(f'{data_struct.rel_str} {parent_comment}')

        for data in data_struct.data:
            # 判断是否创建
            if not data.generable:
                continue

            # 是否有别名
            if data.alias:
                title = parent_prefix + '_' + data.alias
            else:
                title = parent_prefix + '_' + data.title
            # 偏移量
            offset = parent_offset + data.offset
            # 注释
            comment = str(parent_comment).strip() + ' ' + str(data.comment).strip()

            # 先判断数据类型
            if is_udt(data):
                data_type = re.search(r'"(\w+)"', data.data_type)[1]
                print(f'udt {data.title} {data.data_type} ')
                self.traverse(data_struct=udt_dict[data_type],
                              udt_dict=udt_dict,
                              st_dict=st_dict,
                              init_offset=offset,
                              init_prefix=title,
                              init_comment=comment)
            elif is_struct(data):
                print(f'struct {data.title} {data.data_type}')
                self.traverse(data_struct=st_dict[data.data_type],
                              udt_dict=udt_dict,
                              st_dict=st_dict,
                              init_offset=offset,
                              init_prefix=title,
                              init_comment=comment)
            elif is_array(data):
                continue
            else:

                # 跳过一些备用点
                if re.search(f'spare', title, re.I):
                    continue
                if re.search(f'备用', comment, re.I):
                    continue

                tag = HMITag()
                tag.name = title
                tag.type = data.data_type
                tag.group = self.datablock.prefix
                tag.comment = comment
                tag.read_only = 'Yes' if data.read_only else 'No'
                # tag.alarm_state = 'On' if is_alarm(title) else 'None'
                tag.alarm_state = data.alarm_state
                tag.item_name = get_item_name(tag.type, self.datablock.db_number, offset)
                # 判断读写
                if is_udt(data.parent):
                    pass

                print(f'{tag.type} {tag.name} {tag.item_name} {tag.comment}')
                if is_bool(data):
                    self.disc_list.append(tag)
                elif is_int(data):
                    self.int_list.append(tag)
                elif is_real(data):
                    self.real_list.append(tag)


def get_item_name(data_type, db_number, offset):
    addr_prefix = hmi_addr_prefix[data_type.lower()]
    if addr_prefix == 'X':
        addr_offset = '%.1f' % offset
    else:
        addr_offset = '%d' % offset

    return f'DB{db_number},{addr_prefix}{addr_offset}'


def get_taglist(_extractor: DBExtractor, _udt_dict=None):
    """
    获取 taglist
    :param _extractor: DB提取器
    :param _udt_dict: 自定义的udt字典
    :return: (disc_list, int_list, real_list)
    """

    db_list = _extractor.db
    st_dict = _extractor.struct_dict
    udt_dict = _udt_dict if _udt_dict else _extractor.udt_dict

    disc_list = []
    int_list = []
    real_list = []

    for db in db_list:
        for data in db:
            data_type = data.data_type.lower()
            if data_type in DATA_GENERABLE:
                pass
            elif is_udt(data_type):
                pass
            elif is_struct(data_type):
                pass
            else:
                print(f'目前无法处理 {data_type} 类型')
