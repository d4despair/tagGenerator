# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/4/26 0:48

from s7struct import S7Struct


def is_struct(obj):
    if isinstance(obj, S7Struct):
        return True
