# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/23 15:33

import re


def read_db_from_txt(filename: str):
    print('正在处理：{}'.format(filename))
    f = open(filename, 'r', encoding='utf-8')
    lines = f.readlines()
    db_list = []  # DB块列表，由许多DB块组成
    db = []  # DB块
    db_title = ''  # DB块标题
    st_list = []  # 结构列表，由许多结构组成

    # 遍历文件内容
    while True:
        try:
            temp_line = lines.pop(0)
        except IndexError:
            break

        # 查找DB块
        if res := re.search(r'DATA_BLOCK "(.*)"', temp_line):
            db_title = res[1]
            db = []

        # 查找变量
        if db_data := parse_data(temp_line, db_title):
            db.append(db_data)

        # 查找结构

        if db_struct := parse_struct(temp_line, db_title, lines, st_list):
            db.append(db_struct[0])  # DB行
            st_list.append(db_struct[1])  # 结构

        # 结束DB块
        if re.search(r'END_DATA_BLOCK', temp_line):
            if len(db) > 0:
                db_list.append(db)
            else:
                print(f"无法添加，DB名称：{db_title} 数据个数：0")

            # 创建新DB
            db = []

    # print(db_list)
    [print(f'DB名称：\'{db[0][0]}\' 数据个数：{len(db)}') for db in db_list]
    print(f'处理完成，总共 {len(db_list)} 个DB')
    [print(f'结构名称：\'{st[0][0]}\' 数据个数：{len(st)}') for st in st_list]
    print(f'处理完成，总共 {len(st_list)} 个结构')

    return db_list, st_list


# 提取注释
def get_remark(string: str):
    if res := re.search(r'//(.*)', string):
        return res.group(1).strip()
    else:
        return ''


# 提取变量名
def get_name(string: str):
    if res := re.search(r'(.*){(.*)}', string):
        return res.group(1).strip()
    else:
        return string.strip()


# 解析结构，返回（结构变量，结构列表）
def parse_struct(line: str, title: str, lines: list, st_list: list):
    parent_data = [title]
    self_st = []
    child_st = []
    child_list = None
    if res := re.search(r'(.*): (Struct.*)', line):
        # 结构名
        st_name = get_name(res.group(1))
        parent_data.append(st_name)

        # 结构类型
        st_type = f'{title}.{parent_data[-1]}'
        parent_data.append(st_type)

        # 结构注释
        st_remark = res.group(2).strip()
        parent_data.append(get_remark(st_remark))
    else:
        return

    while not re.search(r'end_struct', line, re.I):
        try:
            line = lines.pop(0)
        except IndexError:
            break

        # 结构里的数据
        if st_data := parse_data(line, st_type):
            self_st.append(st_data)

        # 嵌套结构
        if child_struct := parse_struct(line, st_type, lines, st_list):
            child_st.append(child_struct[0])  # 结构添加一个数据
            self_st.extend(child_st)  # 结构添加所有子数据
            child_list = child_struct[1].copy()
            if child_list:
                st_list.insert(0, child_list)
            print(child_list)
    return parent_data, self_st, child_list


def parse_data(line: str, parent_title: str):
    # 查找变量
    db_data = [parent_title]
    if res := re.search(r'(.*) : (.*);(.*)', line):
        # 变量名
        data_name_raw = res.group(1).strip()
        db_data.append(get_name(data_name_raw))

        # 变量类型
        data_type_raw = res.group(2).strip()
        db_data.append(data_type_raw)

        # 变量注释
        data_remark_raw = res.group(3).strip()
        db_data.append(get_remark(data_remark_raw))
        return db_data
    else:
        return


def test():
    # filepath = 'D:\\工作资料\\10-宝尔康资料\\tia_db\\'
    filepath = 'D:\\工作资料\\11-PYTHON测试\\'
    filename = 'S_HP'
    db_list, st_list = read_db_from_txt(f'{filepath}{filename}.db')
    from taggen import write_db_to_excel
    from taggen import add_offset
    [add_offset(st) for st in st_list]
    write_db_to_excel(f'{filepath}{filename}.xlsx', db_list, st_list)


if __name__ == '__main__':
    test()
