# -*- encoding: utf-8 -*-


import sys
import pyperclip
import ConfigParser

reload(sys)
sys.setdefaultencoding('utf-8')
import os
import re
import shutil

path_root = os.getcwd()

TutorialPath = path_root + "/Tutorial"
sidebarHtmlPath = "{}/menus/sidebar.html".format(path_root)

HTMLH1TITLE = "<h1>问题导出</h1>"
EXPORTHTMLH1TAG = "<h1>看完此文章需理解</h1>"
EXPORT2FILEPATH = TutorialPath + "/" + u"问题导出.html"

#这个是按照Tutorial路径下html自己的排序导出
# def get_all_html():
#     res = []
#     arr = os.listdir(unicode(TutorialPath, "utf-8"))
#     for name in arr:
#         if name.endswith(".html"):
#             # res.append(name.decode("utf-8"))
#             res.append(name)
#     return res

#这个是按照sidebar.html的排序导出
def get_all_html():
    path = sidebarHtmlPath
    f = open(path, "r")
    content = f.read()
    f.close()

    content = content.decode("utf-8")
    datepat = re.compile(r'Tutorial[\s\S]*?html')
    arr = datepat.findall(content)
    res = []
    for i in range(len(arr)):
        tmp_path = arr[i]
        name_with_ext = tmp_path.replace("Tutorial/", "")
        res.append(name_with_ext)
    return res


def do_re(name):
    name_no_ext = name.replace(".html", "")
    path = TutorialPath + u"/" + name

    exit_path = os.path.exists(path)
    if not exit_path:
        raise RuntimeError("没有这个html文件:{}".format(path))


    f = open(path, "r")
    content = f.read()
    f.close()
    # content = content.replace("</a>", "")
    datepat = re.compile(r'{}[\s\S]*?</ul>'.format(EXPORTHTMLH1TAG))
    re_arr = datepat.findall(content)
    for item in re_arr:
        itemStr = str(item)
        # <p> 参考文章:./title_str.html<a href="title_str.html">点击打开</a></p>
        href_str = """<p> 参考文章:./{0}.html<a href="{0}.html">点击打开</a></p>""".format(name_no_ext)
        title_str = "\n\n<h1>{}</h1>\n{}".format(name_no_ext, href_str)
        export_str = itemStr.replace(EXPORTHTMLH1TAG, title_str)
        return export_str
    return None


def do_insert_html(path, insert_content):
    f = open(path, "r")
    content = f.read()
    f.close()

    new_content = "{0}\n\n{1}\n\n</body>".format(HTMLH1TITLE, insert_content)
    htmlTmpContent = re.sub(r'{0}[\s\S]*?</body>'.format(HTMLH1TITLE), new_content, content)

    f = open(path, "w")
    f.write(htmlTmpContent)
    f.flush()
    f.close()


def do_export():
    res_str = ""
    for name in get_all_html():
        content = do_re(name)
        if content == None:
            pass
        else:
            res_str = res_str + content

    path = EXPORT2FILEPATH
    do_insert_html(path, res_str)


# content = do_re("Early_Z.html")


def Check():
    exit_path = os.path.exists(EXPORT2FILEPATH)
    if not exit_path:
        error_str = "不存在路径{}".format(EXPORT2FILEPATH)
        raise RuntimeError(error_str)


Check()
do_export()
print(u"导出完成")
