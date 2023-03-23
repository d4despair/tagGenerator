# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/18 16:19

TYPE_BOOL = 'Bool'
TYPE_INT = 'Int'
TYPE_REAL = 'Real'
TYPE_STRING = 'String'


class Tag:
    name = None
    type = None
    comment = None

    def __init__(self, name=None, ttype=None, comment=None):
        self.name = name
        self.type = ttype
        self.comment = comment

    def __getitem__(self, item):
        # if hasattr(self, item):
        return self.__getattribute__(item)

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def __str__(self):
        print('测试__str__')
        return '{0},{1},{2}'.format(str(self.name), str(self.type), str(self.comment))


class Bool:
    pass
    __slots__ = ['IOInt', 'Group', 'Comment', 'Logged', 'EventLogged', 'EventLoggingPriority', 'RetentiveValue',
                 'RetentiveAlarmParameters', 'AlarmValueDeadband', 'AlarmDevDeadband', 'EngUnits', 'InitialValue',
                 'MinEU',
                 'MaxEU', 'Deadband', 'LogDeadband', 'LoLoAlarmState', 'LoLoAlarmValue', 'LoLoAlarmPri', 'LoAlarmState',
                 'LoAlarmValue', 'LoAlarmPri', 'HiAlarmState', 'HiAlarmValue', 'HiAlarmPri', 'HiHiAlarmState',
                 'HiHiAlarmValue', 'HiHiAlarmPri', 'MinorDevAlarmState', 'MinorDevAlarmValue', 'MinorDevAlarmPri',
                 'MajorDevAlarmState', 'MajorDevAlarmValue', 'MajorDevAlarmPri', 'DevTarget', 'ROCAlarmState',
                 'ROCAlarmValue', 'ROCAlarmPri', 'ROCTimeBase', 'MinRaw', 'MaxRaw', 'Conversion', 'AccessName',
                 'ItemUseTagname', 'ItemName', 'ReadOnly', 'AlarmComment', 'AlarmAckModel', 'LoLoAlarmDisable',
                 'LoAlarmDisable', 'HiAlarmDisable', 'HiHiAlarmDisable', 'MinDevAlarmDisable', 'MajDevAlarmDisable',
                 'RocAlarmDisable', 'LoLoAlarmInhibitor', 'LoAlarmInhibitor', 'HiAlarmInhibitor', 'HiHiAlarmInhibitor',
                 'MinDevAlarmInhibitor', 'MajDevAlarmInhibitor', 'RocAlarmInhibitor', 'SymbolicName'
                 ]

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def __getitem__(self, key):
        return self.__getattribute__(key)
