# -*- encoding: utf-8 -*-


import sys
import os
import re
import shutil
import thread
import threading
import time

reload(sys)
sys.setdefaultencoding('utf-8')

path_root = os.getcwd()

newHtmlPath = path_root + "/index.html"


def IsMac():
    p = sys.platform
    return p == "darwin"


def IsWin():
    p = sys.platform
    return p == "win32"


def OpenInChrome():
    if IsMac():
        os.system("open {}".format(newHtmlPath))
    elif IsWin():
        x86Exe = "/c/Program Files (x86)/Google/Chrome/Application/chrome.exe"
        x64Exe = "/c/Program Files/Google/Chrome/Application/chrome.exe"
        os.system("{} {}".format(x64Exe,newHtmlPath))
    else:
        raise ("没有处理这个平台")


OpenInChrome()