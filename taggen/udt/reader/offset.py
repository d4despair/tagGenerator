# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/4/22 20:52
import math
import re

DATA_LENGTH = {
    'bool': 0.1,
    'int': 2,
    'real': 4,
    'dint': 4,
    'word': 2,
    'dword': 4,
}


def add_offset(st: list[list]):
    offset = 0
    last_data_type = None
    for st_data in st:
        data_type = st_data[2].lower()
        if last_data_type is None:
            st_data.append(0)
            last_data_type = data_type
            continue

        if is_bool(last_data_type):
            if is_bool(data_type):
                offset += 0.1
                if offset * 10 % 10 > 7:
                    offset = math.floor(offset) + 1
            else:
                offset = math.floor(offset)
                if offset % 2 == 1:
                    offset += 1
                else:
                    offset += 2
        else:
            offset += get_data_length(last_data_type)

        st_data.append(offset)
        last_data_type = data_type


def is_bool(data_type: str):
    return data_type.lower() == 'bool'


def is_udt(data_type: str):
    if re.search('".+"', data_type):
        return True
    else:
        return False


def is_struct(data_type: str):
    if re.search(r'.+\..+', data_type):
        return True
    else:
        return False


def get_udt_length(udt, length_dict: dict = None):
    length = 0
    return length


def get_length_from_dict(data_type, length_dict: dict):
    if data_type in length_dict:
        return length_dict[data_type]
    else:
        raise ValueError(f'数据长度字典中不包含该数据类型：{data_type}')


def get_length_from_excel(data_type, filepath):
    pass


def get_struct_length(st, length_dict: dict = None):
    length = 0
    return length


def get_data_length(data_type, length_dict: dict = None):
    if data_type is None:
        return 0
    if is_udt(data_type):
        return get_udt_length(data_type, length_dict)
    if is_struct(data_type):
        return get_struct_length(data_type, length_dict)
    if is_bool(data_type):
        return 0.1
    if data_type.lower() in DATA_LENGTH:
        return DATA_LENGTH[data_type.lower()]

    raise ValueError(f'无法获得数据：{data_type} 的长度')
