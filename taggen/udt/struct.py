# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 16:07

class Struct:

    _parent = None
    _struct = []
    _length = 0

    def __init__(self, parent, name=None):
        self._parent = parent
        self.name = name
        self._struct = Struct()
        self._length = self._struct._length

    @property
    def length(self):
        return self._length

    # def _get_length(self):
    #     self._length = len(self._struct)
