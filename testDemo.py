# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/15 14:42
import openpyxl
import os

from taggen import udt, intouch, kepserver
from taggen.tag import HMITag, TagList
from definition import Definition

project_path = os.path.dirname(__file__)

workbook_path = project_path + '/defn/defn.xlsx'
workbook = openpyxl.load_workbook(workbook_path)
worksheet = workbook['Sheet1']
ws = workbook.active
list_defn = []


# 从excel获取定义列表
for row_cells in worksheet[2: worksheet.max_row]:
    l = []
    for cell in row_cells:
        l.append(cell.value)
    d = Definition().create_from_list(l)
    list_defn.append(d)
    # print(d.to_list())

# print(list_defn)

# 生成udt合集的字典
# ud = udt.get_udt_from_path(project_path + '\\udt_src')
udt_excel_filename = project_path + '/udt_src/088变量生成器 20200728 - 副本.xlsx'
ud = udt.get_udt_from_excel(udt_excel_filename)
# for u in ud:
#     print('udt类型 {}, {}'.format(ud[u].udt_type, ud[u].name))
#     for t in ud[u].struct:
#         print(t.__dict__)

hmi_disc = []
hmi_int = []
hmi_real = []

hmi_addr_prefix = {
    udt.type_bool.name: 'X',
    udt.type_int.name: 'INT',
    udt.type_real.name: 'REAL',
    udt.type_dint.name: 'DINT',
}

dn_count = 0
# 生成变量
for dn in list_defn:
    dn_count += 1
    udt_type = dn.udt_type
    # print(ud[udt_type].name)
    struct = ud[udt_type].struct
    tag_count = 0
    for udt_tag in ud[udt_type].struct:
        hmi_tag = HMITag()
        hmi_tag.name = '{}_{}_{}'.format(dn.prefix, dn.middle, udt_tag.name)
        hmi_tag.type = udt_tag.type.lower()
        hmi_tag.comment = '{} {}'.format(dn.comment, udt_tag.comment).strip()
        if udt.is_bool(hmi_tag.type):
            udt_tag_offset = float(udt_tag.offset)
        else:
            udt_tag_offset = int(udt_tag.offset)
        hmi_tag.item_name = dn.db_addr + ',' + hmi_addr_prefix[hmi_tag.type] + str(dn.offset + udt_tag_offset)
        hmi_tag.read_only = udt_tag.read_only
        hmi_tag.alarm_state = udt_tag.alarm_state
        hmi_tag.group = dn.prefix
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

path = os.path.dirname(__file__) + '\\test.csv'

intouch.output_csv(tag_list=tag_list, output_path=path, access_name='kep1500', item_use_tag_name=True)

path = os.path.dirname(__file__) + '\\kep_test.csv'
kepserver.output_csv(tag_list=tag_list, output_path=path)

