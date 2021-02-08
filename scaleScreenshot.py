# encoding:utf-8

#!/usr/bin/python

#此脚本一般用于mac截图太大的处理
#需要传递的参数:自动将当前路径下的Screenshot.jpg同比缩小2倍 , 
#并清空iosScreenshot文件夹
#并将缩小后的Screenshot.jpg移动到iosScreenshot文件夹

import os,shutil
import sys
from PIL import Image


handler_Name = 'Screenshot.jpg'
handler_FilePath = os.getcwd()+ "/"+handler_Name
saving_path = os.getcwd()+ "/"+"iosScreenshot"

if not os.path.exists(handler_FilePath):
    print(handler_Name+" 文件不存在!!!!")
    sys.exit(0)


def PNG_JPG(PngPath,outPutFolder):
    img = Image.open(PngPath)
    w = img.width
    h = img.height

    if w==0:
        return
    if h==0:
        return
            


    infile = PngPath
    outfileNoExt = os.path.splitext(infile)[0] + ""
    outfile = outfileNoExt + ".jpg"
    img = Image.open(infile)
    outW = w/2
    outH = h/2
    img = img.resize((outW, outH), Image.ANTIALIAS)
    try:
        if len(img.split()) == 4:
            # prevent IOError: cannot write mode RGBA as BMP
            r, g, b, a = img.split()
            img = Image.merge("RGB", (r, g, b))
            img.convert('RGB').save(outfile, quality=70)           
        else:
            img.convert('RGB').save(outfile, quality=70)
        shutil.move(outfile,outPutFolder)
        # os.remove(PngPath)
        print("同比缩小2倍处理完成")
        return outfile
    except Exception as e:
    	print("PNG转换JPG 错误", e)





path_root = os.getcwd()
after_path = saving_path


# 重新创建after_path
shutil.rmtree(after_path)
os.makedirs(after_path)
	
PNG_JPG(handler_FilePath,after_path)

