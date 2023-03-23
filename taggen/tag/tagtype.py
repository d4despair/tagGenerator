# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/16 14:41

class TagType:

    __slots__ = (
        'name',
        'length'
    )

    def __init__(self, name, length):
        self.name = name
        self.length = length

    def __getitem__(self, item):
        return self.__getattribute__(item)
