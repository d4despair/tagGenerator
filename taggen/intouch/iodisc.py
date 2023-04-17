# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/4/12 22:49

# ========================== IODisc 开始 ==========================

class IODisc:
    __slots__ = (
        'io_disc',
        'group',
        'comment',
        'logged',
        'event_logged',
        'event_logging_priority',
        'retentive_value',
        'initial_disc',
        'off_msg',
        'on_msg',
        'alarm_state',
        'alarm_pri',
        'd_conversion',
        'access_name',
        'item_use_tagname',
        'item_name',
        'read_only',
        'alarm_comment',
        'alarm_ack_model',
        'dsc_alarm_disable',
        'dsc_alarm_inhibitor',
        'symbolic_name',
    )

    def __init__(self, io_disc, group, comment='', logged='No', event_logged='No', event_logging_priority=0,
                 retentive_value='No', initial_disc='off', off_msg='', on_msg='', alarm_state='None', alarm_pri='',
                 d_conversion='Direct', access_name='kep1500', item_use_tagname='No', item_name='', read_only='No',
                 alarm_comment='', alarm_ack_model=0, dsc_alarm_disable=0, dsc_alarm_inhibitor='', symbolic_name=''):
        self.io_disc = io_disc
        self.group = group
        self.comment = comment
        self.logged = logged
        self.event_logged = event_logged
        self.event_logging_priority = event_logging_priority
        self.retentive_value = retentive_value
        self.initial_disc = initial_disc
        self.off_msg = off_msg
        self.on_msg = on_msg
        self.alarm_state = alarm_state
        self.alarm_pri = alarm_pri
        self.d_conversion = d_conversion
        self.access_name = access_name
        self.item_use_tagname = item_use_tagname
        self.item_name = item_name
        self.read_only = read_only
        self.alarm_comment = alarm_comment
        self.alarm_ack_model = alarm_ack_model
        self.dsc_alarm_disable = dsc_alarm_disable
        self.dsc_alarm_inhibitor = dsc_alarm_inhibitor
        self.symbolic_name = symbolic_name

    @property
    def tagname(self):
        return self.io_disc


# ========================== IODisc 结束 ==========================

def test():
    pass


if __name__ == '__main__':
    test()
