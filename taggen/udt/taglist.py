# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/6/20 15:29

from util import *
from extractor import DBExtractor
from taggen.tag.tag import HMITag
from taggen.udt.s7data import S7Data


class Taglist:

    def __init__(self, hmi_disc=None, hmi_int=None, hmi_real=None):
        self.hmi_disc = hmi_disc if hmi_disc else []
        self.hmi_int = hmi_int if hmi_int else []
        self.hmi_real = hmi_real if hmi_real else []

    def traverse(self, data_list: list, udt_dict, st_dict):
        for data in data_list:
            if is_bool(data):
                tag = HMITag()
                print(f'bool {data.title} {get_offset(data)}')
                self.hmi_disc.append(tag)
            elif is_int(data):
                tag = HMITag()
                print(f'int {data.title} {get_offset(data)}')
                self.hmi_int.append(tag)
            elif is_real(data):
                tag = HMITag()
                print(f'real {data.title} {get_offset(data)}')
                self.hmi_real.append(tag)
            elif is_udt(data):
                data_type = re.search(r'"(\w+)"', data.data_type)[1]
                print(f'udt {data.title}')
                self.traverse(data_list=udt_dict[data_type].data, udt_dict=udt_dict, st_dict=st_dict)
            elif is_struct(data):
                print(f'struct {data.title} {data.data_type}')
                self.traverse(data_list=udt_dict[data.data_type].data, udt_dict=udt_dict, st_dict=st_dict)
            else:
                print(f'无效类型 {data.title}')


def get_offset(data, init_offset=0):
    offset = init_offset + data.offset
    if data.parent is None:
        return offset
    else:
        return get_offset(data.parent, offset)


def get_taglist(_extractor: DBExtractor, _udt_dict=None):
    """
    获取 taglist
    :param _extractor: DB提取器
    :param _udt_dict: 自定义的udt字典
    :return: (disc_list, int_list, real_list)
    """

    db_list = _extractor.db
    st_dict = _extractor.struct_dict
    udt_dict = _udt_dict if _udt_dict else _extractor.udt_dict

    disc_list = []
    int_list = []
    real_list = []

    for db in db_list:
        for data in db:
            data_type = data.data_type.lower()
            if data_type in DATA_GENERABLE:
                pass
            elif is_udt(data_type):
                pass
            elif is_struct(data_type):
                pass
            else:
                print(f'目前无法处理 {data_type} 类型')


