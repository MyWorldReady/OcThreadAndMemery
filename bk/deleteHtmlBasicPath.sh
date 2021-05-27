#!/bin/bash


#快速替换html文件路径下包含Basis



filepath=$(cd "$(dirname "$0")"; pwd)  

rootHtmlPath="${filepath}/Tutorial"


#TDOO文件名包含空格未处理 只处理了包看 "副本" 字眼的文件
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

fileArr=()
for f in $(ls $rootHtmlPath)
do
	fullPath="${rootHtmlPath}"'/'"$f"
	if  [[ "$f" != *副本* ]] && [  -f "$fullPath"  ]
	then
		len=${#fileArr[@]}
		fileArr[$len]="$f"
	fi
done


IFS=$SAVEIFS


#拷贝html文件
for f in ${fileArr[*]}
do
	fullPath="${rootHtmlPath}"'/'"$f"
	oldStr='../../'
	newStr='../'
	sed -i "s#${oldStr}#${newStr}#g" ${fullPath}
done


#处理sidebar.html
# sidebarPath=${menusRoot}'/sidebar.html'
# menusOldStr='Tutorial/Basis'
# menusNewStr='Tutorial'
# sed -i "s#${menusOldStr}#${menusNewStr}#g" ${sidebarPath}

echo "处理完成"