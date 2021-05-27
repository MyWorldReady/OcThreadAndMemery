# -*- encoding: utf-8 -*-


import sys
import os
import re
import shutil

reload(sys)
sys.setdefaultencoding('utf-8')

path_root = os.getcwd()


def get_foler_name():
    p = path_root.replace("\\", "/")
    arr = p.split("/")
    name = arr[len(arr) - 1]
    return name


def do_pull(foler_name):
    print(foler_name + " pull")

    process = os.popen('git pull')  # return file
    output = process.read()
    process.close()

    print (foler_name + "   " + output)


foler_name = get_foler_name()
do_pull(foler_name)
