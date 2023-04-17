# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 15:33

import re


def read_db_from_txt(filename: str):
    print('正在处理：{}'.format(filename))
    f = open(filename, 'r', encoding='utf-8')
    lines = f.readlines()
    db_list = []

    # 遍历文件内容
    while True:
        try:
            temp_line = lines.pop(0)
        except IndexError:
            break

        # 查找DB块
        if res := re.search(r'DATA_BLOCK "(.*)"', temp_line):
            title = res[1]
            db = []
            db_line = [title]
            # print(f'正在处理: {title} ...')

        # 查找变量
        if res := re.search(r'(.*) : "(.*)";\s+// (.*)', temp_line):
            for i in res.groups():
                if res := re.search(r'"(.*)"', i):
                    db_line.append(res.groups()[0])
                else:
                    db_line.append(i.strip())
            # [db_line.append(i.strip()) for i in res.groups()]
            db.append(db_line)
            db_line = [title]
            # print(res)

        # 结束DB块
        if re.search(r'END_DATA_BLOCK', temp_line):
            db_list.append(db)
            db = []
    # print(db_list)

    [print(f'DB名称：\'{db[0][0]}\' 数据个数：{len(db)}') for db in db_list]
    print(f'处理完成，总共 {len(db_list)} 个DB')

    return db_list


def test():
    filepath = 'D:\\工作资料\\10-宝尔康资料\\tia_db\\'
    filename = 'valve'
    db_list = read_db_from_txt(f'{filepath}{filename}.db')
    from taggen.udt.writer.datablock import write_db_to_excel
    write_db_to_excel(f'{filepath}{filename}.xlsx', db_list)


if __name__ == '__main__':
    test()

#
# def get_udt_from_txt(filename: str) -> UDT | None:
#     if filename.endswith('.txt'):
#         print('正在处理: {}'.format(filename))
#         f = open(filename, 'r', encoding='utf-8')
#         lines = f.readlines()
#
#         while True:
#             temp_line = lines.pop(0)
#             if 'DATA_BLOCK' in temp_line:
#                 print('目前无法处理DB文件')
#                 return
#             if 'TYPE' in temp_line:
#                 break
#
#         new_udt = UDT()
#         struct = []
#         # udt 类型
#         new_udt.udt_type = temp_line[temp_line.find('"') + 1:temp_line.rfind('"')].strip()
#
#         udt_fd = list(new_udt.__dict__)
#         # print(udt_fd)
#
#         # udt 作者 描述 版本号
#         for i in range(1, 4):
#             temp_line = lines.pop(0)
#             # print('udt_fd[{}]: , new_udt[{}]'.format(i, udt_fd[i])
#             new_udt[udt_fd[i]] = temp_line[temp_line.find(':') + 1:temp_line.rfind('\n')].strip().lower()
#
#         # 读变量
#         offset = 0
#         prev_type = ''
#         while len(lines) > 0:
#             temp_line = lines.pop(0)
#             if 'END_TYPE' in temp_line:
#                 break
#             elif ':' not in temp_line:
#                 continue
#
#             new_tag = _txt_read_tag(temp_line)
#
#             if tagtype.is_bool(prev_type):
#                 if tagtype.is_bool(new_tag.type):
#                     if offset * 10 % 10 > 7:
#                         offset = math.floor(offset) + 1
#                 else:
#                     offset = math.floor(offset)
#                     if offset % 2 == 1:
#                         offset += 1
#                     else:
#                         offset += 2
#             if tagtype.is_bool(new_tag.type):
#                 new_tag.offset = '%.1f' % offset
#             else:
#                 new_tag.offset = '%d' % offset
#
#             offset += tagtype.type_length(new_tag.type)
#             prev_type = new_tag.type
#             struct.append(new_tag)
#             new_udt.struct = struct
#
#         # udt 长度
#         if tagtype.is_bool(prev_type):
#             offset = math.floor(offset)
#             if offset % 2 == 1:
#                 offset += 1
#             else:
#                 offset += 2
#         new_udt.length = offset
#
#         f.close()
#         print('处理完毕')
#         return new_udt
#     else:
#         print('无法处理: {}'.format(filename))
#
#     return
