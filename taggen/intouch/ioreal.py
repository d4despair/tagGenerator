# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/4/13 9:33

from util import StringListObject

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
IOReal_TEXT = ['SS_Level1_Value', 'SS', '表干刨花料仓 干刨花料仓料位 实际值', 'No', 'No', '0', 'No', 'No', '0', '0', '', '0', '-32768',
               '32767', '0', '0', 'Off', '0', '1', 'Off', '0', '1', 'Off', '0', '1', 'Off', '0', '1', 'Off', '0', '1',
               'Off', '0', '1', '0', 'Off', '0', '1', 'Min', '-32768', '32767', 'Linear', 'kep1500', 'No',
               'SS_Level1_Value', 'No', '', '0', '0', '0', '0', '0', '0', '0', '0',
               ]


class IOReal(StringListObject):
    __slots__ = (
        'io_real',
        'group',
        'comment',
        'logged',
        'event_logged',
        'event_logging_priority',
        'retentive_value',
        'retentive_alarm_parameters',
        'alarm_value_deadband',
        'alarm_dev_deadband',
        'eng_units',
        'initial_value',
        'min_eu',
        'max_eu',
        'deadband',
        'log_deadband',
        'lolo_alarm_state',
        'lolo_alarm_value',
        'lolo_alarm_pri',
        'lo_alarm_state',
        'lo_alarm_value',
        'lo_alarm_pri',
        'hi_alarm_state',
        'hi_alarm_value',
        'hi_alarm_pri',
        'hihi_alarm_state',
        'hihi_alarm_value',
        'hihi_alarm_pri',
        'minor_dev_alarm_state',
        'minor_dev_alarm_value',
        'minor_dev_alarm_pri',
        'major_dev_alarm_state',
        'major_dev_alarm_value',
        'major_dev_alarm_pri',
        'dev_target',
        'roc_alarm_state',
        'roc_alarm_value',
        'roc_alarm_pri',
        'roc_time_base',
        'min_raw',
        'max_raw',
        'conversion',
        'access_name',
        'item_use_tagname',
        'item_name',
        'read_only',
        'alarm_comment',
        'alarm_ack_model',
        'lolo_alarm_disable',
        'lo_alarm_disable',
        'hi_alarm_disable',
        'hihi_alarm_disable',
        'min_dev_alarm_disable',
        'maj_dev_alarm_disable',
        'roc_alarm_disable',
        'lolo_alarm_inhibitor',
        'lo_alarm_inhibitor',
        'hi_alarm_inhibitor',
        'hihi_alarm_inhibitor',
        'min_dev_alarm_inhibitor',
        'maj_dev_alarm_inhibitor',
        'roc_alarm_inhibitor',
        'symbolic_name',
    )

    def __init__(self, io_real='', group='', comment='', logged='No', event_logged='No', event_logging_priority='0',
                 retentive_value='No', retentive_alarm_parameters='No', alarm_value_deadband='0',
                 alarm_dev_deadband='0', eng_units='', initial_value='0', min_eu='-32768', max_eu='32767', deadband='0',
                 log_deadband='0', lolo_alarm_state='Off', lolo_alarm_value='0', lolo_alarm_pri='1',
                 lo_alarm_state='Off', lo_alarm_value='0', lo_alarm_pri='1', hi_alarm_state='Off', hi_alarm_value='0',
                 hi_alarm_pri='1', hihi_alarm_state='Off', hihi_alarm_value='0', hihi_alarm_pri='1',
                 minor_dev_alarm_state='Off', minor_dev_alarm_value='0', minor_dev_alarm_pri='1',
                 major_dev_alarm_state='Off', major_dev_alarm_value='0', major_dev_alarm_pri='1', dev_target='0',
                 roc_alarm_state='Off', roc_alarm_value='0', roc_alarm_pri='1', roc_time_base='Min', min_raw='-32768',
                 max_raw='32767', conversion='Linear', access_name='kep1500', item_use_tagname='No',
                 item_name='SS_Level1_Value', read_only='No', alarm_comment='', alarm_ack_model='0',
                 lolo_alarm_disable='0', lo_alarm_disable='0', hi_alarm_disable='0', hihi_alarm_disable='0',
                 min_dev_alarm_disable='0', maj_dev_alarm_disable='0', roc_alarm_disable='0', lolo_alarm_inhibitor='',
                 lo_alarm_inhibitor='', hi_alarm_inhibitor='', hihi_alarm_inhibitor='', min_dev_alarm_inhibitor='',
                 maj_dev_alarm_inhibitor='', roc_alarm_inhibitor='', symbolic_name=''):
        self.io_real = io_real
        self.group = group
        self.comment = comment
        self.logged = logged
        self.event_logged = event_logged
        self.event_logging_priority = event_logging_priority
        self.retentive_value = retentive_value
        self.retentive_alarm_parameters = retentive_alarm_parameters
        self.alarm_value_deadband = alarm_value_deadband
        self.alarm_dev_deadband = alarm_dev_deadband
        self.eng_units = eng_units
        self.initial_value = initial_value
        self.min_eu = min_eu
        self.max_eu = max_eu
        self.deadband = deadband
        self.log_deadband = log_deadband
        self.lolo_alarm_state = lolo_alarm_state
        self.lolo_alarm_value = lolo_alarm_value
        self.lolo_alarm_pri = lolo_alarm_pri
        self.lo_alarm_state = lo_alarm_state
        self.lo_alarm_value = lo_alarm_value
        self.lo_alarm_pri = lo_alarm_pri
        self.hi_alarm_state = hi_alarm_state
        self.hi_alarm_value = hi_alarm_value
        self.hi_alarm_pri = hi_alarm_pri
        self.hihi_alarm_state = hihi_alarm_state
        self.hihi_alarm_value = hihi_alarm_value
        self.hihi_alarm_pri = hihi_alarm_pri
        self.minor_dev_alarm_state = minor_dev_alarm_state
        self.minor_dev_alarm_value = minor_dev_alarm_value
        self.minor_dev_alarm_pri = minor_dev_alarm_pri
        self.major_dev_alarm_state = major_dev_alarm_state
        self.major_dev_alarm_value = major_dev_alarm_value
        self.major_dev_alarm_pri = major_dev_alarm_pri
        self.dev_target = dev_target
        self.roc_alarm_state = roc_alarm_state
        self.roc_alarm_value = roc_alarm_value
        self.roc_alarm_pri = roc_alarm_pri
        self.roc_time_base = roc_time_base
        self.min_raw = min_raw
        self.max_raw = max_raw
        self.conversion = conversion
        self.access_name = access_name
        self.item_use_tagname = item_use_tagname
        self.item_name = item_name
        self.read_only = read_only
        self.alarm_comment = alarm_comment
        self.alarm_ack_model = alarm_ack_model
        self.lolo_alarm_disable = lolo_alarm_disable
        self.lo_alarm_disable = lo_alarm_disable
        self.hi_alarm_disable = hi_alarm_disable
        self.hihi_alarm_disable = hihi_alarm_disable
        self.min_dev_alarm_disable = min_dev_alarm_disable
        self.maj_dev_alarm_disable = maj_dev_alarm_disable
        self.roc_alarm_disable = roc_alarm_disable
        self.lolo_alarm_inhibitor = lolo_alarm_inhibitor
        self.lo_alarm_inhibitor = lo_alarm_inhibitor
        self.hi_alarm_inhibitor = hi_alarm_inhibitor
        self.hihi_alarm_inhibitor = hihi_alarm_inhibitor
        self.min_dev_alarm_inhibitor = min_dev_alarm_inhibitor
        self.maj_dev_alarm_inhibitor = maj_dev_alarm_inhibitor
        self.roc_alarm_inhibitor = roc_alarm_inhibitor
        self.symbolic_name = symbolic_name

    @property
    def tagname(self):
        return self.io_real

    @tagname.setter
    def tagname(self, value):
        self.io_real = value


# ========================== IOReal 结束 ==========================


def test():
    print('test')
    from util import print_class_string
    from header import IO_REAL_HEADER, IO_REAL_HEADER_PYTHON
    header = IO_REAL_HEADER
    header_python = IO_REAL_HEADER_PYTHON
    print_class_string(header[0].replace(':', ''), header_python)
    ch01_flow_value = IOReal(io_real='CH01_Flow_Value', group='ch01', comment='表胶流量', item_name='DB11,REAL6')
    print(ch01_flow_value.csv_format)


if __name__ == '__main__':
    test()
