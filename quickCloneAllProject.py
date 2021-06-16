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


def IsMac():
    p = sys.platform
    return p == "darwin"


def IsWin():
    p = sys.platform
    return p == "win32"


if IsWin():
    os.system('chcp 65001')

path_root = os.getcwd()
AllSubjectTxt = path_root + "/AllSubject/allSubject.txt"

if not os.path.isfile(AllSubjectTxt):
    print("allSubject.txt 不存在")
    exit(0)


def get_all_folder_name():
    arr = []
    res = os.listdir(path_root)
    for name in res:
        full = path_root + "/" + name
        if not os.path.isfile(full):
            arr.append(name)
    arr.sort()
    return arr


def get_all_name():
    f = open(AllSubjectTxt, "r")
    content = f.read()
    f.close()
    res = []
    arr = content.split("\n")
    for val in arr:
        name = val.replace(" ", "")
        if not name == "":
            res.append(name)
    return res


def do_clone(git_name):
    print (git_name + "   start\n")
    cmd = "git clone https://github.com/MyWorldReady/" + git_name
    if IsWin():
        cmd = cmd.decode('utf-8').encode('gb2312')
    os.system(cmd)

    print (git_name + "   finish\n")


all_name = get_all_name()
all_folder_name = get_all_folder_name()
for git_name in all_name:
    if git_name not in all_folder_name:
        do_clone(git_name)
