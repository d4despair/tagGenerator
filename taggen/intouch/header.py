# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/4/13 9:40


IO_ACCESS_HEADER = [':IOAccess', 'Application', 'Topic', 'AdviseActive', 'DDEProtocol', 'SecApplication', 'SecTopic',
                    'SecAdviseActive', 'SecDDEProtocol', 'FailoverExpression', 'FailoverDeadband', 'DFOFlag', 'FBDFlag',
                    'FailbackDeadband']
IO_ACCESS_HEADER_PYTHON = [':io_access', 'application', 'topic', 'advise_active', 'dde_protocol', 'sec_application',
                           'sec_topic', 'sec_advise_active', 'sec_dde_protocol', 'failover_expression',
                           'failover_deadband', 'dfo_flag', 'fbd_flag', 'failback_deadband']
IO_ACCESS_DICT = {python: camel for python, camel in zip(IO_ACCESS_HEADER_PYTHON, IO_ACCESS_HEADER)}

ALARM_GROUP_HEADER = [':AlarmGroup', 'Group', 'Comment', 'EventLogged', 'EventLoggingPriority', 'LoLoAlarmDisable',
                      'LoAlarmDisable', 'HiAlarmDisable', 'HiHiAlarmDisable', 'MinDevAlarmDisable',
                      'MajDevAlarmDisable', 'RocAlarmDisable', 'DSCAlarmDisable', 'LoLoAlarmInhibitor',
                      'LoAlarmInhibitor', 'HiAlarmInhibitor', 'HiHiAlarmInhibitor', 'MinDevAlarmInhibitor',
                      'MajDevAlarmInhibitor', 'RocAlarmInhibitor', 'DSCAlarmInhibitor']
ALARM_GROUP_HEADER_PYTHON = [':alarm_group', 'group', 'comment', 'event_logged', 'event_logging_priority',
                             'lolo_alarm_disable', 'lo_alarm_disable', 'hi_alarm_disable', 'hihi_alarm_disable',
                             'min_dev_alarm_disable', 'maj_dev_alarm_disable', 'roc_alarm_disable', 'dsc_alarm_disable',
                             'lolo_alarm_inhibitor', 'lo_alarm_inhibitor', 'hi_alarm_inhibitor', 'hihi_alarm_inhibitor',
                             'min_dev_alarm_inhibitor', 'maj_dev_alarm_inhibitor', 'roc_alarm_inhibitor',
                             'dsc_alarm_inhibitor']
ALARM_GROUP_DICT = {python: camel for python, camel in zip(ALARM_GROUP_HEADER_PYTHON, ALARM_GROUP_HEADER)}

IO_DISC_HEADER = [':IODisc', 'Group', 'Comment', 'Logged', 'EventLogged', 'EventLoggingPriority', 'RetentiveValue',
                  'InitialDisc', 'OffMsg', 'OnMsg', 'AlarmState', 'AlarmPri', 'DConversion', 'AccessName',
                  'ItemUseTagname', 'ItemName', 'ReadOnly', 'AlarmComment', 'AlarmAckModel', 'DSCAlarmDisable',
                  'DSCAlarmInhibitor', 'SymbolicName']
IO_DISC_HEADER_PYTHON = [':io_disc', 'group', 'comment', 'logged', 'event_logged', 'event_logging_priority',
                         'retentive_value', 'initial_disc', 'off_msg', 'on_msg', 'alarm_state', 'alarm_pri',
                         'd_conversion', 'access_name', 'item_use_tagname', 'item_name', 'read_only', 'alarm_comment',
                         'alarm_ack_model', 'dsc_alarm_disable', 'dsc_alarm_inhibitor', 'symbolic_name']
IO_DISC_DICT = {python: camel for python, camel in zip(IO_DISC_HEADER_PYTHON, IO_DISC_HEADER)}

