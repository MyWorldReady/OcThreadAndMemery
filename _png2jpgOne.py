# encoding:utf-8

#!/usr/bin/python

#处理一张图片 转jpg,调整尺寸
#需要传递的参数:待处理文件路径

import os,shutil
import sys
from PIL import Image

len_argv = len(sys.argv)
if len_argv != 2:
	print("需要并且需要待处理文件路径")
	sys.exit(0)

handler_path = str(sys.argv[1])


if not os.path.exists(handler_path):
	print("待处理文件夹路径不存在 handler_path="+handler_path)
	sys.exit(0)

def PNG_JPG(PngPath):
    fp = open(PngPath,'rb')
    img = Image.open(fp)
    w = img.width
    h = img.height
    infile = PngPath
    outfileNoExt = os.path.splitext(infile)[0] + ""
    outfile = outfileNoExt + ".jpg"
    img = Image.open(infile)
    
    outW = w
    outH = h

    if w==0:
        return
    if h==0:
        return



    if outW>outH:
        if outW > 650:
            outW = 650
            ratio = float(outW) / w
            outH = int(h*ratio)
    else:
        if outH > 650:
            outH = 650
            ratio = float(outH) / h
            outW = int(width*ratio)
            
    
    img = img.resize((outW, outH), Image.ANTIALIAS)
    try:
        if len(img.split()) == 4:
            # prevent IOError: cannot write mode RGBA as BMP
            r, g, b, a = img.split()
            img = Image.merge("RGB", (r, g, b))
            img.convert('RGB').save(outfile, quality=70)           
        else:
            img.convert('RGB').save(outfile, quality=70)

    except Exception as e:
    	print("PNG转换JPG 错误", e)

    fp.close()
    os.remove(PngPath)
    os.rename(outfile,outfileNoExt)


PNG_JPG(handler_path)

