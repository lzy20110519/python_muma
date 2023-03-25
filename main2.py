# -*- coding: CP936 -*-
from __future__ import print_function
import cv2
import ctypes
import os
import string
import sys
import threading
from pyscreeze import unicode
import win32api,win32con
from win10toast import ToastNotifier
toaster = ToastNotifier()

def run_images():
    img = cv2.imread("./images/bg.jpg")

    out_win = "output_style_full_screen"
    cv2.namedWindow(out_win, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(out_win, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow(out_win, img)
    cv2.waitKey(0)


def no_input():
    import time
    class keyboardDisable():

        def start(self):
            self.on = True

        def stop(self):
            self.on = False

        def __call__(self):
            while self.on:
                msvcrt.getwch()

        def __init__(self):
            self.on = False
            import msvcrt

    disable = keyboardDisable()
    disable.start()
    time.sleep(10)
    disable.stop()


def windows_zha():
    from win10toast import ToastNotifier
    from win10toast import ToastNotifier
    toaster = ToastNotifier()
    toaster = ToastNotifier()
    toaster.show_toast("Windows信息",
                        "系统错误--严重错误",
                        icon_path="./images/bg.jpg",
                        duration=0)


# root()

t1 = threading.Thread(target=run_images)
t2 = threading.Thread(target=windows_zha)

t2.start()
t1.start()

