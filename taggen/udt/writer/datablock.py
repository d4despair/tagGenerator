# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/4/14 11:39

from openpyxl import Workbook


def write_db_to_excel(filename: str, db_list):
    wb = Workbook()
    ws = wb.active
    for db in db_list:
        for db_line in db:
            ws.append(db_line)
    wb.save(filename)
    print(f'文件保存至：{filename}')
