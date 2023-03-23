# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/17 16:17
import os.path

path = os.path.dirname(__file__) + '/db_temp.CSV'
print('打开: ' + path)


def string_to_list(s: str):
    if ',' in s:
        return '[\'{}]'.format(s.replace(',', '\',\''))


with open(path, 'r', newline='') as f:
    l = [line for line in f.readlines() if ':' not in line]
    print(string_to_list(l[0]))
    print(string_to_list(l[1]))
    print(string_to_list(l[2]))
    f.close()

template = [
    ':IOAccess,Application,Topic,AdviseActive,DDEProtocol,SecApplication,SecTopic,SecAdviseActive,SecDDEProtocol,FailoverExpression,FailoverDeadband,DFOFlag,FBDFlag,FailbackDeadband,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\r\n',
    ':AlarmGroup,Group,Comment,EventLogged,EventLoggingPriority,LoLoAlarmDisable,LoAlarmDisable,HiAlarmDisable,HiHiAlarmDisable,MinDevAlarmDisable,MajDevAlarmDisable,RocAlarmDisable,DSCAlarmDisable,LoLoAlarmInhibitor,LoAlarmInhibitor,HiAlarmInhibitor,HiHiAlarmInhibitor,MinDevAlarmInhibitor,MajDevAlarmInhibitor,RocAlarmInhibitor,DSCAlarmInhibitor,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\r\n',
    ':IODisc,Group,Comment,Logged,EventLogged,EventLoggingPriority,RetentiveValue,InitialDisc,OffMsg,OnMsg,AlarmState,AlarmPri,DConversion,AccessName,ItemUseTagname,ItemName,ReadOnly,AlarmComment,AlarmAckModel,DSCAlarmDisable,DSCAlarmInhibitor,SymbolicName,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\r\n',
    ':MemoryInt,Group,Comment,Logged,EventLogged,EventLoggingPriority,RetentiveValue,RetentiveAlarmParameters,AlarmValueDeadband,AlarmDevDeadband,EngUnits,InitialValue,MinValue,MaxValue,Deadband,LogDeadband,LoLoAlarmState,LoLoAlarmValue,LoLoAlarmPri,LoAlarmState,LoAlarmValue,LoAlarmPri,HiAlarmState,HiAlarmValue,HiAlarmPri,HiHiAlarmState,HiHiAlarmValue,HiHiAlarmPri,MinorDevAlarmState,MinorDevAlarmValue,MinorDevAlarmPri,MajorDevAlarmState,MajorDevAlarmValue,MajorDevAlarmPri,DevTarget,ROCAlarmState,ROCAlarmValue,ROCAlarmPri,ROCTimeBase,AlarmComment,AlarmAckModel,LoLoAlarmDisable,LoAlarmDisable,HiAlarmDisable,HiHiAlarmDisable,MinDevAlarmDisable,MajDevAlarmDisable,RocAlarmDisable,LoLoAlarmInhibitor,LoAlarmInhibitor,HiAlarmInhibitor,HiHiAlarmInhibitor,MinDevAlarmInhibitor,MajDevAlarmInhibitor,RocAlarmInhibitor,SymbolicName,,,,,,,\r\n',
    ':IOInt,Group,Comment,Logged,EventLogged,EventLoggingPriority,RetentiveValue,RetentiveAlarmParameters,AlarmValueDeadband,AlarmDevDeadband,EngUnits,InitialValue,MinEU,MaxEU,Deadband,LogDeadband,LoLoAlarmState,LoLoAlarmValue,LoLoAlarmPri,LoAlarmState,LoAlarmValue,LoAlarmPri,HiAlarmState,HiAlarmValue,HiAlarmPri,HiHiAlarmState,HiHiAlarmValue,HiHiAlarmPri,MinorDevAlarmState,MinorDevAlarmValue,MinorDevAlarmPri,MajorDevAlarmState,MajorDevAlarmValue,MajorDevAlarmPri,DevTarget,ROCAlarmState,ROCAlarmValue,ROCAlarmPri,ROCTimeBase,MinRaw,MaxRaw,Conversion,AccessName,ItemUseTagname,ItemName,ReadOnly,AlarmComment,AlarmAckModel,LoLoAlarmDisable,LoAlarmDisable,HiAlarmDisable,HiHiAlarmDisable,MinDevAlarmDisable,MajDevAlarmDisable,RocAlarmDisable,LoLoAlarmInhibitor,LoAlarmInhibitor,HiAlarmInhibitor,HiHiAlarmInhibitor,MinDevAlarmInhibitor,MajDevAlarmInhibitor,RocAlarmInhibitor,SymbolicName\r\n',
    ':MemoryReal,Group,Comment,Logged,EventLogged,EventLoggingPriority,RetentiveValue,RetentiveAlarmParameters,AlarmValueDeadband,AlarmDevDeadband,EngUnits,InitialValue,MinValue,MaxValue,Deadband,LogDeadband,LoLoAlarmState,LoLoAlarmValue,LoLoAlarmPri,LoAlarmState,LoAlarmValue,LoAlarmPri,HiAlarmState,HiAlarmValue,HiAlarmPri,HiHiAlarmState,HiHiAlarmValue,HiHiAlarmPri,MinorDevAlarmState,MinorDevAlarmValue,MinorDevAlarmPri,MajorDevAlarmState,MajorDevAlarmValue,MajorDevAlarmPri,DevTarget,ROCAlarmState,ROCAlarmValue,ROCAlarmPri,ROCTimeBase,AlarmComment,AlarmAckModel,LoLoAlarmDisable,LoAlarmDisable,HiAlarmDisable,HiHiAlarmDisable,MinDevAlarmDisable,MajDevAlarmDisable,RocAlarmDisable,LoLoAlarmInhibitor,LoAlarmInhibitor,HiAlarmInhibitor,HiHiAlarmInhibitor,MinDevAlarmInhibitor,MajDevAlarmInhibitor,RocAlarmInhibitor,SymbolicName,,,,,,,\r\n',
    ':IOReal,Group,Comment,Logged,EventLogged,EventLoggingPriority,RetentiveValue,RetentiveAlarmParameters,AlarmValueDeadband,AlarmDevDeadband,EngUnits,InitialValue,MinEU,MaxEU,Deadband,LogDeadband,LoLoAlarmState,LoLoAlarmValue,LoLoAlarmPri,LoAlarmState,LoAlarmValue,LoAlarmPri,HiAlarmState,HiAlarmValue,HiAlarmPri,HiHiAlarmState,HiHiAlarmValue,HiHiAlarmPri,MinorDevAlarmState,MinorDevAlarmValue,MinorDevAlarmPri,MajorDevAlarmState,MajorDevAlarmValue,MajorDevAlarmPri,DevTarget,ROCAlarmState,ROCAlarmValue,ROCAlarmPri,ROCTimeBase,MinRaw,MaxRaw,Conversion,AccessName,ItemUseTagname,ItemName,ReadOnly,AlarmComment,AlarmAckModel,LoLoAlarmDisable,LoAlarmDisable,HiAlarmDisable,HiHiAlarmDisable,MinDevAlarmDisable,MajDevAlarmDisable,RocAlarmDisable,LoLoAlarmInhibitor,LoAlarmInhibitor,HiAlarmInhibitor,HiHiAlarmInhibitor,MinDevAlarmInhibitor,MajDevAlarmInhibitor,RocAlarmInhibitor,SymbolicName\r\n',
    ':MemoryMsg,Group,Comment,Logged,EventLogged,EventLoggingPriority,RetentiveValue,MaxLength,InitialMessage,AlarmComment,SymbolicName,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\r\n',
    ':IOMsg,Group,Comment,Logged,EventLogged,EventLoggingPriority,RetentiveValue,MaxLength,InitialMessage,AccessName,ItemUseTagname,ItemName,ReadOnly,AlarmComment,SymbolicName,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\r\n',
    ':GroupVar,Group,Comment,SymbolicName,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\r\n',
    ':HistoryTrend,Group,Comment,SymbolicName,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\r\n',
    ':TagID,Group,Comment,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\r\n',
    ':IndirectDisc,Group,Comment,EventLogged,EventLoggingPriority,RetentiveValue,SymbolicName,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\r\n',
    ':IndirectAnalog,Group,Comment,EventLogged,EventLoggingPriority,RetentiveValue,SymbolicName,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\r\n',
    ':IndirectMsg,Group,Comment,EventLogged,EventLoggingPriority,RetentiveValue,SymbolicName,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\r\n'
]
for t in template:
    print(string_to_list(t))
