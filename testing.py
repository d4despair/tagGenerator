# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/18 16:21

# snap7 连接测试
def snap7_test():
    import snap7

    plc_obj = snap7.client.Client()
    plc_obj.connect('192.168.0.100', 0, 1)
    print(f'连接状态： {plc_obj.get_connected()}')
    # plc_obj.disconnect()
    # print((f'连接状态： {plc_obj.get_connected()}'))
    data = plc_obj.db_read(79, 74, 4)
    print(snap7.util.get_real(data, 0))


def list_pop(l: list):
    print(l.pop(0))
    l.append(6)

l1 = [1, 2, 3, 4]
print(l1)
list_pop(l1)
print(l1)
