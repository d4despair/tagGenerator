# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/17 15:44
import csv
from taggen.tag import tagtype
from taggen.tag import TagList, HMITag
from taggen.udt.util import is_bool

# mode_text = ':mode=REPLACE,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\r\n'
FORM = [[':IOAccess', 'Application', 'Topic', 'AdviseActive', 'DDEProtocol', 'SecApplication', 'SecTopic',
         'SecAdviseActive', 'SecDDEProtocol', 'FailoverExpression', 'FailoverDeadband', 'DFOFlag', 'FBDFlag',
         'FailbackDeadband',
         ],
        [':AlarmGroup', 'Group', 'Comment', 'EventLogged', 'EventLoggingPriority', 'LoLoAlarmDisable',
         'LoAlarmDisable', 'HiAlarmDisable', 'HiHiAlarmDisable', 'MinDevAlarmDisable', 'MajDevAlarmDisable',
         'RocAlarmDisable', 'DSCAlarmDisable', 'LoLoAlarmInhibitor', 'LoAlarmInhibitor', 'HiAlarmInhibitor',
         'HiHiAlarmInhibitor', 'MinDevAlarmInhibitor', 'MajDevAlarmInhibitor', 'RocAlarmInhibitor',
         'DSCAlarmInhibitor',
         ],
        [':IODisc', 'Group', 'Comment', 'Logged', 'EventLogged', 'EventLoggingPriority', 'RetentiveValue',
         'InitialDisc', 'OffMsg', 'OnMsg', 'AlarmState', 'AlarmPri', 'DConversion', 'AccessName', 'ItemUseTagname',
         'ItemName', 'ReadOnly', 'AlarmComment', 'AlarmAckModel', 'DSCAlarmDisable', 'DSCAlarmInhibitor',
         'SymbolicName',
         ],
        [':MemoryInt', 'Group', 'Comment', 'Logged', 'EventLogged', 'EventLoggingPriority', 'RetentiveValue',
         'RetentiveAlarmParameters', 'AlarmValueDeadband', 'AlarmDevDeadband', 'EngUnits', 'InitialValue',
         'MinValue', 'MaxValue', 'Deadband', 'LogDeadband', 'LoLoAlarmState', 'LoLoAlarmValue', 'LoLoAlarmPri',
         'LoAlarmState', 'LoAlarmValue', 'LoAlarmPri', 'HiAlarmState', 'HiAlarmValue', 'HiAlarmPri',
         'HiHiAlarmState', 'HiHiAlarmValue', 'HiHiAlarmPri', 'MinorDevAlarmState', 'MinorDevAlarmValue',
         'MinorDevAlarmPri', 'MajorDevAlarmState', 'MajorDevAlarmValue', 'MajorDevAlarmPri', 'DevTarget',
         'ROCAlarmState', 'ROCAlarmValue', 'ROCAlarmPri', 'ROCTimeBase', 'AlarmComment', 'AlarmAckModel',
         'LoLoAlarmDisable', 'LoAlarmDisable', 'HiAlarmDisable', 'HiHiAlarmDisable', 'MinDevAlarmDisable',
         'MajDevAlarmDisable', 'RocAlarmDisable', 'LoLoAlarmInhibitor', 'LoAlarmInhibitor', 'HiAlarmInhibitor',
         'HiHiAlarmInhibitor', 'MinDevAlarmInhibitor', 'MajDevAlarmInhibitor', 'RocAlarmInhibitor', 'SymbolicName',
         ],
        [':IOInt', 'Group', 'Comment', 'Logged', 'EventLogged', 'EventLoggingPriority', 'RetentiveValue',
         'RetentiveAlarmParameters', 'AlarmValueDeadband', 'AlarmDevDeadband', 'EngUnits', 'InitialValue', 'MinEU',
         'MaxEU', 'Deadband', 'LogDeadband', 'LoLoAlarmState', 'LoLoAlarmValue', 'LoLoAlarmPri', 'LoAlarmState',
         'LoAlarmValue', 'LoAlarmPri', 'HiAlarmState', 'HiAlarmValue', 'HiAlarmPri', 'HiHiAlarmState',
         'HiHiAlarmValue', 'HiHiAlarmPri', 'MinorDevAlarmState', 'MinorDevAlarmValue', 'MinorDevAlarmPri',
         'MajorDevAlarmState', 'MajorDevAlarmValue', 'MajorDevAlarmPri', 'DevTarget', 'ROCAlarmState',
         'ROCAlarmValue', 'ROCAlarmPri', 'ROCTimeBase', 'MinRaw', 'MaxRaw', 'Conversion', 'AccessName',
         'ItemUseTagname', 'ItemName', 'ReadOnly', 'AlarmComment', 'AlarmAckModel', 'LoLoAlarmDisable',
         'LoAlarmDisable', 'HiAlarmDisable', 'HiHiAlarmDisable', 'MinDevAlarmDisable', 'MajDevAlarmDisable',
         'RocAlarmDisable', 'LoLoAlarmInhibitor', 'LoAlarmInhibitor', 'HiAlarmInhibitor', 'HiHiAlarmInhibitor',
         'MinDevAlarmInhibitor', 'MajDevAlarmInhibitor', 'RocAlarmInhibitor', 'SymbolicName'
         ],
        [':MemoryReal', 'Group', 'Comment', 'Logged', 'EventLogged', 'EventLoggingPriority', 'RetentiveValue',
         'RetentiveAlarmParameters', 'AlarmValueDeadband', 'AlarmDevDeadband', 'EngUnits', 'InitialValue',
         'MinValue', 'MaxValue', 'Deadband', 'LogDeadband', 'LoLoAlarmState', 'LoLoAlarmValue', 'LoLoAlarmPri',
         'LoAlarmState', 'LoAlarmValue', 'LoAlarmPri', 'HiAlarmState', 'HiAlarmValue', 'HiAlarmPri',
         'HiHiAlarmState', 'HiHiAlarmValue', 'HiHiAlarmPri', 'MinorDevAlarmState', 'MinorDevAlarmValue',
         'MinorDevAlarmPri', 'MajorDevAlarmState', 'MajorDevAlarmValue', 'MajorDevAlarmPri', 'DevTarget',
         'ROCAlarmState', 'ROCAlarmValue', 'ROCAlarmPri', 'ROCTimeBase', 'AlarmComment', 'AlarmAckModel',
         'LoLoAlarmDisable', 'LoAlarmDisable', 'HiAlarmDisable', 'HiHiAlarmDisable', 'MinDevAlarmDisable',
         'MajDevAlarmDisable', 'RocAlarmDisable', 'LoLoAlarmInhibitor', 'LoAlarmInhibitor', 'HiAlarmInhibitor',
         'HiHiAlarmInhibitor', 'MinDevAlarmInhibitor', 'MajDevAlarmInhibitor', 'RocAlarmInhibitor', 'SymbolicName',
         ],
        [':IOReal', 'Group', 'Comment', 'Logged', 'EventLogged', 'EventLoggingPriority', 'RetentiveValue',
         'RetentiveAlarmParameters', 'AlarmValueDeadband', 'AlarmDevDeadband', 'EngUnits', 'InitialValue', 'MinEU',
         'MaxEU', 'Deadband', 'LogDeadband', 'LoLoAlarmState', 'LoLoAlarmValue', 'LoLoAlarmPri', 'LoAlarmState',
         'LoAlarmValue', 'LoAlarmPri', 'HiAlarmState', 'HiAlarmValue', 'HiAlarmPri', 'HiHiAlarmState',
         'HiHiAlarmValue', 'HiHiAlarmPri', 'MinorDevAlarmState', 'MinorDevAlarmValue', 'MinorDevAlarmPri',
         'MajorDevAlarmState', 'MajorDevAlarmValue', 'MajorDevAlarmPri', 'DevTarget', 'ROCAlarmState',
         'ROCAlarmValue', 'ROCAlarmPri', 'ROCTimeBase', 'MinRaw', 'MaxRaw', 'Conversion', 'AccessName',
         'ItemUseTagname', 'ItemName', 'ReadOnly', 'AlarmComment', 'AlarmAckModel', 'LoLoAlarmDisable',
         'LoAlarmDisable', 'HiAlarmDisable', 'HiHiAlarmDisable', 'MinDevAlarmDisable', 'MajDevAlarmDisable',
         'RocAlarmDisable', 'LoLoAlarmInhibitor', 'LoAlarmInhibitor', 'HiAlarmInhibitor', 'HiHiAlarmInhibitor',
         'MinDevAlarmInhibitor', 'MajDevAlarmInhibitor', 'RocAlarmInhibitor', 'SymbolicName'
         ],
        [':MemoryMsg', 'Group', 'Comment', 'Logged', 'EventLogged', 'EventLoggingPriority', 'RetentiveValue',
         'MaxLength', 'InitialMessage', 'AlarmComment', 'SymbolicName',
         ],
        [':IOMsg', 'Group', 'Comment', 'Logged', 'EventLogged', 'EventLoggingPriority', 'RetentiveValue',
         'MaxLength', 'InitialMessage', 'AccessName', 'ItemUseTagname', 'ItemName', 'ReadOnly', 'AlarmComment',
         'SymbolicName',
         ],
        [':GroupVar', 'Group', 'Comment', 'SymbolicName',
         ],
        [':HistoryTrend', 'Group', 'Comment', 'SymbolicName',
         ],
        [':TagID', 'Group', 'Comment',
         ],
        [':IndirectDisc', 'Group', 'Comment', 'EventLogged', 'EventLoggingPriority', 'RetentiveValue',
         'SymbolicName',
         ],
        [':IndirectAnalog', 'Group', 'Comment', 'EventLogged', 'EventLoggingPriority', 'RetentiveValue',
         'SymbolicName',
         ],
        [':IndirectMsg', 'Group', 'Comment', 'EventLogged', 'EventLoggingPriority', 'RetentiveValue',
         'SymbolicName',
         ]
        ]

