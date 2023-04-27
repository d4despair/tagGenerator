# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/4/27 17:24

from s7struct import S7Struct


class UDT(S7Struct):
    def __init__(self, title, version=0.1):
        super().__init__(title=title)
