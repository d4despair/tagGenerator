# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/18 16:21

from taggen.tag import Tag

import keyword
print(type(keyword.kwlist))
print(keyword.kwlist)
t = Tag('name', 'type', 'comment')
print(t)
print(t.__init_subclass__())


# snap7 连接测试
def snap7_test():
    import snap7

    plcobj = snap7.client.Client()
    plcobj.connect('192.168.0.100', 0, 1)
    print((f'连接状态： {plcobj.get_connected()}'))
    # plcobj.disconnect()
    # print((f'连接状态： {plcobj.get_connected()}'))
    data = plcobj.db_read(79, 74, 4)

    print(snap7.util.get_real(data, 0))

