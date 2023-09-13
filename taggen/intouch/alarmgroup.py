# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/4/12 13:36

from util import StringListObject

ALARM_GROUP_HEADER = [':AlarmGroup', 'Group', 'Comment', 'EventLogged', 'EventLoggingPriority', 'LoLoAlarmDisable',
                      'LoAlarmDisable', 'HiAlarmDisable', 'HiHiAlarmDisable', 'MinDevAlarmDisable',
                      'MajDevAlarmDisable',
                      'RocAlarmDisable', 'DSCAlarmDisable', 'LoLoAlarmInhibitor', 'LoAlarmInhibitor',
                      'HiAlarmInhibitor',
                      'HiHiAlarmInhibitor', 'MinDevAlarmInhibitor', 'MajDevAlarmInhibitor', 'RocAlarmInhibitor',
                      'DSCAlarmInhibitor',
                      ]

ALARM_GROUP_HEADER_PYTHON = [':alarm_group', 'group', 'comment', 'event_logged', 'event_logging_priority',
                             'lolo_alarm_disable', 'lo_alarm_disable', 'hi_alarm_disable', 'hihi_alarm_disable',
                             'min_dev_alarm_disable', 'maj_dev_alarm_disable', 'roc_alarm_disable', 'dsc_alarm_disable',
                             'lolo_alarm_inhibitor', 'lo_alarm_inhibitor', 'hi_alarm_inhibitor',
                             'hihi_alarm_inhibitor', 'min_dev_alarm_inhibitor', 'maj_dev_alarm_inhibitor',
                             'roc_alarm_inhibitor', 'dsc_alarm_inhibitor']

ALARM_GROUP_DICT = {python: camel for python, camel in zip(ALARM_GROUP_HEADER_PYTHON, ALARM_GROUP_HEADER)}


# ========================== AlarmGroup 开始 ==========================

class AlarmGroup(StringListObject):
    __slots__ = (
        'alarm_group',
        'group',
        'comment',
        'event_logged',
        'event_logging_priority',
        'lolo_alarm_disable',
        'lo_alarm_disable',
        'hi_alarm_disable',
        'hihi_alarm_disable',
        'min_dev_alarm_disable',
        'maj_dev_alarm_disable',
        'roc_alarm_disable',
        'dsc_alarm_disable',
        'lolo_alarm_inhibitor',
        'lo_alarm_inhibitor',
        'hi_alarm_inhibitor',
        'hihi_alarm_inhibitor',
        'min_dev_alarm_inhibitor',
        'maj_dev_alarm_inhibitor',
        'roc_alarm_inhibitor',
        'dsc_alarm_inhibitor',
    )

    def __init__(self, alarm_group, group='$System', comment='', event_logged='Yes', event_logging_priority=999,
                 lolo_alarm_disable=0, lo_alarm_disable=0, hi_alarm_disable=0, hihi_alarm_disable=0,
                 min_dev_alarm_disable=0, maj_dev_alarm_disable=0, roc_alarm_disable=0, dsc_alarm_disable=0,
                 lolo_alarm_inhibitor='', lo_alarm_inhibitor='', hi_alarm_inhibitor='', hihi_alarm_inhibitor='',
                 min_dev_alarm_inhibitor='', maj_dev_alarm_inhibitor='', roc_alarm_inhibitor='',
                 dsc_alarm_inhibitor=''):
        self.alarm_group = alarm_group
        self.group = group
        self.comment = comment
        self.event_logged = event_logged
        self.event_logging_priority = event_logging_priority
        self.lolo_alarm_disable = lolo_alarm_disable
        self.lo_alarm_disable = lo_alarm_disable
        self.hi_alarm_disable = hi_alarm_disable
        self.hihi_alarm_disable = hihi_alarm_disable
        self.min_dev_alarm_disable = min_dev_alarm_disable
        self.maj_dev_alarm_disable = maj_dev_alarm_disable
        self.roc_alarm_disable = roc_alarm_disable
        self.dsc_alarm_disable = dsc_alarm_disable
        self.lolo_alarm_inhibitor = lolo_alarm_inhibitor
        self.lo_alarm_inhibitor = lo_alarm_inhibitor
        self.hi_alarm_inhibitor = hi_alarm_inhibitor
        self.hihi_alarm_inhibitor = hihi_alarm_inhibitor
        self.min_dev_alarm_inhibitor = min_dev_alarm_inhibitor
        self.maj_dev_alarm_inhibitor = maj_dev_alarm_inhibitor
        self.roc_alarm_inhibitor = roc_alarm_inhibitor
        self.dsc_alarm_inhibitor = dsc_alarm_inhibitor


def test():
    print('test')
    from util import camel_list_to_python, print_class_string
    print(ALARM_GROUP_HEADER)
    python_style_field = camel_list_to_python(ALARM_GROUP_HEADER)
    print(python_style_field)
    print_class_string('AlarmGroup', python_style_field)
    dry = AlarmGroup('DRY')
    l = dry.csv_format
    [print(i, end=',') for i in l]
    print()

    print(l)


if __name__ == '__main__':
    test()