FORM_DICT = {line[0].replace(':', ''): line for line in FORM}

IODisc_TEXT = ['SS_Level1_HiALM', 'SS', '表干刨花料仓 干刨花料仓料位 上限报警', 'No', 'No', '0', 'No', 'Off', '', '', 'None', '1',
               'Direct', 'kep1500', 'No', 'SS_Level1_HiALM', 'Yes', '"表干刨花料仓 干刨花料仓料位 上限报警"', '0', '0',
               ]
IOInt_TEXT = ['SS_Level1_Code', 'SS', '表干刨花料仓 干刨花料仓料位 实际内码', 'No', 'No', '0', 'No', 'No', '0', '0', '', '0', '-32768',
              '32767', '0', '0', 'Off', '0', '1', 'Off', '0', '1', 'Off', '0', '1', 'Off', '0', '1', 'Off', '0', '1',
              'Off', '0', '1', '0', 'Off', '0', '1', 'Min', '-32768', '32767', 'Linear', 'kep1500', 'No',
              'SS_Level1_Code', 'Yes', '', '0', '0', '0', '0', '0', '0', '0', '0',
              ]
IOReal_TEXT = ['SS_Level1_Value', 'SS', '表干刨花料仓 干刨花料仓料位 实际值', 'No', 'No', '0', 'No', 'No', '0', '0', '', '0', '-32768',
               '32767', '0', '0', 'Off', '0', '1', 'Off', '0', '1', 'Off', '0', '1', 'Off', '0', '1', 'Off', '0', '1',
               'Off', '0', '1', '0', 'Off', '0', '1', 'Min', '-32768', '32767', 'Linear', 'kep1500', 'No',
               'SS_Level1_Value', 'No', '', '0', '0', '0', '0', '0', '0', '0', '0',
               ]
