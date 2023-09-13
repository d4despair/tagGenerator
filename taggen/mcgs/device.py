# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/7/11 8:53


_DEVICE_INFO = ['组态设备名称', '驱动库文件路径', '驱动构件名称', '驱动构件版本']
_DEVICE_INFO_EN = ['device_name', 'driver_path', 'driver_name', 'driver_version']
_DEV_INFO = {k: v for k, v in zip(_DEVICE_INFO, _DEVICE_INFO_EN)}
_DEV_INFO_REV = {k: v for k, v in zip(_DEVICE_INFO_EN, _DEVICE_INFO)}


class McgsDevice:
    __slots__ = tuple(_DEVICE_INFO_EN)

    def __init__(self, device_name='', driver_path='', driver_name='', driver_version=''):
        self.__setattr__(_DEVICE_INFO_EN[0], device_name)
        self.__setattr__(_DEVICE_INFO_EN[1], driver_path)
        self.__setattr__(_DEVICE_INFO_EN[2], driver_name)
        self.__setattr__(_DEVICE_INFO_EN[3], driver_version)
        # self.device_name = device_name
        # self.driver_path = driver_path
        # self.driver_name = driver_name
        # self.driver_version = driver_version

    @property
    def info(self):
        return [self.__getattribute__(k) for k in self.__slots__]

    @property
    def list_info(self):
        return [{_DEV_INFO_REV[k]: self.__getattribute__(k)} for k in self.__slots__]


def device_from_csv(csv_file: str):
    import csv
    import re
    try:
        with open(csv_file, 'r', newline='', encoding='ANSI') as f:
            global _DEV_INFO
            d_info = {}
            reader = csv.reader(f)
            for row in reader:
                if reader.line_num > 4:
                    break
                key, val = re.match(r'(\w+):(.*)', row[0]).groups()
                d_info[_DEV_INFO[key]] = val
    except FileNotFoundError as e:
        print(e)
    else:
        print(d_info)
        return McgsDevice(**d_info)


if __name__ == '__main__':
    d = device_from_csv(r"D:\Siemens_1200gg.csv")
    print(d.info)
    print(d.list_info)
    # print(d.driver_name)
