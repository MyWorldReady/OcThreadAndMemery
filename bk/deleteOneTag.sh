#!/bin/bash


#这个脚本是用来删除某一对标签的
#比如，删除 <span class="sxs-lookup".....> </span> 包裹的内容
#现在这个脚本写死删除<span class="sxs-lookup".....> </span>



#系统类型  0:mac 1:win 2linux
os=1
if [ "$(uname)" == "Darwin" ]
then
	os=0
fi






filepath=$(cd "$(dirname "$0")"; pwd)  
htmlPath=$filepath/qqq.html



rootHtmlPath="${filepath}/Tutorial"


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
		echo "$f 正在清理标签"
		curCnt=0
		while [[ 1==1 ]]; do
			#在这里修改删除的标签对，
			oldStr=$(grep -oi -m 1 -P '<span class="sxs-lookup"([!]|[^!])*?</span>' ${htmlPath} | head -n1)
			newStr=""
			if [[ -z $oldStr ]]; then
				break;
			fi
			sed -i "s~${oldStr}~${newStr}~g" ${htmlPath}
			((curCnt++))
			if [[ $curCnt -gt 15 ]]; then
				echo 'sed替换超过15次未完成'
			fi

		done
		# sed -i 's~<span class="sxs-lookup">[^/]*span>~~g'  ${htmlPath}
	done
}

globalRel2





echo "清理标签所有操作执行完成"