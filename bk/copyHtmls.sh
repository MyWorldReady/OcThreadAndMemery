#!/bin/bash



#快速复制某个html文件到一系列带数字后缀的新html文件

#for开始的数字
startIdx=1
#for结束的数字
endIdx=70


copyFilePath="$1"
if ! [ -n "${copyFilePath}" ]; then
	echo "操作失败!"
	echo "需要传递拷贝的文件的绝对路径作为第一参数！！！"
	exit
fi

newFileName="$2"
if ! [ -n "${newFileName}" ]; then
	echo "操作失败!"
	echo "需要传递一个文件名作为第二参数！！！"
	exit
fi

if ! [[ -f "$copyFilePath" ]]; then
	echo "操作失败!"
	echo "文件不存在！！！"
	exit
fi


filepath=$(cd "$(dirname "$0")"; pwd)  


dstFolderPath=`dirname $copyFilePath` 
for (( i = "${startIdx}"; i < "${endIdx}"; i++ )); do
	dstPath="${dstFolderPath}"'/'"${newFileName}${i}.html"
	cp "${copyFilePath}" "${dstPath}"
done

echo "操作结束!"