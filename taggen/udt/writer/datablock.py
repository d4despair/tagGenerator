# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/4/14 11:39

from openpyxl import Workbook

DB_HEADER = ['数据块', '数据名称', '数据类型', '注释']
ST_HEADER = ['所属结构', '数据名称', '数据类型', '注释']


def write_db_to_excel(filename: str, db_list: list, st_list: list = None):
    wb = Workbook()

    ws = wb.active
    ws.append(DB_HEADER)
    for db in db_list:
        for db_line in db:
            ws.append(db_line)
    ws.title = 'datablock'

    ws = wb.create_sheet('struct', 1)
    ws.append(ST_HEADER)
    if st_list:
        st_list.sort(reverse=1)
        for st in st_list:
            for st_line in st:
                ws.append(st_line)
    wb.save(filename)
    wb.close()
    print(f'文件保存至：{filename}')
