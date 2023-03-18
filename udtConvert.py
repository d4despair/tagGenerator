# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/14 14:27
import math
import os.path
from openpyxl import Workbook
import udtg

rootdir = os.path.dirname(__file__) + '/udtg'
filenames = []
# 遍历所有文件
for parent, dirnames, filenames in os.walk(rootdir):
    pass

udtList = {}
tagDict = udtg.udt_tag_dict()

typeBool = 'Bool'
typeInt = 'Int'
typeReal = 'Real'


# print(dict.keys(tagDict))

def read_udt():
    print("... reading udtg")


for file in filenames:
    # udt格式
    udtDict = dict(udtg.UDT().__dict__)

    if 'txt' in file:
        print('read: ' + file)
        f = open(rootdir + '/' + file, encoding='utf-8')
        lines = f.readlines()
        print(lines)

        dbFile = 0
        # udtg 类型
        while True:
            temp_line = lines.pop(0)
            if 'DATA_BLOCK' in temp_line:
                dbFile = 1
                break
            if 'TYPE' in temp_line:
                break
        if dbFile == 1:
            print('目前无法处理DB文件')
            continue

        read_udt()
        udtDict['udt_type'] = temp_line[temp_line.find('"') + 1:temp_line.rfind('"')].strip()
        # print(udtDict['udt_type'])

        # udtg 作者 名字 版本 非关键
        listFromDict = list(dict.keys(udtDict))
        for i in range(1, 4):
            temp_line = lines.pop(0)
            udtDict[listFromDict[i]] = temp_line[temp_line.find(':') + 1:temp_line.rfind('\n')].strip()

        # print(udtDict['TYPE'])
        # print(udtDict['AUTHOR'])
        # print(udtDict['NAME'])
        # print(udtDict['VERSION'])

        # 读变量
        firstTag = 1
        offset = 0.0
        dOffsets = {'Bool': 0.1, 'Int': 2, 'Real': 4}
        lTypes = ['Bool', 'Int', 'Real']
        previousType = ''

        while len(lines) > 0:
            temp_line = lines.pop(0)
            if 'END_TYPE' in temp_line:

                break
            elif ':' not in temp_line:
                continue
            # 变量格式
            tagDict = udtg.UDTTag().__dict__
            start_name_index = 0
            end_name_index = temp_line.find(':')
            start_type_index = end_name_index + 1
            end_type_index = temp_line.find(';')
            # 变量名
            tagDict['name'] = temp_line[start_name_index:end_name_index].strip()
            # 变量类型
            tagDict['ttype'] = temp_line[start_type_index:end_type_index].strip()
            # 注释
            if '//' in temp_line:
                tagDict['remark'] = temp_line[temp_line.find('//') + 2: temp_line.find('\n')].strip()
            # 偏移量
            tagType = tagDict['ttype']
            if firstTag == 1:
                firstTag = 0
            else:
                if previousType == typeBool:
                    if tagType == typeBool:
                        if offset * 10 % 10 > 7:
                            offset = math.floor(offset) + 1
                    else:
                        offset = math.floor(offset)
                        if offset % 2 == 1:
                            offset += 1
                        else:
                            offset += 2
            tagDict['offset'] = offset
            offset += dOffsets[tagType]
            previousType = tagType
            udtDict['struct'].append(tagDict)
        if previousType == typeBool:
            offset = math.floor(offset)
            if offset % 2 == 1:
                offset += 1
            else:
                offset += 2
        udtDict['length'] = offset
        print('finished: {}, length {} byte'.format(file, str(offset)))
        f.close()
    if udtDict['udt_type'] != '':
        udtList[udtDict['udt_type']] = udtDict


print('udt数量: ' + str(len(udtList)))
print(list(udtList))

'''
以下是生成excel的部分
'''
print('\n开始生成excel\n')
wb = Workbook()
ws_gather = wb.active
ws_gather.title = 'UDT汇总'
header = list(tagDict)
headerGather = ['UDT_NAME']
headerGather.extend(header)
for udt in udtList:
    print('生成Sheet: ' + udt)
    ws = wb.create_sheet(udt)
    ws.append(header)
    # header_gather = ['UDT_NAME'].extend(header)
    ws_gather.append(headerGather)
    for tag in udtList[udt]['STRUCT']:
        listFromDict = []
        for fd in tagDict:
            listFromDict.append(tag[fd])
        listGather = [udt]
        listGather.extend(listFromDict)
        # print(listFromDict)
        ws.append(listFromDict)
        ws_gather.append(listGather)

wb.save(rootdir + '\\' + 'test.xlsx')
