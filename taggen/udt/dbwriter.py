# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/4/28 22:58

from openpyxl import Workbook

from taggen.udt.datablock import DataBlock
from taggen.udt.udt import UDT
from taggen.udt.s7struct import S7Struct
from taggen.udt.extractor import DBExtractor
from taggen.udt.util import SHEET_UDT_CATALOG, SHEET_UDT_CONTENT

DB_HEADER = ['前缀', '位号', '类型', '位号描述', '所属DB', '生成偏移量', 'DB名称', '描述', '可否生成', '设定值']
UDT_HEADER = ['UDT', '后缀', '类型', '偏移量', '默认值', '临时1', '临时2', '临时3', '临时4', '临时5', '临时6', '描述', '报警', '只读', '别名', '是否创建']
STRUCT_HEADER = ['所属结构', '后缀', '类型', '偏移量', '默认值', '临时1', '临时2', '临时3', '临时4', '临时5', '临时6', '描述', '报警', '只读']
UDT_CATALOG_HEADER = ['UDT', '长度', '描述', '别名', '版本号']

HEADER = {
    DataBlock.__name__: DB_HEADER,
    UDT.__name__: UDT_HEADER,
    S7Struct.__name__: STRUCT_HEADER,
}


class DBWriter:
    """
    将提取的DB写入到excel

    例子：

    e = DBExtractor('文件目录')

    writer = DBWriter()

    writer.write_defn_to_excel(e)

    writer.save('excel保存地址')
    """
    _wb: Workbook

    def __init__(self):
        self._wb = Workbook()
        if 'Sheet' in self._wb.sheetnames:
            self._wb.remove(self._wb['Sheet'])

    def write_defn_to_excel(self, _extractor, filename=None):
        if isinstance(_extractor, DBExtractor):
            self.write_list_to_excel(_extractor.db, 'data_block')
            if _extractor.udt:
                self.write_list_to_excel(_extractor.udt, 'udt')
            if _extractor.struct:
                self.write_list_to_excel(_extractor.struct, 'struct')
            if filename:
                self.save(filename)
                print(f'保存至：{filename}')
        else:
            raise ValueError

    def write_list_to_excel(self, list_s7struct: list[DataBlock | UDT | S7Struct], sheet_name: str = None):
        wb = self._wb
        ws = wb.create_sheet(sheet_name) if sheet_name else wb.active
        # ws.append(DB_HEADER)
        ws.append(HEADER[list_s7struct[0].__class__.__name__])
        if isinstance(list_s7struct[0], DataBlock):
            for data_list in list_s7struct:
                for data in data_list.data:
                    ws.append(data.csv_format())
        else:
            for data_list in list_s7struct:
                for data in data_list.data:
                    ws.append(data.udt_format())

    @staticmethod
    def write_udt_to_excel(_extractor, filename):
        wb = Workbook()
        wb.remove(wb['Sheet'])
        ws_catalog = wb.create_sheet(SHEET_UDT_CATALOG, 0)
        ws_content = wb.create_sheet(SHEET_UDT_CONTENT, 1)
        if isinstance(_extractor, DBExtractor):
            if _extractor.udt:
                ws_catalog.append(UDT_CATALOG_HEADER)
                ws_content.append(UDT_HEADER)
                for udt in _extractor.udt:
                    ws_catalog.append(udt.csv_format())
                    for data in udt.data:
                        ws_content.append(data.udt_format())
                if filename:
                    wb.save(filename)
                    wb.close()
            else:
                raise ValueError

    @staticmethod
    def write_xlsm_to_excel(_extractor, filename):
        wb = Workbook()
        wb.remove(wb['Sheet'])
        ws = wb.create_sheet('给变量生成起用', 0)
        if isinstance(_extractor, DBExtractor):
            ws.append([
                '前缀',
                '位号',
                '类型',
                '位号描述',
                '所属DB',
                '生成偏移量',
                '是否UDT',
                '所属结构',
                '原始名称',
            ])
            if _extractor.db:
                for db in _extractor.db:
                    for data in db.data:
                        ws.append(data.xlsm_format())

            if _extractor.struct:
                for st in _extractor.struct:
                    for data in st.data:
                        ws.append(data.xlsm_format())
            if filename:
                wb.save(filename)
                wb.close()
        else:
            raise ValueError

    def save(self, filename):
        wb = self._wb
        # ws = wb['Sheet']
        # wb.remove(ws)
        wb.save(filename)
        wb.close()
