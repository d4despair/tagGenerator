# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 16:07
import math

from taggen.udt.s7object import S7Object
from taggen.udt.s7tag import S7Tag, S7BoolTag, S7IntTag


class S7Struct(S7Object):
    _struct: list[S7Object]
    # _end = False

    def __init__(self, parent=None, title=None, comment=None):
        super().__init__(parent)
        self._parent = parent
        self.title = title
        self.comment = comment
        self._setup()

    def _setup(self):
        self._struct = []
        self._data_type = 'Struct'
        # self._init_offset()

    def append(self, s7obj):
        if isinstance(s7obj, S7Object):
            s7obj.parent = self
        self._struct.append(s7obj)

    @property
    def struct(self):
        return self._struct

    @struct.setter
    def struct(self, s7obj_list: list[S7Object]):
        for s7obj in s7obj_list:
            self.append(s7obj)
        self._init_offset()

    def _init_offset(self):
        if self.parent is None:
            offset = 0
        else:
            offset = self.offset
        prev = None | S7Object
        for s7obj in self._struct:
            if prev is None:
                s7obj.offset = 0
            elif isinstance(prev, S7BoolTag):
                if isinstance(s7obj, S7BoolTag):
                    if offset * 10 % 10 > 7:
                        offset = math.floor(offset) + 1
                else:
                    offset = math.floor(offset)
                    if offset % 2 == 1:
                        offset += 1
                    else:
                        offset += 2
            elif isinstance(prev, self.__class__):
                prev._init_offset()
            s7obj.offset = offset
            offset += s7obj.length
            prev = s7obj

        if isinstance(prev, S7BoolTag):
            offset = math.floor(offset)
            if offset % 2 == 1:
                offset += 1
            else:
                offset += 2
        # 结构长度
        self.length = offset

    def print_tree(self):
        print('STRUCT TITLE: {} {}'.format(self.title, self.offset))
        for obj in self._struct:
            if isinstance(obj, self.__class__):
                obj.print_tree()
            elif isinstance(obj, S7Tag):
                print('{} {} {} {}'.format(obj.name, obj.offset, obj.data_type, obj.comment))
        print('END STRUCT')


def S7StructFromList(s7obj_list: list[S7Object], parent=None, title=None, comment=None):
    s7struct = S7Struct(parent=parent, title=title, comment=comment)
    s7struct.struct = s7obj_list
    return s7struct


# 测试

# st = S7Struct(title='root')
b1 = S7BoolTag(tag_name='b1', comment='布尔型1')
b2 = S7BoolTag(tag_name='b2', comment='布尔型2')
i1 = S7IntTag(tag_name='i1', comment='整型1')
b3 = S7BoolTag(tag_name='b3', comment='布尔型3')
i2 = S7IntTag(tag_name='i2', comment='整型2')
b4 = S7BoolTag(tag_name='b4', comment='布尔型4')
# st2 = S7Struct(title='child1')
#
# st.append(b1)
# st.append(b2)
# st.append(i1)
# st.append(b3)
# st.append(st2)
# st2.append(i2)
# st2.append(b4)

# for tg in st.struct:
#     print(tg.offset)

# st.print_tree()
# print(st.struct[4].struct[1].offset)


st4_list = [i2, b4]


st4 = S7StructFromList(title='st4', s7obj_list=st4_list)

st3_list = [b1, b2, i1, st4, b3]
st3 = S7StructFromList(title='st3', s7obj_list=st3_list)
# st4.parent = st3

print(st3.print_tree())

testa = 'helloword'
print(f'{testa}')

# print(testa.find('ow').text)
