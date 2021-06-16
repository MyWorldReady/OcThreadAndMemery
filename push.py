# -*- encoding: utf-8 -*-


import sys
import os
import re
import shutil

reload(sys)
sys.setdefaultencoding('utf-8')

def IsMac():
    p = sys.platform
    return p == "darwin"

def IsWin():
    p = sys.platform
    return p == "win32"


if IsWin():
    os.system('chcp 65001')

path_root = os.getcwd()


def get_foler_name():
    p = path_root.replace("\\", "/")
    arr = p.split("/")
    name = arr[len(arr) - 1]
    return name


def do_push(foler_name):
    print(foler_name + " push")
    cmd = ""
    if IsMac():
        cmd = "git add ./;git commit -m ex;git push"
    else:
        cmd = "git add ./&git commit -m ex&git push"

    process = os.popen(cmd)
    output = process.read()
    process.close()

    print (foler_name + "   " + output)

foler_name = get_foler_name()
do_push(foler_name)
