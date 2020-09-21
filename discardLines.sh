#!/bin/bash



#这个脚本是用来删除多行的
#比如，清理从'<main id'到' <content> -->'所在的行
#现在这个脚本写死删除从'<main id'到' <content> -->'所在的行




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

globalRel2(){
	for f in ${fileArr[*]}
	do
		htmlPath="${rootHtmlPath}"'/'"$f"

		#清理从'<main id'到' <content> -->'所在的行
		contailStr=$(grep -n '<main id' $htmlPath)
		contailLen=${#contailStr}
		if [[  "$contailLen" == "0"  ]]; then
			continue
		fi
		startRowNum=$(echo $contailStr | cut -d ":" -f 1)
		endRowNum=$(grep -n ' <content> -->' $htmlPath | cut -d ":" -f 1)
		
		if [[ $os = 1 ]]; then
			sed -i "${startRowNum},${endRowNum}d" $htmlPath
		else
			sed -i "" "${startRowNum},${endRowNum}d" $htmlPath
		fi
	done
}

globalRel2


echo "清理多行完成"
