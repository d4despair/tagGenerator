# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/4/26 0:48

import re

DATA_BOOL = 'bool'
DATA_INT = 'int'
DATA_DINT = 'dint'
DATA_REAL = 'real'
DATA_WORD = 'word'
DATA_Struct = 'struct'

DATA_GENERABLE = [
    DATA_BOOL,
    DATA_INT,
    DATA_REAL,
    DATA_DINT,
    DATA_WORD,
]

DATA_INT_TYPE = [
    DATA_INT,
    DATA_WORD,
]

DATA_LENGTH = {
    DATA_BOOL: 0.1,
    DATA_INT: 2,
    DATA_REAL: 4,
    DATA_DINT: 4,
    DATA_WORD: 2,
}

DATA_TRUE = {
    'true',
    'yes',
    '是',
    1,
    '1',
}

DATA_FALSE = {
    'false',
    'No',
    '否',
    '0',
}


def is_bool(obj):
    if isinstance(obj, str):
        return obj.lower() == DATA_BOOL
    if hasattr(obj, 'data_type'):
        return obj.data_type.lower() == DATA_BOOL


def is_int(obj):
    if isinstance(obj, str):
        return obj.lower() in DATA_INT_TYPE
    if hasattr(obj, 'data_type'):
        return obj.data_type.lower() in DATA_INT_TYPE


def is_real(obj):
    if isinstance(obj, str):
        return obj.lower() == DATA_REAL
    if hasattr(obj, 'data_type'):
        return obj.data_type.lower() == DATA_REAL


def is_udt(obj):
    pattern = r'"(\w+)"'
    if isinstance(obj, str):
        return bool(re.search(pattern, obj.lower()))
    if hasattr(obj, 'data_type'):
        return bool(re.search(pattern, obj.data_type.lower()))


def is_struct(obj):
    pattern = r'(\w+)\.(\w+)'
    if isinstance(obj, str):
        return bool(re.search(pattern, obj.lower()))
    if hasattr(obj, 'data_type'):
        return bool(re.search(pattern, obj.data_type.lower()))


def is_array(obj):
    pattern = r'array\s?\[\d+..\d+] of \w+'
    if isinstance(obj, str):
        return bool(re.search(pattern, obj.lower()))
    if hasattr(obj, 'data_type'):
        return bool(re.search(pattern, obj.data_type.lower()))


def is_datablock(obj):
    if isinstance(obj, str):
        return bool(obj.lower() == 'data_block')
    if hasattr(obj, 'rel_str'):
        return bool(obj.rel_str.lower() == 'data_block')


def is_alarm(obj):
    if isinstance(obj, str):
        t = obj.lower()
    elif hasattr(obj, 'title'):
        t = obj.title.lower()
    else:
        return False
    if t.endswith('alm') or t.endswith('alarm') or t.endswith('ol') or t.endswith('fault') or t.endswith('stop'):
        return True
    else:
        return False


def get_true_false(obj):
    if obj:
        if isinstance(obj, str):
            obj = obj.lower().strip()
        return obj in DATA_TRUE
    else:
        return False


def has_children(obj):
    return is_array(obj) or is_udt(obj) or is_struct(obj)


if __name__ == '__main__':
    print(is_array('Array =[0..16] of int'))
    print(is_struct('ROT_C_Motor_DB.M1'))
    print(is_udt('"var_dat"'))
    print(get_true_false(None))
