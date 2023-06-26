# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/4/27 17:24

from taggen.udt.s7struct import S7Struct


class UDT(S7Struct):
    _rel_type = 'TYPE'

    def __init__(self, title, version=None):
        super().__init__(title=title)
        self._version = version

    @property
    def struct_title(self):
        return self.title

    @property
    def version(self):
        return self._version

    def csv_format(self):
        return [
            self.title,
            self.length,
            self.comment,
            self.alias,
            self.version]
