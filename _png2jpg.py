# encoding:utf-8

#!/usr/bin/python

#需要传递的参数:待处理文件夹路径,被处理后文件保存文件夹路径

import os,shutil
import sys
from PIL import Image

len_argv = len(sys.argv)
if len_argv !=3:
	print("需要并且需要待处理文件夹路径,被处理后文件保存文件夹路径")
	sys.exit(0)

handler_path = str(sys.argv[1])
saving_path = str(sys.argv[2])

if not handler_path.endswith('/'):
    handler_path= handler_path + "/"
        
if not saving_path.endswith('/'):
    saving_path= saving_path + "/"   


if not os.path.exists(handler_path):
	print("待处理文件夹路径不存在 handler_path="+handler_path)
	sys.exit(0)

if not os.path.exists(saving_path):
    print("被处理后文件保存文件夹路径不存在 saving_path="+saving_path)
    sys.exit(0)



def PNG_JPG(PngPath,outPutFolder):
    img = Image.open(PngPath)
    w = img.width
    h = img.height

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
        os.rename(outfile,outfileNoExt)
        shutil.move(outfileNoExt,outPutFolder)
        os.remove(PngPath)
        return outfile
    except Exception as e:
    	print("PNG转换JPG 错误", e)





path_root = os.getcwd()
# before_path = path_root + '/before/'
# after_path = path_root + '/after/'
before_path = handler_path
after_path = saving_path

if not os.path.exists(before_path):
	print("需要处理的文件放在before文件夹")
	sys.exit(0)

#重新创建after_path
# shutil.rmtree(after_path)
# os.makedirs(after_path)
	
handlerLen = 0;

Path=before_path
img_dir = os.listdir(Path)
for img in img_dir:
    if img.lower().endswith('.png'):
        handlerLen = handlerLen + 1
        PngPath= Path + img
        PNG_JPG(PngPath,after_path)

img_dir = os.listdir(Path)
for img in img_dir:
    if img.startswith('A_'):
        handlerLen = handlerLen + 1
        PngPath= Path + img
        oldPngPath = PngPath
        newPngPath = PngPath + ".png"
        os.rename(oldPngPath,newPngPath)
        PNG_JPG(newPngPath,after_path)


if handlerLen == 0:
    print("一个文件也没有处理到!!!!")
    print("自动寻找.png后缀，A_开头 格式的文件进行处理: 转jpg,调整尺寸")
    pass