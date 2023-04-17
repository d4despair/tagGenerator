# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/22 15:51


class MODE:
    _mode = 'ask'
    _modes = (
        'ask',
        'replace',
        'update',
    )

    def __init__(self, mode_name='ask'):
        self.mode = mode_name

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        # 错误提示
        if value.lower() in self._modes:
            self._mode = value
        else:
            raise ValueError("'{}' 不是 Intouch DB 文件的模式，可选模式如下{}".format(value, self._modes))

    @property
    def csv_format(self) -> list[str]:
        return [':mode={}'.format(self.mode)]


if __name__ == '__main__':
    print()
    print('======== taggen/intouch/mode.py 测试 ========')
    print('正常情况')
    md = MODE('UPDATE')
    print(md.csv_format)
    print()
    print('报错情况')
    md = MODE('updated')
    print(md.csv_format)
    print('======== taggen/intouch/mode.py 测试 ========')
