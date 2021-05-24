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

# 需要清理的Tag
DelTagList = (
    'a',
    'div', 'span', 'code', 'font', 'li ', 'ul', 'ol', 'article', 'button', 'blockquote', 'path', 'svg', 'figure',
    'ins',
    'section', 'em', 'ignore_js_op', 'span', 'data-original-src', 'hr', 'strong')
# 需要精简的Tag
SimpeTagList = ('p ', 'br', 'pre', 'table', 'tbody', 'tr', 'td', 'h1', 'h2', 'h3', 'h4', 'h5')
# 和DelTagList，SimpeTagList正则匹配冲突的Tag
ConflictagList = (
    'i', 'b')
# 和DelTagList，SimpeTagList正则匹配冲突的Tag
ReplaceTagDic = {
    "。": "<br><br>\n\n",
}

# 已经清理过的html文件的标记
HasFlushHtmlMark = "<!--clear--clear--clear-->"
# 已经下载过图片的标记
HasDowloadPicMark = "<!--../img/-->"

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
    img = Image.open(PngPath)
    w = img.width
    h = img.height

    if w == 0:
        return
    if h == 0:
        return

    outW = w
    outH = h
    if outW > outH:
        if outW > 650:
            outW = 650
            ratio = float(outW) / w
            outH = int(h * ratio)
    else:
        if outH > 650:
            outH = 650
            ratio = float(outH) / h
            outW = int(w * ratio)

    infile = PngPath
    outfileNoExt = os.path.splitext(infile)[0] + ""
    outfile = outfileNoExt + ".jpg"
    img = Image.open(infile)
    outW = w
    if outW > 550:
        outW = 550
    outH = h
    if outH > 550:
        outH = 550
    img = img.resize((outW, outH), Image.ANTIALIAS)
    try:
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


def GetRemotePng(filePath, url, fileName):
    print("正在下载url------    " + url + "    fileName=" + fileName)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get(url, headers=headers)
    code = r.status_code
    if code != 200:
        print ("下载错误!!! code=" + str(code) + " filePath=" + str(filePath))
        return False
    with open(filePath, "wb") as f:
        f.write(r.content)
        f.flush()
    return True


def ThrowErrorAndDelDownload(downOkDic, strReason):
    for filePath in downOkDic.values():
        os.remove(filePath)
    raise (strReason + " , 已删除下载的图片, 正在退出程序 , 请重新执行脚本!!!".format())


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
                keyValueArr = content.split("=")
                key = keyValueArr[0]
                url = keyValueArr[1]
                url = url.replace('"', "").replace("<", "").replace(">", "")
                dic[key] = url
        bExitUrl = False
        url = ""

        if "../" in itemStr:
            ThrowErrorAndDelDownload(downOkDic, "图片路径包含../")

        if "src" in dic.keys():
            bExitUrl = True
            url = dic["src"]
        elif "data-original-src" in dic.keys():
            bExitUrl = True
            url = dic["data-original-src"]
        if url.startswith("://"):
            url = "https" + url
        elif url.startswith("//"):
            url = "https:" + url
        elif url.startswith("/"):
            if DomainName == '':
                print("当前url=   " + url)
                ThrowErrorAndDelDownload(downOkDic, "想要传入完整的域名部分(不能有引号) 如 https://www.baidu.com")
            else:
                url = DomainName + url

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

            result = GetRemotePng(filePath, url, fileName)
            if result:
                downOkDic[url] = filePath
                htmlTmpContent = __ReplaceImgTag(htmlTmpContent, itemStr, fileNameNoExt)
                PNG_JPG(filePath, ImgPath)
            else:
                os.remove(filePath)

    htmlTmpContent = __ClearTags(htmlTmpContent)
    htmlTmpContent = __ReplaceMoreBrTag(htmlTmpContent)
    if HasDowloadPicMark not in htmlTmpContent:
        htmlTmpContent = HasDowloadPicMark + htmlTmpContent
    if HasFlushHtmlMark not in htmlTmpContent:
        htmlTmpContent = HasFlushHtmlMark + htmlTmpContent

    f = open(htmlPath, "w")
    f.write(htmlTmpContent)
    f.flush()
    f.close()


def HandlerWithGit():
    shell = "git status -s | grep -a -Eoi 'Tutorial/.*html'"
    process = os.popen(shell)
    output = process.read()
    process.close()

    resArr = output.split("\n")
    for name in resArr:
        if StrIsContain(name, "Tutorial/"):
            fulllPath = path_root + "/" + name
            if os.path.exists(fulllPath):
                name = name.replace("Tutorial/", "")
                Download(name)


HandlerWithGit()

print("操作结束,退出程序")
