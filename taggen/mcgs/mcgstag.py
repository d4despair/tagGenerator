# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/7/11 14:37

from taggen.tag import Tag


class McgsTag(Tag):

    __slots__ = (
        'tag_name',
        'variable_type',
        'channel',
        'read_only',
        'register',
        'data_type',
        'register_addr',
        'addr_offset',
        'frequency',
        'process',
    )

    def __init__(self, tag_name='', variable_type='INTEGER', channel='读写DB1:000.0',
                 read_only='读写', register='V数据寄存器', data_type='通道的第00位',
                 register_addr='1.0', addr_offset='', frequency=1, process=''):
        self.tag_name = tag_name
        self.variable_type = variable_type
        self.channel = channel
        self.read_only = read_only
        self.register = register
        self.data_type = data_type
        self.register_addr = register_addr
        self.addr_offset = addr_offset
        self.frequency = frequency
        self.process = process




