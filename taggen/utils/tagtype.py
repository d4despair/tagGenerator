# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/22 10:33
from taggen.tag import Tag

TYPE_BOOL_STRING = (
    'bool',
    'boolean',
    '离散',
    '离散型',
    '开关量',
    '布尔型',
    '布尔量',
)

TYPE_INT_STRING = (
    'int',
    'integer',
    '整型',
    '整数',
    '短整型',
)

TYPE_REAL_STRING = (
    'real',
    'float',
    '浮点型',
    '浮点数',
    '实型',
    '模拟量',
)

TYPE_DINT_STRING = (
    'dint',
    'long',
    '长整型',
    '长整数',
)


def is_bool(ttype: str | Tag):
    if isinstance(ttype, str):
        return ttype.lower() in TYPE_BOOL_STRING
    elif isinstance(ttype, Tag):
        return ttype.type.lower() in TYPE_BOOL_STRING
    else:
        return False


def is_int(ttype: str | Tag):
    if isinstance(ttype, str):
        return ttype.lower() in TYPE_INT_STRING
    elif isinstance(ttype, Tag):
        return ttype.type.lower() in TYPE_INT_STRING
    else:
        return False


def is_real(ttype: str | Tag):
    if isinstance(ttype, str):
        return ttype.lower() in TYPE_REAL_STRING
    elif isinstance(ttype, Tag):
        return ttype.type.lower() in TYPE_REAL_STRING
    else:
        return False


def is_dint(ttype: str | Tag):
    if isinstance(ttype, str):
        return ttype.lower() in TYPE_DINT_STRING
    elif isinstance(ttype, Tag):
        return ttype.type.lower() in TYPE_DINT_STRING
    else:
        return False


class TagType(object):

    def __init__(self, ttype=None, length=None):
        self._type = ttype
        self._length = length

    @property
    def type(self):
        return self._type

    @property
    def length(self):
        return self._length


class TagTypes:
    TYPE_BOOL = TagType(ttype='bool', length=0.1)
    TYPE_INT = TagType(ttype='int', length=2)
    TYPE_DINT = TagType(ttype='dint', length=4)
    TYPE_REAL = TagType(ttype='real', length=4)


def type_length(ttype) -> int | float:
    if is_bool(ttype):
        return TagTypes.TYPE_BOOL.length
    if is_int(ttype):
        return TagTypes.TYPE_INT.length
    if is_dint(ttype):
        return TagTypes.TYPE_DINT.length
    if is_real(ttype):
        return TagTypes.TYPE_REAL.length
    raise ValueError('无法识别该类型: {}'.format(ttype))


def type_name(ttype) -> str:
    if is_bool(ttype):
        return TagTypes.TYPE_BOOL.type
    if is_int(ttype):
        return TagTypes.TYPE_INT.type
    if is_dint(ttype):
        return TagTypes.TYPE_DINT.type
    if is_real(ttype):
        return TagTypes.TYPE_REAL.type
    raise ValueError('无法识别该类型: {}'.format(ttype))
