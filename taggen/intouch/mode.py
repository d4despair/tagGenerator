# @AUTHOR: DIOCAI
# DEVELOP TIME: 23/3/22 15:51

class MODE:
    """
    Intouch DB 导入模式包含一下三种

    ask: 询问模式，导入已存在变量时会询问执行怎样的操作

    replace: 取代模式，导入已存在的变量时，用新的变量取代原有的变量

    update: 更新模式

    """
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
            self._mode = value.lower()
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
    print('======== taggen/intouch/mode.py 测试 ========')
