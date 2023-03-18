# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/15 14:45


class Tag:

    def __init__(self, name='', tag_type='', comment=''):
        self.name = name
        self.type = tag_type
        self.comment = comment

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        if key in self.__dict__:
            self.__setattr__(key, value)
        else:
            print('No such field: "{}" in {}'.format(key, self.__class__))

    def to_list(self):
        l = []
        for fd in self.__dict__:
            l.append(self.__dict__[fd])
        return l


class UDTTag(Tag):

    def __init__(self, name='', tag_type='', comment='', offset=0, read_only=0, alarm_state=0):
        Tag.__init__(self, name, tag_type, comment)
        self.offset = offset
        self.read_only = read_only
        self.alarm_state = alarm_state


class HMITag(Tag):

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
