#!/bin/bash


#已经处理过的html文件的标记
hasFlushHtmlMark="<!--clear--clear--clear-->"

#系统类型  0:mac 1:win 2linux
os=1
if [ "$(uname)" == "Darwin" ]
then
	os=0
fi

filepath=$(cd "$(dirname "$0")"; pwd)  

rootHtmlPath="${filepath}/Tutorial"


#遍历全部的html后缀文件
#只处理了包看 "副本" 字眼的文件
# SAVEIFS=$IFS
# if [ $os = 1 ]
# then
# 	IFS=$(echo -en "\n\b")
# fi

# fileArr=()
# for f in $(ls $rootHtmlPath)
# do
# 	fullPath="${rootHtmlPath}"'/'"$f"
# 	if  [[ "$f" != *副本* ]] && [  -f "$fullPath"  ]
# 	then
# 		len=${#fileArr[@]}
# 		fileArr[$len]="$f"
# 	fi
# done


# if [ $os = 1 ]
# then
# 	IFS=$SAVEIFS
# fi



#需要处理的文件优化成使用git
fileArr=()
modifyArr=$(git status -s | grep -a -Eoi 'Tutorial/.*html')
for f in ${modifyArr}
do
	fullPath="${filepath}/$f"
	if  [[ "$f" != *副本* ]] && [  -e "$fullPath"  ]
	then
		name=${f:9} #删除Tutorial/  得到带后缀的文件名
		len=${#fileArr[@]}
		fileArr[$len]="$name"
	fi
done



#直接删除标签
#如传入li  则直接删除<li>和</li>
function DeleteTag(){
	oldStr=$1
	if [[ $os = 1 ]]; then
		sed -i -e "s~<${oldStr} [^>]*>~~g" -e "s~<${oldStr}>~~g"  -e "s~</${oldStr}>~~g"  ${htmlPath}
	else
		sed -i "" -e "s~<${oldStr} [^>]*>~~g" -e "s~<${oldStr}>~~g" -e "s~</${oldStr}>~~g"  ${htmlPath}
	fi
}

#精简标签
#如传入li  则精简<li .....>为<li>
function SimpleTag(){
	oldStr=$1
	if [[ $os = 1 ]]; then
		sed -i "s~<${oldStr} [^>]*>~<${oldStr}>~g"  ${htmlPath}
	else
		sed -i "" "s~<${oldStr} [^>]*>~<${oldStr}>~g"  ${htmlPath}
	fi
}

function TagStartNewLine(){
	oldStr=$1
	TagReplace "$oldStr" '\
'"${oldStr}"
}

function TagEndNewLine(){
	oldStr=$1
	TagReplace "$oldStr" "${oldStr}"'\
'
}

function TagReplace(){
	oldStr=$1
	newStr=$2
	if [[ -z $oldStr ]]; then
		echo '字符串替换第一个参数错误'
		exit;
	fi 
	if [[ -z $newStr ]]; then
		echo '字符串替换第二个参数错误'
		exit;
	fi 
	if [[ $os = 1 ]]; then
		sed -i "s~${oldStr}~${newStr}~g"  ${htmlPath}
	else
		sed -i "" "s~${oldStr}~${newStr}~g"  ${htmlPath}
	fi
}


globalRel2(){
	for f in ${fileArr[*]}
	do
		htmlPath="${rootHtmlPath}"'/'"$f"


		htmlContent=$(cat ${htmlPath})
		if [[ $htmlContent == *${hasFlushHtmlMark}*  ]]
		then
			continue
		fi


		SimpleTag 'p'
		SimpleTag 'strong'
		SimpleTag 'br'
		SimpleTag 'pre'
		SimpleTag 'table'
		SimpleTag 'tbody'
		SimpleTag 'tr'
		SimpleTag 'td'
		SimpleTag 'h1'
		SimpleTag 'h2'
		SimpleTag 'h3'
		SimpleTag 'h4'
		SimpleTag 'h5'


		DeleteTag 'div'
		DeleteTag 'span'
		DeleteTag 'code'
		DeleteTag 'font'
		DeleteTag 'li'
		DeleteTag 'ul'
		DeleteTag 'ol'
		DeleteTag 'article'
		DeleteTag 'button'
		DeleteTag 'blockquote'
		DeleteTag 'i'
		DeleteTag 'path'
		DeleteTag 'svg'
		DeleteTag 'figure'
		DeleteTag 'ins'
		DeleteTag 'section'
		DeleteTag 'em'
		DeleteTag 'ignore_js_op'
		DeleteTag 'span'
		DeleteTag 'data-original-src'
		DeleteTag 'hr'
		DeleteTag 'b'

		TagStartNewLine '<p>'
		TagEndNewLine '</p>'

		TagReplace '。' '\
''<br><br>''\
''\
'

	
		htmlContent=$(cat ${htmlPath})
		newContent=$hasFlushHtmlMark$htmlContent
		echo "${newContent}" > $htmlPath

	done
}
globalRel2


echo "清理html的标签的css完成"