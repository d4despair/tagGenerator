# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 15:32

from taggen.udt.s7struct import S7Struct
from taggen.udt.s7tag import S7Tag
from taggen.udt.s7object import S7Object

if __name__ == '__main__':
    import taggen.utils

    s = 'parent, name, struct, length'
    t = taggen.utils.str_to_tuple(s)
    taggen.utils.print_class_init(t)


class DataBlock:
    # __slots__ = (
    #     'data_block',
    #     'name',
    #     'title',
    #     'version',
    #     'struct',
    # )

    def __init__(self, data_block=None, name=None, title=None, version=None):
        self.data_block = data_block
        self.name = name
        self.title = title
        self.version = version
        self._setup()

    def _setup(self):
        self._struct = S7Struct(parent=self, title='root')

    @property
    def struct(self):
        return self._struct

    def init_offset(self):
        offset = 0
        with self._struct.struct as root_struct:
            for s7obj in root_struct:
                if isinstance(s7obj, S7Object):
                    s7obj.offset = offset
                    offset += s7obj.length
