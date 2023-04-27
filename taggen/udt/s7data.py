# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 16:59

from taggen.tag.tag import Tag
from taggen.udt.s7object import S7Object, DATA_BOOL, DATA_INT, DATA_REAL, DATA_DINT, DATA_LENGTH
from util import is_struct


class S7Data(S7Object):
    _rel_type = 's7data'
    _struct_title = ''

    def __init__(self, parent=None, title=None, data_type=None, comment=''):
        super().__init__(parent, title, data_type, comment)
        if isinstance(parent, S7Object):
            self._ExternalAccessible = parent._external_accessible
            self._ExternalVisible = parent._external_visible
            self._ExternalWritable = parent._external_writable
            self._S7_SetPoint = parent._s7_set_point
            self._parent = parent

    @property
    def struct_title(self):
        __parent = self._parent
        while __parent is not None:
            if hasattr(__parent, 'title'):
                self._struct_title = f'{__parent.title}.{self._struct_title}'
            try:
                __parent = __parent.parent
            except TypeError:
                break
        return self._struct_title

    # def csv_format(self):
    #     if self.parent:
    #         cf = super().csv_format()
    #         if is_struct(self.parent):
    #             cf[0] = self.struct_title
    #         return cf


class S7BoolData(S7Data):

    def __init__(self, parent=None, title=None, comment=None):
        S7Data.__init__(self, parent=parent, title=title, data_type=DATA_BOOL, comment=comment)
        self.length = DATA_LENGTH[DATA_BOOL]
        self._data_type = DATA_BOOL


class S7IntData(S7Data):

    def __init__(self, parent=None, title=None, comment=None):
        S7Data.__init__(self, parent=parent, title=title, data_type=DATA_INT, comment=comment)
        self.length = DATA_LENGTH[DATA_INT]
        self._data_type = DATA_INT


class S7DintData(S7Data):

    def __init__(self, parent=None, title=None, comment=None):
        S7Data.__init__(self, parent=parent, title=title, data_type=DATA_DINT, comment=comment)
        self.length = DATA_LENGTH[DATA_DINT]
        self._data_type = DATA_DINT


class S7RealData(S7Data):

    def __init__(self, parent=None, title=None, comment=None):
        S7Data.__init__(self, parent=parent, title=title, data_type=DATA_REAL, comment=comment)
        self.length = DATA_LENGTH[DATA_REAL]
        self._data_type = DATA_REAL