MEMORY_INT_HEADER = [':MemoryInt', 'Group', 'Comment', 'Logged', 'EventLogged', 'EventLoggingPriority',
                     'RetentiveValue', 'RetentiveAlarmParameters', 'AlarmValueDeadband', 'AlarmDevDeadband', 'EngUnits',
                     'InitialValue', 'MinValue', 'MaxValue', 'Deadband', 'LogDeadband', 'LoLoAlarmState',
                     'LoLoAlarmValue', 'LoLoAlarmPri', 'LoAlarmState', 'LoAlarmValue', 'LoAlarmPri', 'HiAlarmState',
                     'HiAlarmValue', 'HiAlarmPri', 'HiHiAlarmState', 'HiHiAlarmValue', 'HiHiAlarmPri',
                     'MinorDevAlarmState', 'MinorDevAlarmValue', 'MinorDevAlarmPri', 'MajorDevAlarmState',
                     'MajorDevAlarmValue', 'MajorDevAlarmPri', 'DevTarget', 'ROCAlarmState', 'ROCAlarmValue',
                     'ROCAlarmPri', 'ROCTimeBase', 'AlarmComment', 'AlarmAckModel', 'LoLoAlarmDisable',
                     'LoAlarmDisable', 'HiAlarmDisable', 'HiHiAlarmDisable', 'MinDevAlarmDisable', 'MajDevAlarmDisable',
                     'RocAlarmDisable', 'LoLoAlarmInhibitor', 'LoAlarmInhibitor', 'HiAlarmInhibitor',
                     'HiHiAlarmInhibitor', 'MinDevAlarmInhibitor', 'MajDevAlarmInhibitor', 'RocAlarmInhibitor',
                     'SymbolicName']
MEMORY_INT_HEADER_PYTHON = [':memory_int', 'group', 'comment', 'logged', 'event_logged', 'event_logging_priority',
                            'retentive_value', 'retentive_alarm_parameters', 'alarm_value_deadband',
                            'alarm_dev_deadband', 'eng_units', 'initial_value', 'min_value', 'max_value', 'deadband',
                            'log_deadband', 'lolo_alarm_state', 'lolo_alarm_value', 'lolo_alarm_pri', 'lo_alarm_state',
                            'lo_alarm_value', 'lo_alarm_pri', 'hi_alarm_state', 'hi_alarm_value', 'hi_alarm_pri',
                            'hihi_alarm_state', 'hihi_alarm_value', 'hihi_alarm_pri', 'minor_dev_alarm_state',
                            'minor_dev_alarm_value', 'minor_dev_alarm_pri', 'major_dev_alarm_state',
                            'major_dev_alarm_value', 'major_dev_alarm_pri', 'dev_target', 'roc_alarm_state',
                            'roc_alarm_value', 'roc_alarm_pri', 'roc_time_base', 'alarm_comment', 'alarm_ack_model',
                            'lolo_alarm_disable', 'lo_alarm_disable', 'hi_alarm_disable', 'hihi_alarm_disable',
                            'min_dev_alarm_disable', 'maj_dev_alarm_disable', 'roc_alarm_disable',
                            'lolo_alarm_inhibitor', 'lo_alarm_inhibitor', 'hi_alarm_inhibitor', 'hihi_alarm_inhibitor',
                            'min_dev_alarm_inhibitor', 'maj_dev_alarm_inhibitor', 'roc_alarm_inhibitor',
                            'symbolic_name']
MEMORY_INT_DICT = {python: camel for python, camel in zip(MEMORY_INT_HEADER_PYTHON, MEMORY_INT_HEADER)}

