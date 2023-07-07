# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 17:13
import re
import math
from taggen.udt.util import DATA_LENGTH, DATA_BOOL, is_udt


class S7Object:
    _rel_type = 's7obj'
    _offset = 0
    _length = 0
    _parent = None
    _previous = None
    _next = None
    _data_type: str
    _data_block = None
    generable = True
    read_only = False
    alarm_state = None
    alias = None

    _external_accessible = True
    _external_visible = True
    _external_writable = True
    _s7_set_point = False

    __init_offset = False

    def __init__(self,
                 parent,
                 title,
                 data_type='',
                 comment='',
                 external_accessible=True,
                 external_visible=True,
                 external_writable=True,
                 s7_set_point=False):
        self._title = title
        self._parent = parent
        self._data_type = data_type
        self.comment = comment
        if data_type.lower() in DATA_LENGTH:
            self._length = DATA_LENGTH[data_type.lower()]
        elif is_array(data_type):
            self._length = get_array_length(data_type)
        else:
            self._length = 0
        if parent:
            self._db_number = parent.db_number
            self._data_block = parent.data_block
        if not external_accessible:
            self._external_accessible = False
            self._external_visible = False
            self._external_writable = False
        else:
            self._external_accessible = external_accessible
            self._external_visible = external_visible
            self._external_writable = external_writable
        self._s7_set_point = s7_set_point

    @property
    def title(self):
        return self._title

    @property
    def external_accessible(self):
        return self._external_accessible

    @property
    def external_visible(self):
        return self._external_visible

    @property
    def external_writable(self):
        return self._external_writable

    @property
    def s7_set_point(self):
        return self._s7_set_point

    @property
    def offset(self):
        self._init_offset()
        return self._offset

    @offset.setter
    def offset(self, value):
        self._offset = value
        self.__init_offset = True

    def _init_offset(self):
        if not self.__init_offset:
            if self.previous:
                if self.is_bool(self.previous):
                    if self.is_bool():
                        __offset = self.previous.offset + 0.1
                        if round(__offset * 10) % 10 > 7:
                            __offset = math.floor(__offset) + 1
                    else:
                        __offset = math.floor(self.previous.offset)
                        if __offset % 2 == 1:
                            __offset += 1
                        else:
                            __offset += 2
                    self._offset = float(round(__offset, 1))
                else:
                    self._offset = int(self.previous.offset + self.previous.length)
            self.__init_offset = True

    @property
    def absolute_offset(self):
        if self.parent:
            return self.parent.absolute_offset + self.offset
        else:
            return self.offset

    @property
    def full_comment(self):
        if self.parent:
            if self.parent is self.data_block:
                return self.data_block.comment + ' ' + self.comment
            else:
                return self.parent.full_comment + ' ' + self.comment
        else:
            return self.comment

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, s7object):
        self._previous = s7object

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, s7obj):
        self._parent = s7obj

    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value

    @property
    def data_block(self):
        return self._data_block

    @property
    def db_number(self):
        if self._data_block:
            return self._data_block.db_number

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, s7object):
        self._next = s7object

    def csv_format(self):
        if self.parent:
            return [
                self.data_block.prefix,
                self.title,
                self.data_type,
                f"{self.data_block.comment} {self.comment}",
                self.db_number,
                self.offset,
                self.parent.struct_title,
                self.comment,
                self.data_block.generable,
                self.s7_set_point,
            ]

    def xlsm_format(self):
        if self.parent:
            return [
                self.data_block.prefix,  # self.parent.struct_title,
                self._get_struct_title(),  # self.title,
                self.data_type,
                self.full_comment,
                self.db_number,
                self.absolute_offset,
                is_udt(self.data_type),
                self.parent.struct_title,
                self.title,
            ]

    def udt_format(self):
        if self.parent:
            return [self.parent.struct_title,
                    self.title,
                    self.data_type,
                    self.offset,
                    0,  # 默认值
                    False,  # 保持
                    self._external_accessible,
                    self._external_writable,
                    self._external_visible,
                    self._s7_set_point,
                    '',  # 临时6
                    self.comment,
                    self.alarm_state,
                    yes_no(self.read_only),
                    self.alias,
                    yes_no(self.generable)
                    ]

    def is_bool(self, __s7obj=None):
        __data_type = self._data_type
        if __s7obj:
            __data_type = __s7obj.data_type
        return __data_type.lower() == DATA_BOOL

    def _get_struct_title(self):
        if self.parent:
            st_title = str(self.parent.struct_title).replace(self.data_block.title, '') + '.' + self.title
            st_title = st_title.removeprefix('.')
            st_title = st_title.replace('.', '_')
            return st_title


class DBNumberAvailableObject(S7Object):
    _data_block = None

    def __init__(self, parent, title):
        super().__init__(parent, title)

    @property
    def data_block(self):
        return self._data_block

    @property
    def db_number(self):
        if self._data_block:
            return self._data_block.db_number

    def csv_format(self):
        if self.parent:
            return [self.parent.struct_title, self.title, self.data_type, self.comment, self.db_number, self.offset]


def is_array(data_type):
    return re.search(r"Array", data_type, re.I)


def get_array_length(array_string):
    res = re.search(r'Array\[(\d+)..(\d+)] of (\w+)', array_string, re.I)
    index_start = int(res.group(1))
    index_end = int(res.group(2))
    array_type = res.group(3)
    data_quantity = index_end - index_start + 1
    if array_type.lower() == 'bool':
        return get_bools_length(data_quantity)
    else:
        return data_quantity * DATA_LENGTH[array_type.lower()]


def get_bools_length(quantity):
    byte_size = quantity // 8
    # print(byte_size)
    if quantity % 8 == 0:
        if byte_size % 2 == 0:
            length = byte_size
        else:
            length = byte_size + 1
    else:
        if byte_size % 2 == 0:
            length = byte_size + 2
        else:
            length = byte_size + 1
    return length


def yes_no(b):
    return 'Yes' if b else 'No'


if __name__ == '__main__':
    print(get_array_length('Array[1..32] of Bool'))
