# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/9/12 9:40

import csv
import re
from xml.etree import ElementTree as ET

import taggen.intouch
import taggen.kepserver
from taggen.tag import HMITag, TagList

MCGS_FIELD_MAPPING = {
    '通道号': 0,
    '变量名': 1,
    '变量类型': 2,
    '通道名称': 3,
    '读写类型': 4,
    '寄存器名称': 5,
    '数据类型': 6,
    '寄存器地址': 7,
    '地址偏移': 8,
    '通道采集频率': 9,
    '通道处理': 10
}

class MCGSDriver:
    def __init__(self, path, name, version):
        self.path = path
        self.name = name
        self.version = version


class MCGSDevice:
    def __init__(self, name, driver_path, driver_name, driver_version):
        self.name = name
        self.driver = MCGSDriver(driver_path, driver_name, driver_version)


class MCGSTag:
    def __init__(self, tag_name, var_type, ch_name, read_type, register, data_type, addr_offset, ch_frequency,
                 ch_process):
        self.tag_name = tag_name
        self.var_type = var_type
        self.ch_name = ch_name
        self.read_type = read_type
        self.register = register
        self.data_type = data_type
        self.addr_offset = addr_offset
        self.ch_frequency = ch_frequency
        self.ch_process = ch_process


class MCGSFile:
    def __init__(self, filepath):
        self.filepath = filepath
        self.header = None
        self.data_header = None
        self.data_list = None
        self.parse()

    def parse(self):
        self.header = []
        self.data_list = []
        with open(self.filepath, mode='r', encoding='ANSI') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if reader.line_num <= 4:
                    self.header.append(row)
                elif reader.line_num == 5:
                    self.data_header = row
                else:
                    self.data_list.append(row)


def read_csv(filename):
    datas = []
    with open(filename, mode='r', encoding='ANSI') as f:
        reader = csv.reader(f)
        for row in reader:
            datas.append(row)
            # print(row)
    return datas


def read_alarms(filename):
    alarms = {}
    etree = ET.parse(filename)
    root = etree.getroot()
    for child in root:
        if child.attrib['ID']:
            tagname = child.find('变量名称').text
            alarms[tagname] = {}
            for son in child:
                alarms[tagname][son.tag] = son.text
    return alarms


def translate(data_list, prefix='', alarms=None):
    taglist = TagList()
    waste = []
    for data in data_list:
        new_dict = {}
        # print(data)
        raw_name = data[MCGS_FIELD_MAPPING['变量名']]
        new_dict['name'] = f'{prefix}_{raw_name}' if prefix else raw_name
        # 把 Screw改成 M0
        if 'Screw' in new_dict['name']:
            print(new_dict['name'])
            new_dict['name'] = new_dict['name'].replace('Screw', 'M0')
        new_dict['data_type'] = translate_data_type(data[MCGS_FIELD_MAPPING['数据类型']])
        # print(data[MCGS_FIELD_MAPPING['数据类型']], new_dict['data_type'])

        if alarms:
            try:
                new_dict['comment'] = alarms[raw_name]['报警描述']
                new_dict['alarm_state'] = 1
            except KeyError:
                new_dict['comment'] = raw_name
                new_dict['alarm_state'] = 0
        new_dict['read_only'] = 1 if data[MCGS_FIELD_MAPPING['读写类型']] == '只读' else 0
        new_dict['item_name'] = translate_item_name(data[MCGS_FIELD_MAPPING['通道名称']], new_dict['data_type'])
        new_dict['group'] = prefix

        hmitag = HMITag(**new_dict)
        # print(hmitag)

        if len(hmitag.name) > 30:
            print(f'名称过长: {hmitag.name}, 长度{len(hmitag.name)}')
            waste.append(hmitag.name)
        else:
            taglist.append(hmitag)
    print(waste)
    return taglist


def translate_item_name(item_name, data_type):
    if data_type == 'bool':
        res = re.search(r'(DB\d+):(\d+\.\d)', item_name)

        offset = str(float(res.group(2)))
        type_prefix = 'X'
    else:
        res = re.search(r'(DB\d+):(\w+)(\d+)', item_name)
        offset = str(int(res.group(3)))
        type_prefix = data_type.upper()

    db_addr = res.group(1)

    return f'{db_addr},{type_prefix}{offset}'


def translate_data_type(data_type: str):

    if data_type.startswith('16位'):
        new_type = 'int'
    elif data_type.startswith('32位'):
        new_type = 'real'
    else:
        new_type = 'bool'
    # print(data_type, new_type)
    return new_type


if __name__ == '__main__':
    mcgs_data_file = 'D:\\工作资料\\09-待分类\\Siemens_1200.csv'
    mcgs_alarm_file = 'D:\\工作资料\\09-待分类\\mcgs_alarm.xml'
    mcgs_alarms = read_alarms(mcgs_alarm_file)
    mcgs = MCGSFile(mcgs_data_file)
    short_name = 'T'
    access_name = 'TAL'
    taglist = translate(mcgs.data_list, prefix=access_name, alarms=mcgs_alarms)
    intouch_tal_db = f'D:\\工作资料\\09-待分类\\intouch_{access_name}_db.csv'
    kepserver_tal_db = f'D:\\工作资料\\09-待分类\\kepserver_{access_name}_db.csv'
    taggen.intouch.output_csv(taglist, intouch_tal_db, mode='replace', item_use_tag_name=True, access_name=access_name)
    taggen.kepserver.output_csv(taglist, kepserver_tal_db)

    # print(translate_item_name('读写DB19:000.0', 'bool'))
    # print(translate_item_name('读写DB257:WUB082', 'int'))
    # print(translate_item_name('读写DB257:DF106', 'real'))