IO_INT_HEADER = [':IOInt', 'Group', 'Comment', 'Logged', 'EventLogged', 'EventLoggingPriority', 'RetentiveValue',
                 'RetentiveAlarmParameters', 'AlarmValueDeadband', 'AlarmDevDeadband', 'EngUnits', 'InitialValue',
                 'MinEU', 'MaxEU', 'Deadband', 'LogDeadband', 'LoLoAlarmState', 'LoLoAlarmValue', 'LoLoAlarmPri',
                 'LoAlarmState', 'LoAlarmValue', 'LoAlarmPri', 'HiAlarmState', 'HiAlarmValue', 'HiAlarmPri',
                 'HiHiAlarmState', 'HiHiAlarmValue', 'HiHiAlarmPri', 'MinorDevAlarmState', 'MinorDevAlarmValue',
                 'MinorDevAlarmPri', 'MajorDevAlarmState', 'MajorDevAlarmValue', 'MajorDevAlarmPri', 'DevTarget',
                 'ROCAlarmState', 'ROCAlarmValue', 'ROCAlarmPri', 'ROCTimeBase', 'MinRaw', 'MaxRaw', 'Conversion',
                 'AccessName', 'ItemUseTagname', 'ItemName', 'ReadOnly', 'AlarmComment', 'AlarmAckModel',
                 'LoLoAlarmDisable', 'LoAlarmDisable', 'HiAlarmDisable', 'HiHiAlarmDisable', 'MinDevAlarmDisable',
                 'MajDevAlarmDisable', 'RocAlarmDisable', 'LoLoAlarmInhibitor', 'LoAlarmInhibitor', 'HiAlarmInhibitor',
                 'HiHiAlarmInhibitor', 'MinDevAlarmInhibitor', 'MajDevAlarmInhibitor', 'RocAlarmInhibitor',
                 'SymbolicName']
IO_INT_HEADER_PYTHON = [':io_int', 'group', 'comment', 'logged', 'event_logged', 'event_logging_priority',
                        'retentive_value', 'retentive_alarm_parameters', 'alarm_value_deadband', 'alarm_dev_deadband',
                        'eng_units', 'initial_value', 'min_eu', 'max_eu', 'deadband', 'log_deadband',
                        'lolo_alarm_state', 'lolo_alarm_value', 'lolo_alarm_pri', 'lo_alarm_state', 'lo_alarm_value',
                        'lo_alarm_pri', 'hi_alarm_state', 'hi_alarm_value', 'hi_alarm_pri', 'hihi_alarm_state',
                        'hihi_alarm_value', 'hihi_alarm_pri', 'minor_dev_alarm_state', 'minor_dev_alarm_value',
                        'minor_dev_alarm_pri', 'major_dev_alarm_state', 'major_dev_alarm_value', 'major_dev_alarm_pri',
                        'dev_target', 'roc_alarm_state', 'roc_alarm_value', 'roc_alarm_pri', 'roc_time_base', 'min_raw',
                        'max_raw', 'conversion', 'access_name', 'item_use_tagname', 'item_name', 'read_only',
                        'alarm_comment', 'alarm_ack_model', 'lolo_alarm_disable', 'lo_alarm_disable',
                        'hi_alarm_disable', 'hihi_alarm_disable', 'min_dev_alarm_disable', 'maj_dev_alarm_disable',
                        'roc_alarm_disable', 'lolo_alarm_inhibitor', 'lo_alarm_inhibitor', 'hi_alarm_inhibitor',
                        'hihi_alarm_inhibitor', 'min_dev_alarm_inhibitor', 'maj_dev_alarm_inhibitor',
                        'roc_alarm_inhibitor', 'symbolic_name']
IO_INT_DICT = {python: camel for python, camel in zip(IO_INT_HEADER_PYTHON, IO_INT_HEADER)}

