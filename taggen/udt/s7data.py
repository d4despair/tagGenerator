# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 16:59


from s7object import S7Object


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
