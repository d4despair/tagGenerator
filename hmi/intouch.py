# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/17 15:44
import csv
import udt
from udt import TagList, HMITag

# mode_text = ':mode=REPLACE,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\r\n'
form = [[':IOAccess', 'Application', 'Topic', 'AdviseActive', 'DDEProtocol', 'SecApplication', 'SecTopic',
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

form_dict = {line[0].replace(':', ''): line for line in form}

IODisc_text = ['SS_Level1_HiALM', 'SS', '表干刨花料仓 干刨花料仓料位 上限报警', 'No', 'No', '0', 'No', 'Off', '', '', 'None', '1',
               'Direct', 'kep1500', 'No', 'SS_Level1_HiALM', 'Yes', '"表干刨花料仓 干刨花料仓料位 上限报警"', '0', '0',
               ]
IOInt_text = ['SS_Level1_Code', 'SS', '表干刨花料仓 干刨花料仓料位 实际内码', 'No', 'No', '0', 'No', 'No', '0', '0', '', '0', '-32768',
              '32767', '0', '0', 'Off', '0', '1', 'Off', '0', '1', 'Off', '0', '1', 'Off', '0', '1', 'Off', '0', '1',
              'Off', '0', '1', '0', 'Off', '0', '1', 'Min', '-32768', '32767', 'Linear', 'kep1500', 'No',
              'SS_Level1_Code', 'Yes', '', '0', '0', '0', '0', '0', '0', '0', '0',
              ]
IOReal_text = ['SS_Level1_Value', 'SS', '表干刨花料仓 干刨花料仓料位 实际值', 'No', 'No', '0', 'No', 'No', '0', '0', '', '0', '-32768',
               '32767', '0', '0', 'Off', '0', '1', 'Off', '0', '1', 'Off', '0', '1', 'Off', '0', '1', 'Off', '0', '1',
               'Off', '0', '1', '0', 'Off', '0', '1', 'Min', '-32768', '32767', 'Linear', 'kep1500', 'No',
               'SS_Level1_Value', 'No', '', '0', '0', '0', '0', '0', '0', '0', '0',
               ]
# IOAccess_text = 'kep1500,server_runtime,kep1500,Yes,No,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\r\n'


IODisc_index = {
    'name': 0,
    'group': 1,
    'comment': 2,
    'alarm_state': 10,
    'access_name': 13,
    'item_use_tag_name': 14,
    'item_name': 15,
    'real_only': 16,
    'alarm_comment': 17
}

IOInt_index = {
    'name': 0,
    'group': 1,
    'comment': 2,
    'access_name': 42,
    'item_use_tag_name': 43,
    'item_name': 44,
    'real_only': 45,
    'alarm_comment': 46,
}

IOReal_index = IOInt_index

alarm_map = ['None', 'On', 'Off']
# print(form_dict)
print(form_dict.keys())


def csv_write_tag(hmi_tag: HMITag, text: [], index: {}):
    for fd in index:
        if fd in hmi_tag.__dict__:
            try:
                text[index[fd]] = hmi_tag[fd]
            finally:
                pass
    if udt.is_bool(hmi_tag.type):
        text[index['alarm_state']] = alarm_map[hmi_tag.alarm_state]
        text[index['alarm_comment']] = '{} {}'.format(hmi_tag.item_name, hmi_tag.comment)


def output_csv(tag_list: TagList, output_path, mode='ask', item_use_tag_name=False, new_group=False, access_name='kep1200'):

    mode_text = [':mode=' + mode]
    if item_use_tag_name:
        IODisc_text[IODisc_index['item_use_tag_name']] = 'Yes'
        IOInt_text[IOInt_index['item_use_tag_name']] = 'Yes'
        IOInt_text[IOInt_index['item_use_tag_name']] = 'Yes'
    else:
        IODisc_text[IODisc_index['item_use_tag_name']] = 'No'
        IOInt_text[IOInt_index['item_use_tag_name']] = 'No'
        IOInt_text[IOInt_index['item_use_tag_name']] = 'No'

    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(mode_text)
        for key in form_dict.keys():
            writer.writerow(form_dict[key])

            # 自动生成组
            if new_group:
                pass

            # IO离散型变量
            if key == 'IODisc':
                IODisc_text[IODisc_index['access_name']] = access_name
                for hmi_tag in tag_list.disc_list:
                    csv_write_tag(hmi_tag, IODisc_text, IODisc_index)
                    writer.writerow(IODisc_text)

            # IO整型变量
            if key == 'IOInt':
                IOInt_text[IOInt_index['access_name']] = access_name
                for hmi_tag in tag_list.int_list:
                    csv_write_tag(hmi_tag, IOInt_text, IOInt_index)
                    writer.writerow(IOInt_text)

            # IO实型变量
            if key == 'IOReal':
                IOReal_text[IOReal_index['access_name']] = access_name
                for hmi_tag in tag_list.real_list:
                    csv_write_tag(hmi_tag, IOReal_text, IOReal_index)
                    writer.writerow(IOReal_text)

