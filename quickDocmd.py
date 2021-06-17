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

path_root = os.getcwd()


def get_all_path():
    arr = []
    res = os.listdir(path_root)
    for name in res:
        full = path_root + "/" + name
        if not os.path.isfile(full):
            arr.append(full)
    arr.sort()
    return arr


def do_bk(folder_path):
    bk_dir = folder_path + "/bk"
    if not os.path.exists(bk_dir):
        os.mkdir(bk_dir)
    res = os.listdir(folder_path)
    for name in res:
        full = folder_path + "/" + name
        if os.path.isfile(full) and full.endswith(".sh"):
            old_path = full
            new_path = bk_dir + "/" + name
            shutil.move(old_path, new_path)


def do_remove_file(folder_path):
    remove_name = "_png2jpgOne.py"
    old_path = folder_path + "/" + remove_name
    new_path = folder_path + "/bk/" + remove_name
    shutil.move(old_path, new_path)


def do_copy_file(folder_path):
    copy_name = "quickDocmd.py"
    old_path = "C:/Users/Administrator/Downloads/456" + "/" + copy_name
    if IsMac():
        old_path = "/Users/wu/Downloads/123" + "/" + copy_name
    new_path = folder_path + "/" + copy_name
    shutil.copy(old_path, new_path)


# foler_arr = get_all_path()
# for folder_path in foler_arr:
#     do_bk(folder_path)


foler_arr = get_all_path()
for folder_path in foler_arr:
    do_copy_file(folder_path)
