#!/bin/bash


#快速替换html文件路径下包含Basis

#系统类型  0:mac 1:win 2linux
os=1
if [ "$(uname)" == "Darwin" ]
then
	os=0
fi

filepath=$(cd "$(dirname "$0")"; pwd)  

rootHtmlPath="${filepath}/Tutorial"


#TDOO文件名包含空格未处理 只处理了包看 "副本" 字眼的文件
SAVEIFS=$IFS
if [ $os = 1 ]
then
	IFS=$(echo -en "\n\b")
fi

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


if [ $os = 1 ]
then
	IFS=$SAVEIFS
fi



#拷贝html文件
for f in ${fileArr[*]}
do
	fullPath="${rootHtmlPath}"'/'"$f"
	oldStr='rnrnrnrnrn'
	newStr="<!--   QQQQQQQQQQQQQ  -->"
	sed -i "" "s#${oldStr}#${newStr}#g" ${fullPath}


	oldStr='rnrnrn'
	newStr="<!--   FFFFFFFFFF  -->"
	sed -i "" "s#${oldStr}#${newStr}#g" ${fullPath}

	oldStr='rnrn'
	newStr="<!--   ${oldStr}  -->"
	sed -i "" "s#${oldStr}#${newStr}#g" ${fullPath}


	oldStr='QQQQQQQQQQQQQ'
	newStr='rnrnrnrnrn'
	sed -i "" "s#${oldStr}#${newStr}#g" ${fullPath}


	oldStr='FFFFFFFFFF'
	newStr='rnrnrn'
	sed -i "" "s#${oldStr}#${newStr}#g" ${fullPath}

done






#处理sidebar.html
# sidebarPath=${menusRoot}'/sidebar.html'
# menusOldStr='Tutorial/Basis'
# menusNewStr='Tutorial'
# sed -i "s#${menusOldStr}#${menusNewStr}#g" ${sidebarPath}

echo "处理完成"