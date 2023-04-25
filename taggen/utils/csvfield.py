# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 13:52

import re


def str_to_list(string: str, pattern=',', blank=None, lower=False) -> list:
    """
    将字符串转成列表

    raw_string = 'Tag Name,Address,Data Type,Respect Data Type,Client Access'

    t = str_to_tuple(raw_string, blank='_', lower=True)

    返回内容 ['tag_name', 'address', 'data_type', 'respect_data_type', 'client_access']

    :param pattern: 分隔符
    :param string: 带有一定格式的字符串
    :param blank: 字符，用于替换空白格
    :param lower: 是否转换成小写字母
    :return: 字符串列表
    """
    string = string.strip()
    if blank is not None:
        string = string.replace(' ', blank)
    if lower:
        string = string.lower()
    return re.split(pattern, string)


def str_to_tuple(string: str, pattern=',', blank=None, lower=False) -> tuple:
    """
    将有一定格式的字符串转成元组

    :param pattern: 分隔符
    :param string: 带有一定格式的字符串
    :param blank: 字符，用于替换空白格
    :param lower: 是否转换成小写字母
    :return: 字符串元组
    """
    return tuple(str_to_list(string, pattern, blank, lower))


def print_class_init(t: tuple):
    print('复制一下文字')
    print('__slots__ = (')
    for i in t:
        print('\t\'{}\','.format(i))
    print(')')
    print('')
    init_txt = 'def __init__'
    s = '(self'
    for i in t:
        s += ', {}=None'.format(i)
    s += '):'
    print(init_txt + s)
    for i in t:
        print('\tself.{} = {}'.format(i, i))


# test
if __name__ == '__main__':
    print('========= csvfield.py 测试内容 =========')
    raw_string = 'Tag Name,Address,Data Type,Respect Data Type,Client Access'
    print(str_to_list(raw_string, blank='_', lower=True))
    print(str_to_tuple(raw_string, blank='_', lower=True))
    print('========= csvfield.py 测试内容 =========')
