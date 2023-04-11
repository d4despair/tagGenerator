# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/15 14:45


class Tag:

    __slots__ = (
        'name',
        'type',
        'comment',
    )

    def __init__(self, name: str, tag_type: str, comment=None):
        self.name = name
        self.type = tag_type
        self.comment = comment

    @property
    def title(self):
        return self.name

    @property
    def data_type(self):
        return self.type

    def __getitem__(self, item):
        return self.__getattribute__(item)

    def __setitem__(self, key, value):
        if hasattr(key):
            self.__setattr__(key, value)
        else:
            print('No such field: "{}" in {}'.format(key, self.__class__))

    def to_list(self):
        return list([self.__getattribute__(fd) for fd in self.__slots__])


class UDTTag(Tag):

    def __init__(self, name='', tag_type='', comment='', offset=0, read_only=0, alarm_state=0):
        Tag.__init__(self, name, tag_type, comment)
        self.offset = offset
        self.read_only = read_only
        self.alarm_state = alarm_state

    def __str__(self):
        return '后缀: {0}, 类型: {1}, 偏移量: {2}, ' \
               '描述: {3}, 只读: {4}, 报警: {5}'.format(self.name, self.type, self.offset, self.comment,
                                                  self.read_only, self.alarm_state)


class HMITag(Tag):

    __slots__ = (
        'name',
        'tag_type',
        'comment',
        'item_name',
        'read_only',
        'alarm_state',
        'group',
    )

    def __init__(self, name='', tag_type='', comment='', item_name='', read_only=0, alarm_state=0, group=''):
        Tag.__init__(self, name, tag_type, comment)
        self.item_name = item_name
        self.read_only = read_only
        self.alarm_state = alarm_state
        self.group = group


class TagList:
    disc_list = []
    int_list = []
    real_list = []

    def __init__(self, disc_list: [], int_list: [], real_list: []):
        self.disc_list = disc_list
        self.int_list = int_list
        self.real_list = real_list
