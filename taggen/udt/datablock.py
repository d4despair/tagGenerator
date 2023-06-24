# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 15:32


from taggen.udt.s7struct import S7Struct


class DataBlock(S7Struct):
    _rel_type = 'DATA_BLOCK'
    parent = None
    _db_number = 0
    _struct_dict: dict[S7Struct]
    _error: list = None
    _prefix = None

    def __init__(self, title=None, version=None):
        super().__init__(title=title)
        self.version = version
        self._setup()

    def _setup(self):
        self._data = []
        self._struct_dict = {}

    @property
    def rel_type_str(self):
        return self._rel_type

    @property
    def data_block(self):
        return self

    @property
    def db_number(self):
        return self._db_number

    @db_number.setter
    def db_number(self, number: int):
        self._db_number = number

    @property
    def struct_title(self):
        return self.title

    @property
    def struct_dict(self):
        return self._struct_dict

    @property
    def error(self):
        if not self._error:
            self._error = []
        return self._error

    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        self._prefix = prefix


if __name__ == '__main__':
    pass
