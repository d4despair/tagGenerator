# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 13:52

def str_to_list(s: str, blank=None, lower_string=False) -> list:
    s = s.strip()
    if blank is not None:
        s = s.replace(' ', blank)
    if lower_string:
        s = s.lower()
    l = list()
    start = 0
    for i in range(s.count(',') + 1):
        end = s.find(',', start, len(s))
        if end == -1:
            l.append(s[start:len(s)].strip())
        else:
            l.append(s[start:end].strip())
        start = end + 1
    return l


def str_to_tuple(s: str, blank=None, lower_string=False) -> tuple:
    return tuple(str_to_list(s, blank, lower_string))


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
    s = 'Tag Name,Address,Data Type,Respect Data Type,Client Access,Scan Rate,Scaling,Raw Low,Raw High,' \
        'Scaled Low,' \
        'Scaled High,Scaled Data Type,Clamp Low,Clamp High,Eng Units,Description,Negate Value '

    t = str_to_tuple(s, blank='_', lower_string=True)
    print(str_to_list(s, blank='_'))
    print_class_init(t)
