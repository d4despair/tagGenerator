# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 17:13
import math

DATA_BOOL = 'Bool'
DATA_INT = 'Int'
DATA_DINT = 'Dint'
DATA_REAL = 'Real'
DATA_Struct = 'Struct'

DATA_LENGTH = {
    DATA_BOOL: 0.1,
    DATA_INT: 2,
    DATA_REAL: 4,
    DATA_DINT: 4,
}


class S7Object:
    _offset = 0
    _length = 0
    _parent = None
    _previous = None
    _next = None
    _data_type: str
    _data_block = None

    _external_accessible = True
    _external_visible = True
    _external_writable = True
    _s7_set_point = False

    __init_offset = False
    # __init_length = False

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
        if data_type in DATA_LENGTH:
            self._length = DATA_LENGTH[data_type]
            # self.__init_length = True
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

    def _init_offset(self):
        if not self.__init_offset:
            if self.previous:
                if self.is_bool(self.previous):
                    if self.is_bool():
                        __offset = self.previous.offset + 0.1
                        if __offset * 10 % 10 > 7:
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

    # def _round_offset(self):
    #     if self.previous:
    #         self

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
            return [self.parent.struct_title, self.title, self.data_type, self.comment, self.db_number, self.offset]

    def is_bool(self, __s7obj=None):
        __data_type = self._data_type
        if __s7obj:
            __data_type = __s7obj.data_type
        return __data_type.lower() == 'bool'


def is_bool(s):
    if isinstance(s, str):
        return s.lower() == DATA_BOOL.lower()
    if isinstance(s, S7Object):
        return s.data_type.lower() == DATA_BOOL.lower()


def is_int(s):
    if isinstance(s, str):
        return s.lower() == DATA_INT.lower()
    if isinstance(s, S7Object):
        return s.data_type.lower() == DATA_INT.lower()


def is_dint(s):
    if isinstance(s, str):
        return s.lower() == DATA_DINT.lower()
    if isinstance(s, S7Object):
        return s.data_type.lower() == DATA_DINT.lower()


def is_real(s):
    if isinstance(s, str):
        return s.lower() == DATA_REAL.lower()
    if isinstance(s, S7Object):
        return s.data_type.lower() == DATA_REAL.lower()


def is_struct(s):
    if isinstance(s, str):
        return s == DATA_Struct
    if isinstance(s, S7Object):
        return s.data_type.lower() == DATA_Struct.lower()