MEMORY_REAL_HEADER = [':MemoryReal', 'Group', 'Comment', 'Logged', 'EventLogged', 'EventLoggingPriority',
                      'RetentiveValue', 'RetentiveAlarmParameters', 'AlarmValueDeadband', 'AlarmDevDeadband',
                      'EngUnits', 'InitialValue', 'MinValue', 'MaxValue', 'Deadband', 'LogDeadband', 'LoLoAlarmState',
                      'LoLoAlarmValue', 'LoLoAlarmPri', 'LoAlarmState', 'LoAlarmValue', 'LoAlarmPri', 'HiAlarmState',
                      'HiAlarmValue', 'HiAlarmPri', 'HiHiAlarmState', 'HiHiAlarmValue', 'HiHiAlarmPri',
                      'MinorDevAlarmState', 'MinorDevAlarmValue', 'MinorDevAlarmPri', 'MajorDevAlarmState',
                      'MajorDevAlarmValue', 'MajorDevAlarmPri', 'DevTarget', 'ROCAlarmState', 'ROCAlarmValue',
                      'ROCAlarmPri', 'ROCTimeBase', 'AlarmComment', 'AlarmAckModel', 'LoLoAlarmDisable',
                      'LoAlarmDisable', 'HiAlarmDisable', 'HiHiAlarmDisable', 'MinDevAlarmDisable',
                      'MajDevAlarmDisable', 'RocAlarmDisable', 'LoLoAlarmInhibitor', 'LoAlarmInhibitor',
                      'HiAlarmInhibitor', 'HiHiAlarmInhibitor', 'MinDevAlarmInhibitor', 'MajDevAlarmInhibitor',
                      'RocAlarmInhibitor', 'SymbolicName']
MEMORY_REAL_HEADER_PYTHON = [':memory_real', 'group', 'comment', 'logged', 'event_logged', 'event_logging_priority',
                             'retentive_value', 'retentive_alarm_parameters', 'alarm_value_deadband',
                             'alarm_dev_deadband', 'eng_units', 'initial_value', 'min_value', 'max_value', 'deadband',
                             'log_deadband', 'lolo_alarm_state', 'lolo_alarm_value', 'lolo_alarm_pri', 'lo_alarm_state',
                             'lo_alarm_value', 'lo_alarm_pri', 'hi_alarm_state', 'hi_alarm_value', 'hi_alarm_pri',
                             'hihi_alarm_state', 'hihi_alarm_value', 'hihi_alarm_pri', 'minor_dev_alarm_state',
                             'minor_dev_alarm_value', 'minor_dev_alarm_pri', 'major_dev_alarm_state',
                             'major_dev_alarm_value', 'major_dev_alarm_pri', 'dev_target', 'roc_alarm_state',
                             'roc_alarm_value', 'roc_alarm_pri', 'roc_time_base', 'alarm_comment', 'alarm_ack_model',
                             'lolo_alarm_disable', 'lo_alarm_disable', 'hi_alarm_disable', 'hihi_alarm_disable',
                             'min_dev_alarm_disable', 'maj_dev_alarm_disable', 'roc_alarm_disable',
                             'lolo_alarm_inhibitor', 'lo_alarm_inhibitor', 'hi_alarm_inhibitor', 'hihi_alarm_inhibitor',
                             'min_dev_alarm_inhibitor', 'maj_dev_alarm_inhibitor', 'roc_alarm_inhibitor',
                             'symbolic_name']
MEMORY_REAL_DICT = {python: camel for python, camel in zip(MEMORY_REAL_HEADER_PYTHON, MEMORY_REAL_HEADER)}

IO_REAL_HEADER = [':IOReal', 'Group', 'Comment', 'Logged', 'EventLogged', 'EventLoggingPriority', 'RetentiveValue',
                  'RetentiveAlarmParameters', 'AlarmValueDeadband', 'AlarmDevDeadband', 'EngUnits', 'InitialValue',
                  'MinEU', 'MaxEU', 'Deadband', 'LogDeadband', 'LoLoAlarmState', 'LoLoAlarmValue', 'LoLoAlarmPri',
                  'LoAlarmState', 'LoAlarmValue', 'LoAlarmPri', 'HiAlarmState', 'HiAlarmValue', 'HiAlarmPri',
                  'HiHiAlarmState', 'HiHiAlarmValue', 'HiHiAlarmPri', 'MinorDevAlarmState', 'MinorDevAlarmValue',
                  'MinorDevAlarmPri', 'MajorDevAlarmState', 'MajorDevAlarmValue', 'MajorDevAlarmPri', 'DevTarget',
                  'ROCAlarmState', 'ROCAlarmValue', 'ROCAlarmPri', 'ROCTimeBase', 'MinRaw', 'MaxRaw', 'Conversion',
                  'AccessName', 'ItemUseTagname', 'ItemName', 'ReadOnly', 'AlarmComment', 'AlarmAckModel',
                  'LoLoAlarmDisable', 'LoAlarmDisable', 'HiAlarmDisable', 'HiHiAlarmDisable', 'MinDevAlarmDisable',
                  'MajDevAlarmDisable', 'RocAlarmDisable', 'LoLoAlarmInhibitor', 'LoAlarmInhibitor', 'HiAlarmInhibitor',
                  'HiHiAlarmInhibitor', 'MinDevAlarmInhibitor', 'MajDevAlarmInhibitor', 'RocAlarmInhibitor',
                  'SymbolicName']
