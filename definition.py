# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/15 16:25

class Defn:
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

    def create_from_list(self, l=[]):
        self.prefix = l[0]
        self.middle = l[1]
        self.udt_type = l[2]
        self.comment = l[3]
        self.db_addr = l[4]
        self.offset = l[5]
        return self


    def to_list(self):
        l = list()
        for fd in self.__dict__:
            l.append(self.__dict__[fd])
        return l

