# -*- encoding: utf-8 -*-


import sys

import os
import re
from googletrans import Translator

path_root = os.getcwd()

TutorialPath = path_root + "/Tutorial"


def get_all_html():
    res = []
    arr = os.listdir(TutorialPath)
    for name in arr:
        if name.endswith(".html"):
            # res.append(name.decode("utf-8"))
            res.append(name)
    return res


def do_google_translate(ori_str):
    translator = Translator()
    trans = translator.translate(ori_str, src='en', dest='zh-cn')
    # 原文
    # print(trans.origin)
    # 译文
    str = trans.text
    return str


def do_one(name):
    print("正在处理  {}".format(name))
    path = TutorialPath + "/" + name
    f = open(path, "r", encoding='utf-8')
    ori_content = f.read()
    f.close()
    body_tag_begin = '<body style="font-family:sans-serif">'
    body_tag_end = '</body>'
    arr = re.findall(r'{}[\s\S]*?{}'.format(body_tag_begin, body_tag_end), ori_content)
    res_len = len(arr)
    if res_len != 1:
        raise RuntimeError("没有标签:{}...{}".format(body_tag_begin, body_tag_end))
    body_str = str(arr[0])
    no_body_str = body_str.replace(body_tag_begin, "").replace(body_tag_end, "")
    insert_mark = "<!--translate--translate--translate-->"
    html_frame_body = ori_content.replace(no_body_str, "\n\n\n\n\n" + insert_mark + "\n\n\n\n\n")

    translate_res = do_google_translate(no_body_str)
    result_str = html_frame_body.replace(insert_mark,translate_res)
    f = open(path, "w", encoding='utf-8')
    f.write(result_str)
    f.flush()
    f.close()


for name in get_all_html():
    do_one(name)

# do_re("如何查询一组文件夹中的总字节数.html")
