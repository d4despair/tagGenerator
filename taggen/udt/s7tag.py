# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 16:59

from taggen.tag.tag import Tag
from taggen.udt.s7object import S7Object, DATA_BOOL, DATA_INT, DATA_REAL, DATA_DINT, DATA_LENGTH


class S7Tag(Tag, S7Object):
    _rel_type = 's7tag'

    def __init__(self, parent=None, tag_name=None, data_type=None, comment=None):
        Tag.__init__(self, name=tag_name, tag_type=data_type, comment=comment)
        if isinstance(parent, S7Object):
            self._ExternalAccessible = parent._external_accessible
            self._ExternalVisible = parent._external_visible
            self._ExternalWritable = parent._external_writable
            self._S7_SetPoint = parent._s7_set_point
            self._parent = parent


class S7BoolTag(S7Tag):

    def __init__(self, parent=None, tag_name=None, comment=None):
        S7Tag.__init__(self, parent=parent, tag_name=tag_name, data_type=DATA_BOOL, comment=comment)
        self.length = DATA_LENGTH[DATA_BOOL]
        self._data_type = DATA_BOOL


class S7IntTag(S7Tag):

    def __init__(self, parent=None, tag_name=None, comment=None):
        S7Tag.__init__(self, parent=parent, tag_name=tag_name, data_type=DATA_INT, comment=comment)
        self.length = DATA_LENGTH[DATA_INT]
        self._data_type = DATA_INT


class S7DintTag(S7Tag):

    def __init__(self, parent=None, tag_name=None, comment=None):
        S7Tag.__init__(self, parent=parent, tag_name=tag_name, data_type=DATA_DINT, comment=comment)
        self.length = DATA_LENGTH[DATA_DINT]
        self._data_type = DATA_DINT


class S7RealTag(S7Tag):

    def __init__(self, parent=None, tag_name=None, comment=None):
        S7Tag.__init__(self, parent=parent, tag_name=tag_name, data_type=DATA_REAL, comment=comment)
        self.length = DATA_LENGTH[DATA_REAL]
        self._data_type = DATA_REAL
