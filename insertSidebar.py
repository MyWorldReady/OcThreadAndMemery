# -*- encoding: utf-8 -*-


import sys
import os
import re

reload(sys)
sys.setdefaultencoding('utf-8')

len_argv = len(sys.argv)

InputFileNameNoExt = ''
if len_argv == 2:
    InputFileNameNoExt = str(sys.argv[1])
elif len_argv > 2:
    print ("不能含空格")
    exit(0)
else:
    print("没有传入文件名")
    exit(0)
# InputFileNameNoExt = "q7"
InputFileName = InputFileNameNoExt + ".html"

filepath = os.getcwd()

sidebarHtmlPath = "{}/menus/sidebar.html".format(filepath)
copyHtmlPath = "{}/copy.html".format(filepath)
newHtmlPath = "{}/Tutorial/{}".format(filepath, InputFileName)


def InputFileExit():
    f = open(sidebarHtmlPath, "r")
    content = f.read()
    f.close()
    exitStr = InputFileName in content
    return exitStr


def CrateFile():
    f = open(copyHtmlPath, "r")
    content = f.read()
    f.close()
    f = open(newHtmlPath, "w")
    replaceMark = 'sans-serif">'
    h1Str = '<h1>{}</h1>'.format(InputFileNameNoExt)
    content = content.replace(replaceMark, replaceMark + "\n\n" + h1Str)
    f.write(content)
    f.flush()
    f.close()


def IsMac():
    p = sys.platform
    return p == "darwin"


def IsWin():
    p = sys.platform
    return p == "win32"


def OpenInSublime():
    if IsMac():
        os.system("subl {}".format(newHtmlPath))
    elif IsWin():
        os.system("/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl {}".format(newHtmlPath))
    else:
        raise ("没有处理这个平台")


def OpenInChrome():
    if IsMac():
        os.system("open {}".format(newHtmlPath))
    elif IsWin():
        x86Exe = "/c/Program Files (x86)/Google/Chrome/Application/chrome.exe"
        x64Exe = "/c/Program Files/Google/Chrome/Application/chrome.exe"
        os.system("x64Exe {}".format(newHtmlPath))
    else:
        raise ("没有处理这个平台")


def InputSidebar():
    inserStr = '<li><a href="../Tutorial/{0}" target="main">{1}</a></li>'.format(InputFileName, InputFileNameNoExt)
    f = open(sidebarHtmlPath, "r")
    content = f.read()
    f.close()
    content = content.replace("</ul>", inserStr + "\n" + "</ul>")
    f = open(sidebarHtmlPath, "w")
    f.write(content)
    f.flush()
    f.close()


exitFile = InputFileExit()
if exitFile:
    print ("{}  文件已经存在!!!".format(InputFileName))
    exit(0)

InputSidebar()
CrateFile()
OpenInSublime()
OpenInChrome()
