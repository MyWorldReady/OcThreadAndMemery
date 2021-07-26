# -*- encoding: utf-8 -*-


import sys
import pyperclip
import ConfigParser

reload(sys)
sys.setdefaultencoding('utf-8')
import os
import re
import requests
import time
import datetime
import random
import shutil
from PIL import Image


def IsMac():
    p = sys.platform
    return p == "darwin"


def IsWin():
    p = sys.platform
    return p == "win32"

IsMacShot = False
if IsMac():
    IsMacShot = True
if IsWin():
    os.system('chcp 65001')

path_root = os.getcwd()

ImgPath = path_root + "/img"
ScreenshotFolder = "Screenshot"

FilterPicTypeArr = [".png", ".JPG", ".jpg", ".JPEG", ".jpeg", ".gif"]


def get_destop_path():
    return os.path.join(os.path.expanduser("~"), 'Desktop')


ScreenshotPath = get_destop_path() + "/" + ScreenshotFolder
ConfigPath = ScreenshotPath + "/" + "config.ini"

ConfigInfoTag = 'info'
ConfigInfoPath = 'path'
ConfigInfoPicName = 'png_name'

if not os.path.exists(ScreenshotPath):
    raise RuntimeError("路径不存在 ScreenshotPath=" + ScreenshotPath)


def creat_name_no_ext():
    currentTimeStamp = int(time.time()) * 1000000
    mRandom = random.randint(1000, 90000)
    currentTimeStamp = currentTimeStamp + 1
    fileNameNoExt = "A_" + str(mRandom) + "_" + str(currentTimeStamp)
    return fileNameNoExt


def PNG_JPG(PngPath, outPutFolder):
    try:
        img = Image.open(PngPath)
    except:
        if os.path.isfile(PngPath):
            os.remove(PngPath)
        return
    w = img.width
    h = img.height

    if w == 0:
        return
    if h == 0:
        return

    outW = w
    outH = h
    if outW > outH:
        if IsMacShot:
            outW = int(outW / 3)
        elif outW > 550:
            outW = 550
        ratio = float(outW) / w
        outH = int(h * ratio)
    else:
        if IsMacShot:
            outH = int(outH / 3)
        elif outH > 550:
            outH = 550
        ratio = float(outH) / h
        outW = int(w * ratio)

    infile = PngPath
    outfileNoExt = os.path.splitext(infile)[0] + ""
    outfile = outfileNoExt + ".jpg"
    img = Image.open(infile)
    
    try:
        img = img.resize((outW, outH), Image.ANTIALIAS)
        if len(img.split()) == 4:
            # prevent IOError: cannot write mode RGBA as BMP
            r, g, b, a = img.split()
            img = Image.merge("RGB", (r, g, b))
            img.convert('RGB').save(outfile, quality=70)
        else:
            img.convert('RGB').save(outfile, quality=70)
        os.rename(outfile, outfileNoExt)
        os.remove(PngPath)
        return outfile
    except Exception as e:
        if os.path.exists(outfile):
            os.remove(outfile)
        if os.path.exists(PngPath):
            os.remove(PngPath)
        print(u"PNG转换JPG 错误 已删除源文件" + str(e))


def get_all_mac_screen_shot():
    arr = []
    destop_path = get_destop_path()
    res = os.listdir(destop_path)
    for name in res:
        full = destop_path + "/" + name
        if os.path.isfile(full) and name.find("Screenshot") != -1:
            arr.append(full)
    return arr


def get_all_screen_shot():
    if IsMac():
        return get_all_mac_screen_shot()
    raise RuntimeError("没有处理win")


def check_screen_shot_length(arr):
    cnt = len(arr)
    if cnt > 1:
        raise RuntimeError("有多张截图!!! arr=" + str(arr))
    if cnt == 0:
        raise RuntimeError("没有截图!!! arr=" + str(arr))


def move_pic_2_img(new_name):
    pic_path = ScreenshotPath + "/" + new_name
    new_path = ImgPath + "/" + new_name
    shutil.move(pic_path, new_path)


def move_pic_2_Screenshot(pic_path, new_name):
    new_path = ScreenshotPath + "/" + new_name
    shutil.move(pic_path, new_path)
    return new_path


def create_config_file(path):
    if not os.path.exists(path):
        new_name_no_ext = creat_name_no_ext()
        f = open(path, "w")
        content = "[{}]".format(ConfigInfoTag) + "\n" + ConfigInfoPath + "=\n" + "{}".format(
            ConfigInfoPicName) + "={}\n".format(new_name_no_ext)
        f.write(content)
        f.flush()
        f.close()
        return False
    return True


def auto_add_one_by_name(pic_name):
    mutipleStr = str(1000000)
    base_name = pic_name[:-len(mutipleStr) + 1]
    mutil_name = pic_name.replace(base_name, "")
    new_mutil_name = str(int(mutil_name) + 1)
    ex_len = len(mutil_name) - len(new_mutil_name)
    for i in range(0, ex_len):
        new_mutil_name = "0" + new_mutil_name
    new_name = base_name + new_mutil_name
    return new_name


def flush_new_pic_info():
    create_config_file(ConfigPath)

    cf = ConfigParser.ConfigParser()
    cf.read(ConfigPath)

    project_path = cf.get(ConfigInfoTag, ConfigInfoPath)
    cf.set(ConfigInfoTag, ConfigInfoPath, path_root)
    if project_path == path_root:
        read_pic_name = cf.get(ConfigInfoTag, ConfigInfoPicName)
        new_pic_name = auto_add_one_by_name(read_pic_name)
        cf.set(ConfigInfoTag, ConfigInfoPicName, new_pic_name)
    else:
        new_pic_name = creat_name_no_ext()
        cf.set(ConfigInfoTag, ConfigInfoPicName, new_pic_name)

    with open(ConfigPath, "w+") as f:
        cf.write(f)
    return new_pic_name


def str_is_contain(m_str, mark):
    return str(m_str).find(mark) != -1


def get_pic_path():
    pic_arr = []
    res = os.listdir(ScreenshotPath)
    for name in res:
        full = ScreenshotPath + "/" + name
        if os.path.isfile(full):
            for m_type in FilterPicTypeArr:
                if name.endswith(m_type):
                    pic_arr.append(full)

    if len(pic_arr) > 1:
        raise RuntimeError("{}多张图片 ".format(ScreenshotPath))
    if len(pic_arr) == 1:
        return pic_arr[0]

    if IsWin():
        raise RuntimeError("windows的截图需要放在路径{} ".format(ScreenshotPath))

    screen_shot_arr = get_all_screen_shot()
    check_screen_shot_length(screen_shot_arr)
    pic_path = screen_shot_arr[0]

    return pic_path


new_name_no_ext = flush_new_pic_info()
new_name = new_name_no_ext + ".png"
pic_path = get_pic_path()
pic_path = move_pic_2_Screenshot(pic_path, new_name)
PNG_JPG(pic_path, "")

move_pic_2_img(new_name_no_ext)
pyperclip.copy('<br><img src="../img/{}"><br>'.format(new_name_no_ext))

print ("生成文件名 {}".format(new_name_no_ext))
print ("操作结束 退出程序")
