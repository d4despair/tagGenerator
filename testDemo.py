# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/15 14:42
import openpyxl
import os
import re
from taggen import udt, intouch, kepserver
from taggen.tag import HMITag, TagList
from definition import Definition

project_path = r'D:\工作资料\10-宝尔康资料'

# workbook_path = project_path + '/defn/defn.xlsx'
workbook_path = project_path + r'/宝尔康干燥传感器.xlsx'
workbook = openpyxl.load_workbook(workbook_path, data_only=True)
sheet_name = 'defn_analog'
# sheet_name = 'defn_valve'
worksheet = workbook[sheet_name]
ws = workbook
list_defn = []

# 从excel获取定义列表
for row_cells in worksheet[2: worksheet.max_row]:
    l = []
    for cell in row_cells:
        l.append(cell.value)
        if len(l) == 6:
            break
    d = Definition(*l)
    # print(d.udt_type)
    list_defn.append(d)

# 生成udt合集的字典
# ud = udt.get_udt_from_path(project_path + '\\udt_src')
udt_excel_filename = os.path.dirname(__file__) + '/udt_src/026-5UDT.xlsx'
ud = udt.get_udt_from(udt_excel_filename)

hmi_disc = []
hmi_int = []
hmi_real = []

hmi_addr_prefix = {
    'bool': 'X',
    'int': 'INT',
    'real': 'REAL',
    'dint': 'DINT',
}

data_length = {
    'bool': 0.1,
    'int': 2,
    'real': 4,
    'dint': 4,
}

dn_count = 0
# 生成变量
for dn in list_defn:

    if dn.to_list()[0] is None:
        continue
    if re.search('spare', dn.prefix, re.I):
        continue
    # print(dn.to_list())
    dn_count += 1
    udt_type = dn.udt_type
    # print(ud[udt_type].name)
    # print(udt_type)
    struct = ud[udt_type].struct
    tag_count = 0

    for udt_tag in ud[udt_type].struct:
        hmi_tag = HMITag()
        if dn.middle:
            print(dn.middle)

            hmi_tag.name = '{}_{}_{}'.format(dn.prefix, dn.middle, udt_tag.name)
        else:
            hmi_tag.name = '{}_{}'.format(dn.prefix, udt_tag.name)
        # print(hmi_tag.name)
        hmi_tag.type = udt_tag.type.lower()
        hmi_tag.comment = '{} {}'.format(dn.comment, udt_tag.comment).strip()
        if udt.is_bool(hmi_tag.type):
            udt_tag_offset = float(udt_tag.offset)
        else:
            udt_tag_offset = int(udt_tag.offset)
        # print(hmi_addr_prefix[hmi_tag.type])
        # print(dn.offset)
        hmi_tag.item_name = dn.db_addr + ',' + hmi_addr_prefix[hmi_tag.type] + str(dn.offset + udt_tag_offset)
        hmi_tag.read_only = udt_tag.read_only
        hmi_tag.alarm_state = udt_tag.alarm_state
        #### 报警组
        # hmi_tag.group = dn.prefix
        hmi_tag.group = 'DRY'
        tag_count += 1
        # print(hmi_tag.type)
        if udt.is_bool(hmi_tag.type):
            hmi_disc.append(hmi_tag)
        elif udt.is_int(hmi_tag.type):
            hmi_int.append(hmi_tag)
        else:
            hmi_real.append(hmi_tag)
        # print(hmi_tag.__dict__)
    print('{}: {}_{} {} 类型: {} 生成 {} 个变量'.format(dn_count, dn.prefix, dn.middle, dn.comment, dn.udt_type, tag_count))
    # print(dn.udt_type)

tag_list = TagList(hmi_disc, hmi_int, hmi_real)

path = project_path + f'\\intouch_{sheet_name}_db.csv'

intouch.output_csv(tag_list=tag_list, output_path=path, access_name='kep1200', item_use_tag_name=True)

path = project_path + f'\\kep_{sheet_name}_db.csv'
kepserver.output_csv(tag_list=tag_list, output_path=path)
