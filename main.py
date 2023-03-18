import os,sys
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


desktop_bg()
def get_fill():