IO_REAL_HEADER_PYTHON = [':io_real', 'group', 'comment', 'logged', 'event_logged', 'event_logging_priority',
                         'retentive_value', 'retentive_alarm_parameters', 'alarm_value_deadband', 'alarm_dev_deadband',
                         'eng_units', 'initial_value', 'min_eu', 'max_eu', 'deadband', 'log_deadband',
                         'lolo_alarm_state', 'lolo_alarm_value', 'lolo_alarm_pri', 'lo_alarm_state', 'lo_alarm_value',
                         'lo_alarm_pri', 'hi_alarm_state', 'hi_alarm_value', 'hi_alarm_pri', 'hihi_alarm_state',
                         'hihi_alarm_value', 'hihi_alarm_pri', 'minor_dev_alarm_state', 'minor_dev_alarm_value',
                         'minor_dev_alarm_pri', 'major_dev_alarm_state', 'major_dev_alarm_value', 'major_dev_alarm_pri',
                         'dev_target', 'roc_alarm_state', 'roc_alarm_value', 'roc_alarm_pri', 'roc_time_base',
                         'min_raw', 'max_raw', 'conversion', 'access_name', 'item_use_tagname', 'item_name',
                         'read_only', 'alarm_comment', 'alarm_ack_model', 'lolo_alarm_disable', 'lo_alarm_disable',
                         'hi_alarm_disable', 'hihi_alarm_disable', 'min_dev_alarm_disable', 'maj_dev_alarm_disable',
                         'roc_alarm_disable', 'lolo_alarm_inhibitor', 'lo_alarm_inhibitor', 'hi_alarm_inhibitor',
                         'hihi_alarm_inhibitor', 'min_dev_alarm_inhibitor', 'maj_dev_alarm_inhibitor',
                         'roc_alarm_inhibitor', 'symbolic_name']
IO_REAL_DICT = {python: camel for python, camel in zip(IO_REAL_HEADER_PYTHON, IO_REAL_HEADER)}

MEMORY_MSG_HEADER = [':MemoryMsg', 'Group', 'Comment', 'Logged', 'EventLogged', 'EventLoggingPriority',
                     'RetentiveValue', 'MaxLength', 'InitialMessage', 'AlarmComment', 'SymbolicName']
MEMORY_MSG_HEADER_PYTHON = [':memory_msg', 'group', 'comment', 'logged', 'event_logged', 'event_logging_priority',
                            'retentive_value', 'max_length', 'initial_message', 'alarm_comment', 'symbolic_name']
MEMORY_MSG_DICT = {python: camel for python, camel in zip(MEMORY_MSG_HEADER_PYTHON, MEMORY_MSG_HEADER)}

IO_MSG_HEADER = [':IOMsg', 'Group', 'Comment', 'Logged', 'EventLogged', 'EventLoggingPriority', 'RetentiveValue',
                 'MaxLength', 'InitialMessage', 'AccessName', 'ItemUseTagname', 'ItemName', 'ReadOnly', 'AlarmComment',
                 'SymbolicName']
