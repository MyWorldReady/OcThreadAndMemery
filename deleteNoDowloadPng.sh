#!/bin/bash

#此脚本用于删除已经使用脚本下载的图片.
#需要传入一个最大下载名. 如: A_12834_1590901372000043


if [ -z "$1" ]; then
    echo "需要传入一个最大下载名 如  A_12834_1590901372000043"
    echo "已经exit"
    exit
fi



baseStr="$1"
fromIndex=0


# A_12834_1590901372000041

filepath=$(cd "$(dirname "$0")"; pwd)  

baseStrLen=${#baseStr}
newBaseLen=$((${baseStrLen}-2))
newBase=${baseStr:0:$newBaseLen}


newNumberFromIndex=$((${baseStrLen}-2))
newNumber=${baseStr:$newNumberFromIndex:$baseStrLen}

toIndex=$newNumber

if [ $toIndex -le 9 ];
then
	toIndex=${toIndex:1:2}
fi

for (( i = $fromIndex; i <= $toIndex; i++ )); do
	imgName=$newBase
	if [ $i -le 9 ];
	then
		imgName=$imgName'0'$i
	else
	    imgName=$imgName$i
	fi
	fullPngPath=$filepath/img/$imgName
	rm -f $fullPngPath
done


echo "操作完成 删除最大下标是:$toIndex"
