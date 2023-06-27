# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 15:39

from taggen import Tag


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
