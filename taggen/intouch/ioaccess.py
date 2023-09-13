# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/4/11 14:39
from header import IO_ACCESS_HEADER
from util import StringListObject


class IOAccess(StringListObject):
    __slots__ = (
        'io_access',
        'application',
        'topic',
        'advise_active',
        'dde_protocol',
        'sec_application',
        'sec_topic',
        'sec_advise_active',
        'sec_dde_protocol',
        'failover_expression',
        'failover_deadband',
        'dfo_flag',
        'fbd_flag',
        'failback_deadband',
    )

    def __init__(self, io_access='kep1200', application=r'server_runtime', topic='kep1200', advise_active='Yes',
                 dde_protocol='No', sec_application='',
                 sec_topic='', sec_advise_active='', sec_dde_protocol='', failover_expression='', failover_deadband='',
                 dfo_flag='', fbd_flag='', failback_deadband=''):
        self.io_access = io_access
        self.application = application
        self.topic = topic
        self.advise_active = advise_active
        self.dde_protocol = dde_protocol
        self.sec_application = sec_application
        self.sec_topic = sec_topic
        self.sec_advise_active = sec_advise_active
        self.sec_dde_protocol = sec_dde_protocol
        self.failover_expression = failover_expression
        self.failover_deadband = failover_deadband
        self.dfo_flag = dfo_flag
        self.fbd_flag = fbd_flag
        self.failback_deadband = failback_deadband


IO_ACCESS_GALAXY = IOAccess(io_access='Galaxy', application=r'\\NA\\NA', topic='NA', dde_protocol='MX')
IO_ACCESS_KEP1200 = IOAccess(io_access='kep1200', application=r'server_runtime', topic='kep1200')
IO_ACCESS_KEP1500 = IOAccess(io_access='kep1500', application=r'server_runtime', topic='kep1500')
IO_ACCESS_DASERVER = IOAccess(io_access='S7-300', application=r'DASSIDirect', topic='S7PLC')


def test():
    print('test')
    print(IO_ACCESS_HEADER)
    print(IO_ACCESS_KEP1200)
    print(IO_ACCESS_DASERVER)
    print(IO_ACCESS_GALAXY)
    pass


if __name__ == '__main__':
    test()
