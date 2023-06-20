# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/15 16:25

class Definition:
    prefix = ''
    middle = ''
    udt_type = ''
    comment = ''
    db_addr = ''
    offset = 0

    def __init__(self, prefix='', middle='', udt_type='', comment='', db_addr='', offset=0):
        self.prefix = prefix
        self.middle = middle
        self.udt_type = udt_type
        self.comment = comment
        self.db_addr = db_addr
        self.offset = offset

    def to_list(self):
        return [self.__dict__[fd] for fd in self.__dict__]
