import sys
import os

sys.path.append(os.path.dirname(__file__).replace(r'\taggen', ''))

import logging

import intouch
import kepserver

from taggen.udt.extractor import DBExtractor
from taggen.udt.taglist import TagList
from taggen.udt.dbwriter import DBWriter


def test2():
    filepath = 'D:\\工作资料\\11-PYTHON测试\\'
    logging.basicConfig(filename=filepath + 'example.log', level=logging.INFO)
    logging.info('log start')
    extractor = DBExtractor(filepath + 'tia_file\\',
                            r"D:\工作资料\11-PYTHON测试\可导入文件\DB地址定义.xlsx")
    # extractor = DBExtractor(filepath + 'tia_file\\')
    # extractor.read_db_defn(r"D:\工作资料\11-PYTHON测试\DB地址定义.xlsx")
    # extractor.read_udt_from_excel(r"D:\工作资料\10-宝尔康资料\026-5UDT.xlsx")

    writer = DBWriter()
    writer.write_defn_to_excel(extractor, filename=filepath + 'db_defn2.xlsx')

    taglist = TagList()
    for db in extractor.db:
        taglist.traverse(db, extractor.udt_dict, extractor.struct_dict)

    project_path = filepath
    sheet_name = 'test'
    path = project_path + f'\\可导入文件\\intouch_{sheet_name}_db.csv'
    intouch.output_csv(tag_list=taglist, output_path=path, access_name='kep1500', item_use_tag_name=True,
                       mode='replace')
    path = project_path + f'\\可导入文件\\kep_{sheet_name}_db.csv'
    kepserver.output_csv(tag_list=taglist, output_path=path)


if __name__ == '__main__':
    test2()
