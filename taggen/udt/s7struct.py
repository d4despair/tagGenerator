# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 16:07
import math

from s7object import S7Object


class S7Struct(S7Object):
    _data: list[S7Object]
    _struct_title = ''

    def __init__(self, parent=None, title=None, comment=None):
        super().__init__(parent=parent, title=title)
        self._parent = parent
        self.comment = comment
        self._setup()

    def _setup(self):
        self._data = []

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
        self._data.append(__object)

    @property
    def data(self):
        return tuple(self._data)

    @property
    def size(self):
        return len(self._data)

    # def csv_format(self):
    #     if self.parent:
    #         cf = super(S7Struct, self).csv_format()
    #         if isinstance(self.parent, S7Struct):
    #             cf[0] = self.struct_title
    #         return cf

    @property
    def struct_title(self):
        __parent = self.parent
        if __parent:
            self._struct_title = f'{__parent.struct_title}.{self._title}'
        # while __parent is not None:
        #     if hasattr(__parent, 'title'):
        #         self._struct_title = f'{__parent.title}.{self._struct_title}'
        #     try:
        #         __parent = __parent.parent
        #     except TypeError:
        #         break
        return self._struct_title

    # def init_offset(self):
    #     pass

    def init_offset(self):
        offset = 0

        if self.parent is None:
            offset = 0
        else:
            offset = self.offset
        prev = None | S7Object
        for s7obj in self.data:
            if prev is None:
                s7obj.offset = 0
            elif self.is_bool(prev):
                if self.is_bool(s7obj):
                    if offset * 10 % 10 > 7:
                        offset = math.floor(offset) + 1
                else:
                    offset = math.floor(offset)
                    if offset % 2 == 1:
                        offset += 1
                    else:
                        offset += 2
            elif isinstance(prev, self.__class__):
                prev.init_offset()
            s7obj.offset = offset
            offset += s7obj.length
            prev = s7obj

        if self.is_bool(prev):
            offset = math.floor(offset)
            if offset % 2 == 1:
                offset += 1
            else:
                offset += 2
        # 结构长度
        self.length = offset

    @staticmethod
    def is_bool(__s7obj: S7Object):
        return __s7obj.data_type.lower() == 'bool'


def test():
    pass