# IOAccess_text = 'kep1500,server_runtime,kep1500,Yes,No,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\r\n'


IODisc_INDEX = {
    'name': 0,
    'group': 1,
    'comment': 2,
    'alarm_state': 10,
    'access_name': 13,
    'item_use_tag_name': 14,
    'item_name': 15,
    'read_only': 16,
    'alarm_comment': 17
}

IOInt_INDEX = {
    'name': 0,
    'group': 1,
    'comment': 2,
    'access_name': 42,
    'item_use_tag_name': 43,
    'item_name': 44,
    'read_only': 45,
    'alarm_comment': 46,
}

IOReal_INDEX = IOInt_INDEX

ALARM_NONE = 'None'
ALARM_ON = 'On'
ALARM_OFF = 'Off'
ALARM_MAP = [ALARM_NONE, ALARM_ON, ALARM_OFF]


# print(form_dict)
# print(FORM_DICT.keys())


def _csv_write_tag(hmi_tag: HMITag, text: [], index: {}):
    for fd in index:
        if fd in hmi_tag.__slots__:
            try:
                text[index[fd]] = hmi_tag[fd]
            finally:
                pass
        # else:
        #     print('{}字段不存在'.format(fd))
    if is_bool(hmi_tag.data_type):
        if isinstance(hmi_tag.alarm_state, str):
            text[index['alarm_state']] = hmi_tag.alarm_state
        elif hmi_tag.alarm_state is None:
            text[index['alarm_state']] = ALARM_NONE
        else:
            text[index['alarm_state']] = ALARM_MAP[hmi_tag.alarm_state]
        text[index['alarm_comment']] = '{} {}'.format(hmi_tag.item_name, hmi_tag.comment)


