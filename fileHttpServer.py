# -*- encoding: utf-8 -*-


import sys
import os
import re
import shutil
import requests
import json

from flask import Flask, send_file, make_response, request


reload(sys)
sys.setdefaultencoding('utf-8')
# sys.path.append('/Users/wu/Library/Python/2.7')

# from flask import Flask, request, render_template




def IsMac():
    p = sys.platform
    return p == "darwin"

def IsWin():
    p = sys.platform
    return p == "win32"


if IsWin():
    os.system('chcp 65001')

path_root = os.getcwd().replace("\\","/")

IP = "0.0.0.0"
PORT = 8080

RSPTYPEKEY = "RSPTYPEKEY"


from flask import Flask
app = Flask(__name__)

def check_can_return(path):
    can_return = True
    if ".git" in path:
        can_return = False
    elif ".py" in path:
        can_return = False
    elif ".DS_Store" in path:
        can_return = False
    elif ".sh" in path:
        can_return = False
    elif ".py" in path:
        can_return = False
    elif ".git" in path:
        can_return = False
    elif "package" in path:
        can_return = False

    return can_return

@app.route('/')
def hello_world():
    # return 'Hello World flask'
    # return send_file("/Cooking/index.html")



    return '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    <title>The Frameset Boilerplate: Mainframe</title>
    
    
    <style type="text/css">
body {font-size:300%;}
</style>
    
    
    
    
    
    
</head>
<body style="font-family:sans-serif">
    

<h1>123</h1>

<p>qqqqq</p>



    
</body>
</html>
  
    
'''

def getAll(path):
    Dirlist = []
    Filelist = []
    Relativelist = []
    for home, dirs, files in os.walk(path):
        # 获得所有文件夹
        for dirname in dirs:
            can_return = check_can_return(dirname)
            if can_return:
                Dirlist.append(os.path.join(home, dirname))
        # 获得所有文件
        for filename in files:
            full_path = os.path.join(home, filename).replace("\\","/")
            can_return = check_can_return(full_path)
            if can_return:

                Filelist.append(full_path)
                relative_path = full_path.replace(path_root,"")
                if relative_path.startswith("/"):
                    relative_path = relative_path[1:]
                Relativelist.append(relative_path)
    return Dirlist, Filelist, Relativelist  # 返回所有文件夹列表和文件列表[dirlist, filelist, Relativelist]


@app.route('/list_root', methods=['GET', 'POST'])
def list_root():

    path_arr = []
    files = os.listdir(path_root)
    # files = os.listdir(unicode(path_root, "utf-8"))
    for f in files:
        full_path = os.path.join(path_root, f)
        if os.path.isdir(full_path):
            relativePath = "/" + f
            path_arr.append(relativePath)


    JsonStr = json.dumps(path_arr, ensure_ascii=False, encoding='UTF-8')
    return JsonStr

@app.route('/list_path', methods=['GET', 'POST'])
def list_path():
    relativePath = request.form.get("relativePath", type=str, default=None)
    #todo joker
    # relativePath = "/Cooking"
    print "relativePath="+relativePath
    full_path = path_root + relativePath
    resultArr = getAll(full_path)
    fileArr = resultArr[2]
    JsonStr = json.dumps(fileArr, ensure_ascii=False, encoding='UTF-8')
    return JsonStr


# @app.route('/list_path', methods=['GET', 'POST'])
# def list_path():
#     fileArr = []
#     fileArr.append("Cooking/frames/main.html")
#     JsonStr = json.dumps(fileArr, ensure_ascii=False, encoding='UTF-8')
#     return JsonStr

@app.route('/get_file', methods=['GET', 'POST'])
def get_file():
    # return 'hello world 钓鱼岛是中国的！！！ test_cal_by_path'
    # return send_file()
    # file = Path(__file__).parent
    # print file

    # return send_file("11.jpg")
    # return send_file("你好.jpg")
    # return send_file("常用快捷键.html")

    # file_path = '/Users/wu/Downloads/123/常用快捷键.html'
    # f = open(file_path,'rb+')
    # rb = f.read()
    # f.close()
    #
    # testParm = request.form.get("testParm", type=str, default=None)
    # print "testParm====---"
    # print testParm
    #

    relativePath = request.form.get("relativePath", type=str, default=None)
    file_path = path_root+"/"+relativePath
    f = open(file_path,'rb+')
    rb = f.read()
    f.close()

    response = make_response(rb)
    response.headers['Content-Type'] = 'application/octet-stream'
    response.headers['qqjokerqq'] = "1"
    return response


# @app.route('/Cooking', methods=['GET', 'POST'])
# def get_file():
#     return send_file("/Cooking/index.html")



if __name__ == '__main__':
    app.run(IP,PORT,True)

