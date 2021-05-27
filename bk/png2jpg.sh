#!/bin/bash

#此脚本用于将图片是从png转为jpg并且调整尺寸, 将所有图片都调整尺寸.
#注意:回自动删除所有图片文件的后缀
#自动寻找.png后缀，A_开头 格式的文件进行处理: 转jpg,调整尺寸
#需要传入新图片处理路径  如 /c/Users/wwl/Downloads/789/


#需要配置python2 或者 python3
#需要为python安装Image库


if [ -z "$1" ]; then
    echo "需要传入新图片处理路径 如  /c/Users/wwl/Downloads"
    echo "已经exit"
    exit
fi

if [ -d "$1" ]; then
	echo "待处理文件夹路径 $1"
else
	echo '待处理文件夹路径不存在'
	exit
fi


#系统类型  0:mac 1:win 2linux
os=1
if [ "$(uname)" == "Darwin" ]
then
	os=0
fi



handingImgPath=''
if [[ $1 == */ ]]; then 
	handingImgPath=$1
else 
	handingImgPath=$1'/'
fi


filepath=$(cd "$(dirname "$0")"; pwd)  


finalPicSavingPath=$filepath/img

if [ ! -d "$finalPicSavingPath" ]; then
	echo '待处理文件夹路径不存在 finalPicSavingPath='$finalPicSavingPath
	echo "这个路径是自己工程的img目录,如果没有,请查找原因"
	exit
fi

python _png2jpg.py $handingImgPath $finalPicSavingPath