def output_csv(tag_list: TagList, output_path, mode='ask', item_use_tag_name=False, new_group=False,
               access_name='kep1200'):
    mode_text = [':mode=' + mode]
    if item_use_tag_name:
        IODisc_TEXT[IODisc_INDEX['item_use_tag_name']] = 'Yes'
        IOInt_TEXT[IOInt_INDEX['item_use_tag_name']] = 'Yes'
        IOReal_TEXT[IOReal_INDEX['item_use_tag_name']] = 'Yes'
    else:
        IODisc_TEXT[IODisc_INDEX['item_use_tag_name']] = 'No'
        IOInt_TEXT[IOInt_INDEX['item_use_tag_name']] = 'No'
        IOReal_TEXT[IOReal_INDEX['item_use_tag_name']] = 'No'

    with open(output_path, 'w', newline='', encoding='ANSI') as f:
        writer = csv.writer(f)
        # 模式
        writer.writerow(mode_text)
        for key in FORM_DICT.keys():
            writer.writerow(FORM_DICT[key])

            # 自动生成组
            if new_group:
                pass

            # IO离散型变量
            if key == 'IODisc':
                IODisc_TEXT[IODisc_INDEX['access_name']] = access_name
                for hmi_tag in tag_list.disc_list:
                    _csv_write_tag(hmi_tag, IODisc_TEXT, IODisc_INDEX)
                    writer.writerow(IODisc_TEXT)

            # IO整型变量
            if key == 'IOInt':
                IOInt_TEXT[IOInt_INDEX['access_name']] = access_name
                for hmi_tag in tag_list.int_list:
                    _csv_write_tag(hmi_tag, IOInt_TEXT, IOInt_INDEX)
                    writer.writerow(IOInt_TEXT)

            # IO实型变量
            if key == 'IOReal':
                IOReal_TEXT[IOReal_INDEX['access_name']] = access_name
                for hmi_tag in tag_list.real_list:
                    _csv_write_tag(hmi_tag, IOReal_TEXT, IOReal_INDEX)
                    writer.writerow(IOReal_TEXT)

    print(f'数据量{len(tag_list)}， 生成Intouch导入csv文件: {output_path}')
