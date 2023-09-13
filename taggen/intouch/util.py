# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/4/12 9:13

import re

INTOUCH_TRUE_FALSE = {
    True: 'Yes',
    False: 'No',
    1: 'Yes',
    0: 'No',
    '是': 'Yes',
    '否': 'No',
}


def repl(m):
    g = m.group(0)
    return g[0] + '_' + g[1:len(g)].lower()


def _repl(m):
    g = m.group(0)
    return g.replace('_', '')


def camel_string_to_python(camel_string: str):
    camel_string = re.sub(r'\w([A-Z][a-z])', repl, camel_string)
    camel_string = re.sub(r'[a-z][A-Z]+', repl, camel_string).lower()
    python_string = re.sub(r'[a-z]alarm', repl, camel_string)
    python_string = re.sub(r'[lh][oi]_[lh][oi]', _repl, python_string)
    return python_string


def camel_list_to_python(camel_list: iter):
    python_style = []
    for camel_string in camel_list:
        python_string = camel_string_to_python(camel_string)
        # camel_string = re.sub(r'\w([A-Z][a-z])', repl, camel_string)
        # camel_string = re.sub(r'[a-z][A-Z]+', repl, camel_string).lower()
        # python_string = re.sub(r'[a-z]alarm', repl, camel_string)
        # python_string = re.sub(r'[lh][oi]_[lh][oi]', _repl, python_string)
        python_style.append(python_string)
    return python_style


def print_slots(slots):
    print(f'\t__slots__ = (')
    for slot in slots:
        print(f"\t\t'{slot}',")
    print(f'\t)')


def print_init(slots):
    print(f'\tdef __init__(cls', end='')
    for slot in slots:
        print(f" ,{slot} = ''", end='')
    print(f'):')
    for slot in slots:
        print(f'\t\tself.{slot} = {slot}')


def print_class_string(class_name, slots):
    slots[0] = slots[0].replace(':', '')
    print(f'\n# ========================== {class_name} 开始 ==========================\n\n')
    print(f'class {class_name}:')
    print_slots(slots)
    print()
    print_init(slots)
    print(f'\n# ========================== {class_name} 结束 ==========================\n')


def get_string_list(obj):
    return [obj.__getattribute__(slot) for slot in obj.__slots__].__str__()


class StringListObject:
    def __str__(cls):
        return [cls.__getattribute__(slot) for slot in cls.__slots__].__str__()

    @property
    def csv_format(cls):
        return [cls.__getattribute__(slot) for slot in cls.__slots__]


def test():
    print(f'测试 {camel_string_to_python.__name__} 开始')
    camel_string = 'ToYoungToSimple'
    print(f'{camel_string} -> {camel_string_to_python(camel_string)}')
    print(f'测试 {camel_string_to_python.__name__} 结束')
    print()

    header_list = []
    # 生成标题列表
    from intouch import FORM
    for header in FORM:
        python_style = camel_list_to_python(header)
        class_name = header[0].replace(':', '')
        camel_name = python_style[0].upper().replace(':', '') + '_HEADER'
        header_list.append(camel_name)
        python_name = camel_name + '_PYTHON'
        zip_name = camel_name.replace('HEADER', 'DICT')
        print(f'{camel_name} = {header}')
        print(f'{python_name} = {python_style}')
        print(f'{zip_name} = ' + '{' + f'python: camel for python, camel in zip({python_name}, {camel_name})' + '}')
        print()

    print('[', end='')
    [print(header, end=', ') for header in header_list]
    print(']')


if __name__ == '__main__':
    test()
