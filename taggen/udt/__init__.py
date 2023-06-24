# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/16 14:34
from taggen.udt._oldudt import *
from taggen.tag.tagtype import TagType
from taggen.udt.udt import UDT

type_bool = TagType('bool', 0.1)
type_int = TagType('int', 2)
type_real = TagType('real', 4)
type_dint = TagType('dint', 4)

tag_types = {
    type_bool.name: type_bool.length,
    type_int.name: type_int.length,
    type_real.name: type_real.length,
    type_dint.name: type_dint.length,
}




def is_bool(s):
    if type(s) == str:
        return s.lower() == type_bool.name
    elif type(s) == TagType:
        return s.title == type_bool.name
    else:
        return False


def is_int(s):
    if type(s) == str:
        return s.lower() == type_int.name
    elif type(s) == TagType:
        return s.title == type_int.name
    else:
        return False


def is_real(s):
    if type(s) == str:
        return s.lower() == type_real.name
    elif type(s) == TagType:
        return s.title == type_real.name
    else:
        return False


def is_dint(s):
    if type(s) == str:
        return s.lower() == type_dint.name
    elif type(s) == TagType:
        return s.title == type_dint.name
    else:
        return False
