# -*- encoding: utf-8 -*-


import sys

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

# 清理匹配,比如<noscript[\s\S]*?</noscript>
PowDelMatchList = (
    'noscript', 'noscript')
# 需要清理的Tag
DelTagList = (
    'a', 'u',
    'div', 'span', 'code', 'font', 'li ', 'article', 'button', 'blockquote', 'path', 'svg', 'figure',
    'ins', 'noscript',
    'section', 'em', 'ignore_js_op', 'span', 'data-original-src', 'hr', 'strong', 'iframe', 'mark', 'style')
# 需要精简的Tag
SimpeTagList = ('p ', 'br', 'pre', 'table', 'tbody', 'tr', 'td', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol')
# 和DelTagList，SimpeTagList正则匹配冲突的Tag
ConflictagList = (
    'i', 'b')
# 和DelTagList，SimpeTagList正则匹配冲突的Tag
ReplaceTagDic = {
    "。": "<br><br>\n\n",
    "¶": "",
    "<p >": "<p>",
}

# 已经清理过的html文件的标记
HasFlushHtmlMark = "<!--clear--clear--clear-->"
# 已经下载过图片的标记
HasDowloadPicMark = "<!--../img/-->"


def get_destop_path():
    return os.path.join(os.path.expanduser("~"), 'Desktop')


def get_downloads_path():
    return os.path.join(os.path.expanduser("~"), 'Downloads')


def get_fatkun_path():
    return os.path.join(get_downloads_path(), 'Fatkun')


def getAll(path):
    Dirlist = []
    Filelist = []
    for home, dirs, files in os.walk(path):
        # 获得所有文件夹
        for dirname in dirs:
            Dirlist.append(os.path.join(home, dirname))
        # 获得所有文件
        for filename in files:
            Filelist.append(os.path.join(home, filename))
    return Dirlist, Filelist  # 返回所有文件夹列表和文件列表[dirlist, filelist]


def IsMac():
    p = sys.platform
    return p == "darwin"


def IsWin():
    p = sys.platform
    return p == "win32"


IsMacShot = False

if IsWin():
    os.system('chcp 65001')

path_root = os.getcwd()

ImgPath = path_root + "/img"
RootHtmlPath = path_root + "/Tutorial"

len_argv = len(sys.argv)

DomainName = ''
if len_argv > 1:
    DomainName = str(sys.argv[1])


def GetAllHtmlFile():
    arr = []
    datanames = os.listdir(RootHtmlPath)
    for dataname in datanames:
        if os.path.splitext(dataname)[1] == '.html':
            arr.append(dataname)
    return arr


def StrIsContain(mStr, mark):
    return mStr.find(mark) != -1


def PNG_JPG(PngPath, outPutFolder):
    try:
        img = Image.open(PngPath)
    except:
        if os.path.isfile(PngPath):
            os.remove(PngPath)
        return False
    w = img.width
    h = img.height

    if w == 0:
        return False
    if h == 0:
        return False

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
        return True
    except Exception as e:
        if os.path.exists(outfile):
            os.remove(outfile)
        if os.path.exists(PngPath):
            os.remove(PngPath)
        print(u"PNG转换JPG 错误 已删除源文件" + e)
    return False


# def GetRemotePng(filePath, url, fileName):
#     print("正在下载url------    " + url + "    fileName=" + fileName)
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
#     r = requests.get(url, headers=headers)
#     code = r.status_code
#     if code != 200:
#         print ("下载错误!!! code={}".format(code) + " filePath={}".format(filePath))
#         return False
#     with open(filePath, "wb") as f:
#         f.write(r.content)
#         f.flush()
#     return True
#
def GetRemotePng(filePath, url, fileName):
    nameWithExt = GetRemotePngNameWithExt(filePath, url, fileName)
    fatkun_path = get_fatkun_path()
    arr = []
    resultArr = getAll(fatkun_path)
    fileArr = resultArr[1]
    exit_file = False
    src_abs_path = ""
    for abs_path in fileArr:
        tmp_path = abs_path.replace("\\", "/")
        if "/" in tmp_path:
            tmp_arr = tmp_path.split("/")
            length = len(tmp_arr)
            tmp_nameWithExt = tmp_arr[length - 1]
            if tmp_nameWithExt == nameWithExt:
                exit_file = True
                src_abs_path = abs_path
                break

    exit_foler = os.path.exists(get_fatkun_path())
    if not exit_foler:
        ThrowError("Fatkun 路径不存在!!!")

    if not exit_file:
        ThrowError("没有这个下载图片,请手动保存到 Fatkun 路径!!!nameWithExt=" + nameWithExt)

    shutil.copyfile(src_abs_path, filePath)
    return True


def GetRemotePngNameWithExt(filePath, url, fileName):
    tmpUrl = url.replace("\\", "/")
    nameWithExt = ""
    if "?" in tmpUrl:
        arr = tmpUrl.split("?")
        length = len(arr)
        tmpUrl = arr[0]
    if "/" in tmpUrl:
        arr = tmpUrl.split("/")
        length = len(arr)
        nameWithExt = arr[length - 1]
    else:
        ThrowError("这里代码还没有实现!!!")
    if nameWithExt == "":
        ThrowError("获取图片名的结果是空字符串!!!")
    return nameWithExt


def ThrowError(strReason):
    raise Exception(strReason)


def ThrowErrorAndDelDownload(downOkDic, strReason):
    for filePath in downOkDic.values():
        if os.path.exists(filePath):
            os.remove(filePath)
        paht_no_ext = filePath.replace(".png", "")
        if os.path.exists(paht_no_ext):
            os.remove(paht_no_ext)
    ThrowError(strReason)


def __ReplaceMoreBrTag(htmlTmpContent):
    htmlTmpContent = htmlTmpContent.replace('<br><br><br><br>', '<br>')
    htmlTmpContent = htmlTmpContent.replace('<br><br><br>', '<br>')
    return htmlTmpContent


def __ReplaceImgTag(htmlTmpContent, imgTagStr, fileName):
    htmlTmpContent = htmlTmpContent.replace(imgTagStr, '<br><img src="../img/' + fileName + '"><br>')
    return htmlTmpContent


def __ClearTag(htmlTmpContent, mTagStr, isDelTag):
    if isDelTag:
        htmlTmpContent = re.sub(r'<{0}[\s\S]*?>'.format(mTagStr), "", htmlTmpContent)
        htmlTmpContent = htmlTmpContent.replace("</{}>".format(mTagStr), "")
    else:
        htmlTmpContent = re.sub(r'<{0}[\s\S]*?>'.format(mTagStr), "<{0}>".format(mTagStr), htmlTmpContent)
    return htmlTmpContent


def __PowDeleteTags(htmlTmpContent):
    for tag in PowDelMatchList:
        htmlTmpContent = re.sub(r'<{}[\s\S]*?</{}>'.format(tag, tag), "", htmlTmpContent)
    return htmlTmpContent


def __ClearTags(htmlTmpContent):
    for tag in DelTagList:
        htmlTmpContent = __ClearTag(htmlTmpContent, tag, True)
    for tag in SimpeTagList:
        htmlTmpContent = __ClearTag(htmlTmpContent, tag, False)
    for tag in ConflictagList:
        # 注意:这里是匹配多了一个空格
        htmlTmpContent = re.sub(r'<{0} [\s\S]*?>'.format(tag), "", htmlTmpContent)
        htmlTmpContent = htmlTmpContent.replace("<{}>".format(tag), "")
        htmlTmpContent = htmlTmpContent.replace("</{}>".format(tag), "")
    for key, item in ReplaceTagDic.items():
        htmlTmpContent = htmlTmpContent.replace(key, item)

    htmlTmpContent = htmlTmpContent.replace("<br><br>", "<br><br>\n\n")

    return htmlTmpContent


def Download(htmlFileName):
    htmlPath = RootHtmlPath + "/" + htmlFileName
    f = open(htmlPath.decode('utf-8'), "r")
    htmlOriContent = f.read()
    htmlOriContent = __PowDeleteTags(htmlOriContent)
    htmlTmpContent = htmlOriContent
    f.close()

    global HasFlushHtmlMark
    if HasFlushHtmlMark in htmlTmpContent:
        # print ("{0}   已经清理,将跳过此文件".format(htmlFileName))
        return

    datepat = re.compile(r'<img[\s\S]*?>')
    downOkDic = {}
    currentTimeStamp = int(time.time()) * 1000000
    mRandom = random.randint(1000, 90000)
    for item in datepat.findall(htmlOriContent):
        itemStr = str(item)
        arr = itemStr.split(" ")
        dic = {}
        for arrItem in arr:
            content = str(arrItem)
            if StrIsContain(content, "src="):
                keyValueArr = content.split("src=")
                key = keyValueArr[0] + "src"
                url = keyValueArr[1]
                url = url.replace('"', "").replace("<", "").replace(">", "")
                dic[key] = url
        bExitUrl = False
        url = ""

        if "src" in dic.keys():
            bExitUrl = True
            url = dic["src"]
        elif "data-original-src" in dic.keys():
            bExitUrl = True
            url = dic["data-original-src"]

        if url in downOkDic.keys():
            htmlTmpContent = __ReplaceImgTag(htmlTmpContent, itemStr, fileNameNoExt)
            continue

        # A_7449_1614786177000001
        if bExitUrl:
            currentTimeStamp = currentTimeStamp + 1
            fileNameNoExt = "A_" + str(mRandom) + "_" + str(currentTimeStamp)
            fileName = fileNameNoExt + ".png"
            filePath = ImgPath + "/" + fileName

            if os.path.exists(filePath):
                ThrowErrorAndDelDownload(downOkDic, "图片保存路径重复")

            try:
                downOkDic[url] = filePath
                result = GetRemotePng(filePath, url, fileName)

                if result:
                    htmlTmpContent = __ReplaceImgTag(htmlTmpContent, itemStr, fileNameNoExt)

                    try:
                        jpg_res = PNG_JPG(filePath, ImgPath)
                        if not jpg_res:
                            ThrowErrorAndDelDownload(downOkDic, "图片转jpg失败!!  正在处理:filePath={}".format(filePath))
                    except Exception as e:
                        ThrowErrorAndDelDownload(downOkDic, " {} 图片转jpg!!  正在处理:filePath= {}".format(e, filePath))
                        return

                else:
                    os.remove(filePath)
            except Exception as e:
                ThrowErrorAndDelDownload(downOkDic, "下载失败!! {}   正在处理:{}".format(e, url))
                return

    htmlTmpContent = __ClearTags(htmlTmpContent)
    htmlTmpContent = __ReplaceMoreBrTag(htmlTmpContent)
    if HasDowloadPicMark not in htmlTmpContent:
        htmlTmpContent = HasDowloadPicMark + htmlTmpContent
    if HasFlushHtmlMark not in htmlTmpContent:
        htmlTmpContent = HasFlushHtmlMark + htmlTmpContent

    if IsWin():
        # git bash 控制台是gb2312编码
        htmlPath = htmlPath.decode('utf-8').encode('gb2312')
    f = open(htmlPath, "w")
    f.write(htmlTmpContent)
    f.flush()
    f.close()


def CheckAndDeleteDir(fulllPath):
    if os.path.exists(fulllPath):
        shutil.rmtree(fulllPath)


def HandlerWithGit():
    shell = "git status -s | grep -a -Eoi 'Tutorial/.*html'"
    process = os.popen(shell)
    output = process.read()
    process.close()
    
    resArr = output.split("\n")

    for name in resArr:
        if StrIsContain(name, "Tutorial/"):
            fulllPath = path_root + "/" + name
            if IsWin():
                # git bash 控制台是gb2312编码
                fulllPath = fulllPath.decode('utf-8').encode('gb2312')
            if os.path.exists(fulllPath):
                name = name.replace("Tutorial/", "")
                Download(name)


HandlerWithGit()

CheckAndDeleteDir(get_fatkun_path())

print("操作结束,退出程序")
