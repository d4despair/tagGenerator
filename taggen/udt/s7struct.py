# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 16:07
import math

from taggen.udt.s7object import S7Object


class S7Struct(S7Object):
    _rel_type = 'Struct'
    _data: list[S7Object]
    _struct_title = ''
    __init_length = False
    _data_dict = None

    def __init__(self, parent=None, title=None, comment=None):
        super().__init__(parent=parent, title=title)
        self._parent = parent
        self.comment = comment
        self._setup()

    def _setup(self):
        self._data = []
        self._data_dict = {}

    @property
    def data_type(self):
        __parent = self.parent
        self._data_type = self.title
        while __parent is not None:
            if hasattr(__parent, 'title'):
                self._data_type = f'{__parent.title}.{self._data_type}'
            try:
                __parent = __parent.parent
            except TypeError:
                break
        return self._data_type

    def append(self, __object: S7Object):
        if hasattr(__object, 'parent'):
            __object.parent = self
        __object.previous = self._data[-1] if self.size > 0 else None
        if __object.previous:
            __object.previous.next = __object
        self._data.append(__object)

    @classmethod
    def rel_type(cls):
        return cls._rel_type

    @property
    def data(self):
        return tuple(self._data)

    @property
    def data_dict(self):
        if not self._data_dict:
            self._data_dict = {d.title: d for d in self._data}
        return self._data_dict

    @property
    def size(self):
        return len(self._data)

    @property
    def length(self):
        if not self.__init_length:
            last_data = self._data[-1]
            if self.is_bool(last_data):
                __length = math.floor(last_data.offset + 0.1)
                __length += 1 if __length % 2 == 1 else 2
                self._length = __length
            else:
                self._length = last_data.offset + last_data.length
        return self._length

    @property
    def struct_title(self):
        __parent = self.parent
        if __parent:
            self._struct_title = f'{__parent.struct_title}.{self._title}'
        return self._struct_title

    @property
    def rel_str(self):
        return self._rel_type


def test():
    pass