IO_MSG_HEADER_PYTHON = [':io_msg', 'group', 'comment', 'logged', 'event_logged', 'event_logging_priority',
                        'retentive_value', 'max_length', 'initial_message', 'access_name', 'item_use_tagname',
                        'item_name', 'read_only', 'alarm_comment', 'symbolic_name']
IO_MSG_DICT = {python: camel for python, camel in zip(IO_MSG_HEADER_PYTHON, IO_MSG_HEADER)}

GROUP_VAR_HEADER = [':GroupVar', 'Group', 'Comment', 'SymbolicName']
GROUP_VAR_HEADER_PYTHON = [':group_var', 'group', 'comment', 'symbolic_name']
GROUP_VAR_DICT = {python: camel for python, camel in zip(GROUP_VAR_HEADER_PYTHON, GROUP_VAR_HEADER)}

HISTORY_TREND_HEADER = [':HistoryTrend', 'Group', 'Comment', 'SymbolicName']
HISTORY_TREND_HEADER_PYTHON = [':history_trend', 'group', 'comment', 'symbolic_name']
HISTORY_TREND_DICT = {python: camel for python, camel in zip(HISTORY_TREND_HEADER_PYTHON, HISTORY_TREND_HEADER)}

TAG_ID_HEADER = [':TagID', 'Group', 'Comment']
TAG_ID_HEADER_PYTHON = [':tag_id', 'group', 'comment']
TAG_ID_DICT = {python: camel for python, camel in zip(TAG_ID_HEADER_PYTHON, TAG_ID_HEADER)}

INDIRECT_DISC_HEADER = [':IndirectDisc', 'Group', 'Comment', 'EventLogged', 'EventLoggingPriority', 'RetentiveValue',
                        'SymbolicName']
INDIRECT_DISC_HEADER_PYTHON = [':indirect_disc', 'group', 'comment', 'event_logged', 'event_logging_priority',
                               'retentive_value', 'symbolic_name']
INDIRECT_DISC_DICT = {python: camel for python, camel in zip(INDIRECT_DISC_HEADER_PYTHON, INDIRECT_DISC_HEADER)}

INDIRECT_ANALOG_HEADER = [':IndirectAnalog', 'Group', 'Comment', 'EventLogged', 'EventLoggingPriority',
                          'RetentiveValue', 'SymbolicName']
INDIRECT_ANALOG_HEADER_PYTHON = [':indirect_analog', 'group', 'comment', 'event_logged', 'event_logging_priority',
                                 'retentive_value', 'symbolic_name']
INDIRECT_ANALOG_DICT = {python: camel for python, camel in zip(INDIRECT_ANALOG_HEADER_PYTHON, INDIRECT_ANALOG_HEADER)}

INDIRECT_MSG_HEADER = [':IndirectMsg', 'Group', 'Comment', 'EventLogged', 'EventLoggingPriority', 'RetentiveValue',
                       'SymbolicName']
INDIRECT_MSG_HEADER_PYTHON = [':indirect_msg', 'group', 'comment', 'event_logged', 'event_logging_priority',
                              'retentive_value', 'symbolic_name']
INDIRECT_MSG_DICT = {python: camel for python, camel in zip(INDIRECT_MSG_HEADER_PYTHON, INDIRECT_MSG_HEADER)}

HEADER_LIST = [IO_ACCESS_HEADER, ALARM_GROUP_HEADER, IO_DISC_HEADER, MEMORY_INT_HEADER, IO_INT_HEADER,
               MEMORY_REAL_HEADER, IO_REAL_HEADER, MEMORY_MSG_HEADER, IO_MSG_HEADER, GROUP_VAR_HEADER,
               HISTORY_TREND_HEADER, TAG_ID_HEADER, INDIRECT_DISC_HEADER, INDIRECT_ANALOG_HEADER, INDIRECT_MSG_HEADER, ]


def test():
    [print(header) for header in HEADER_LIST]


if __name__ == '__main__':
    test()
