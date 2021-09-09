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


def do_re(name):
    path = TutorialPath + "/" + name
    f = open(path, "r")
    content = f.read()
    f.close()
    # content = re.sub(r'<a href="http://www.52im[\s\S]*?</a>', "", content)
    # content = content.replace("</a>", "")
    content = content.replace("""<img src="../images/""", """<img src="https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@11.0/manual/images/""")
    content = content.replace("""<img src="images/""", """<img src="https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@11.0/manual/images/""")
    content = content.replace("""<img src="images\\""", """<img src="https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@11.0/manual/images/""")
    content = content.replace("""<img src="/Images/""", """<img src="https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@11.0/manual/images/""")
    f = open(path, "w")
    f.write(content)
    f.flush()
    f.close()


for name in get_all_html():
    do_re(name)

# do_re("如何查询一组文件夹中的总字节数.html")
