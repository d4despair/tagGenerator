# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 15:32


if __name__ == '__main__':
    import taggen.utils.csvfield
    s = 'parent, name, struct, length'
    t = utils.str_to_tuple(s)
    taggen.utils.csvfield.print_class_init(t)


class DataBlock:
    __slots__ = (
        'data_block',
        'name',
        'title',
        'version',
    )

    def __init__(self, data_block=None, name=None, title=None, version=None):
        self.data_block = data_block
        self.name = name
        self.title = title
        self.version = version
        self._struct = []
