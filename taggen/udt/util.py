# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/4/26 0:48

from s7struct import S7Struct

TYPE_BOOL = 'bool'


def is_struct(obj):
    if isinstance(obj, S7Struct):
        return True


def is_bool(obj):
    if isinstance(obj, str):
        return obj.lower() == TYPE_BOOL
    if hasattr(obj, 'data_type'):
        return obj.data_type.lower() == TYPE_BOOL
