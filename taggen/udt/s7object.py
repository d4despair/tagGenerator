# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 17:13

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
    _data_type = None

    _external_accessible = True
    _external_visible = True
    _external_writable = True
    _s7_set_point = False

    def __init__(self, parent, external_accessible=True, external_visible=True, external_writable=True,
                 s7_set_point=False):
        self._parent = parent
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
        return self._offset

    @offset.setter
    def offset(self, value):
        self._offset = value

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


def is_bool(s):
    if isinstance(s, str):
        return s.lower() == DATA_BOOL.lower()
    if isinstance(s, S7Object):
        return s.data_type.python() == DATA_BOOL.lower()


def is_int(s):
    if isinstance(s, str):
        return s.lower() == DATA_INT.lower()
    if isinstance(s, S7Object):
        return s.data_type.python() == DATA_INT.lower()


def is_dint(s):
    if isinstance(s, str):
        return s.lower() == DATA_DINT.lower()
    if isinstance(s, S7Object):
        return s.data_type.python() == DATA_DINT.lower()


def is_real(s):
    if isinstance(s, str):
        return s.lower() == DATA_REAL.lower()
    if isinstance(s, S7Object):
        return s.data_type.python() == DATA_REAL.lower()


def is_struct(s):
    if isinstance(s, str):
        return s == DATA_Struct
    if isinstance(s, S7Object):
        return s.data_type.python() == DATA_Struct.lower()