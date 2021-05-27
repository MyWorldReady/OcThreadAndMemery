#!/bin/bash



#此脚本用于重命名一个下载的图片.
#自动寻找png，jpg，jpeg格式的文件进行重命名
#需要放置一个 A_12834_1590901372000043 格式的文件在新图片处理路径下作为起始点的文件名, 如果没有,则从0开始命名
#需要传入新图片处理路径  如 /c/Users/wwl/Downloads/789/



if [ -z "$1" ]; then
    echo "需要传入新图片处理路径 如  /c/Users/wwl/Downloads"
    echo "已经exit"
    exit
fi

if [ -d "$1" ]; then
	echo "新图片保存路径 $1"
else
	echo '新图片保存路径不存在'
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
png2jpgOnePath="${filepath}/_png2jpgOne.py"

if [[ ! -f $png2jpgOnePath ]]; then
	echo "python处理脚本不存在 $png2jpgOnePath"
	exit
fi

finalPicSavingPath=$filepath/img

if [[ ! -d $finalPicSavingPath ]]; then
	echo "最终图片保存路径不存在 $finalPicSavingPath"
	exit
fi



allPicArr=$(ls $handingImgPath | grep -E '\.png|\.JPG|\.JPEG|\.jpg|\.jpeg')
lenghtCheck=0

picName=''
for name in $allPicArr; do
	((lenghtCheck++))
	picName=$name
done

if [[ $lenghtCheck -ne  1 ]]; then
	echo "有且只能有一个图片,现在有${lenghtCheck}个"
	exit
fi

echo "现有图片文件  $picName"



arr=$(ls $handingImgPath| grep 'A_')

baseStr=''
lenghtCheck=0
for name in $arr; do
	((lenghtCheck++))
	baseStr=$name
done

if [[ $lenghtCheck -le  0 ]]; then
	currentTimeStamp=$(($(date +%s)*1000000))
	randomInt=$RANDOM
	baseStr='A_'${randomInt}'_'${currentTimeStamp}
else
	if [[ $lenghtCheck -ne  1 ]]; then
		echo "只有有一个文件作为参考起点,现在有${lenghtCheck}个"
		exit
	fi
fi



echo "参考图片文件名  $baseStr"



baseStrLen=${#baseStr}
newBaseLen=$((${baseStrLen}-2))
newBase=${baseStr:0:$newBaseLen}


newNumberFromIndex=$((${baseStrLen}-2))
newNumber=${baseStr:$newNumberFromIndex:2}


newImgName=$newBase

if [[ $newNumber == 0* ]]; then 
	handingImgPath=$1
	newNumber=${newNumber:1:1}
fi


toIndex=$newNumber
((toIndex++))

if [ $toIndex -le 9 ];
then
	newImgName=$newImgName'0'$toIndex
else
    newImgName=$newImgName$toIndex
fi

echo "新生成图片文件名 $newImgName"


newImgFullPath=$handingImgPath/$newImgName
mv $handingImgPath/$picName $newImgFullPath

# 使用python脚本处理图片
python "${png2jpgOnePath}" "${newImgFullPath}"


cp $handingImgPath/$newImgName $finalPicSavingPath/$newImgName
#删除老文件
rm -f $handingImgPath/$baseStr





echo '检查完成'

echo ''
echo ''
echo '已经复制以下内容到剪切板'

copyToClipboardStr="<img src=\"../img/$newImgName\">"
echo $copyToClipboardStr

tmpFilePath="$handingImgPath/tmp.txt"
echo $copyToClipboardStr>$tmpFilePath

if [[ $os = 1 ]]; then
	clip < $tmpFilePath
else
	pbcopy <  $tmpFilePath
fi

