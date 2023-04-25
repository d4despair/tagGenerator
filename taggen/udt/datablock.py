# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 15:32


class DataBlock:
    _db_number = 0
    parent = None

    def __init__(self, title=None, version=None):
        self.title = title
        self.version = version
        self._setup()

    def _setup(self):
        self._data = []

    @property
    def data(self):
        return tuple(self._data)

    @property
    def data_block(self):
        return self

    @property
    def db_number(self):
        return self._db_number

    @db_number.setter
    def db_number(self, number: int):
        self._db_number = number

    def append(self, __object):
        if hasattr(__object, 'parent'):
            __object.parent = self
        self._data.append(__object)

    def __getitem__(self, item):
        return self._data[item]

    # def init_offset(self):
    #     offset = 0
    #     with self._struct.struct as root_struct:
    #         for s7obj in root_struct:
    #             if isinstance(s7obj, S7Object):
    #                 s7obj.offset = offset
    #                 offset += s7obj.length


if __name__ == '__main__':
    db = DataBlock(title='test')
    db.append('good')
    db.append('good2')
    print(db[0])
    print(db[1])
    pass
