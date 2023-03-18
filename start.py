from __future__ import print_function

import ctypes
import os
import sys

from pyscreeze import unicode


def root():
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if is_admin():
        print('start')
        os.system('python main.py')
    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:  # in python2.x
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)




if __name__ == '__main__':
    print('执行中……')
    root()
    input()
