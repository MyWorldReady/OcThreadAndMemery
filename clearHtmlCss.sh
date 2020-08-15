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


		htmlContent=$(cat ${htmlPath})
		if [[ $htmlContent == *${hasFlushHtmlMark}*  ]]
		then
			continue
		fi

		#p
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<p [^>]+>' ${htmlPath} | head -n1)
			newStr='<p>'
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#^
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<div [^>]+>' ${htmlPath} | head -n1)
			newStr="<div>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#span
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<span [^>]+>' ${htmlPath} | head -n1)

			newStr="<span>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done
		
		#a
		# while [[ 1==1 ]]; do
		# 	oldStr=$(grep -a -Eoi -m 1 '<a [^>]+>' ${htmlPath} | head -n1)

		# 	newStr="<a>"
		# 	if [[ -z $oldStr ]]; then
		# 		break;
		# 	fi
		# 	if [[ $os = 1 ]]; then
		# 		sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		# 	else
		# 		sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		# 	fi
		# done

		#strong
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<strong [^>]+>' ${htmlPath} | head -n1)
			newStr="<strong>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#div
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<div [^>]+>' ${htmlPath} | head -n1)
			newStr="<div>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#br
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<br [^>]+>' ${htmlPath} | head -n1)
			newStr='<br>'
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#pre
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<pre [^>]+>' ${htmlPath} | head -n1)
			newStr="<pre>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#code
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<code [^>]+>' ${htmlPath} | head -n1)
			newStr="<code>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#table
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<table [^>]+>' ${htmlPath} | head -n1)
			newStr="<table>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#tbody
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<tbody [^>]+>' ${htmlPath} | head -n1)
			newStr="<tbody>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#tr
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<tr [^>]+>' ${htmlPath} | head -n1)
			newStr="<tr>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#td
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<td [^>]+>' ${htmlPath} | head -n1)
			newStr="<td>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#font
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<font [^>]+>' ${htmlPath} | head -n1)
			newStr="<font>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#h1
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<h1 [^>]+>' ${htmlPath} | head -n1)
			newStr="<h1>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#h2
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<h2 [^>]+>' ${htmlPath} | head -n1)
			newStr="<h2>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#h3
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<h3 [^>]+>' ${htmlPath} | head -n1)
			newStr="<h3>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#h4
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<h4 [^>]+>' ${htmlPath} | head -n1)
			newStr="<h4>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#h5
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<h5 [^>]+>' ${htmlPath} | head -n1)
			newStr="<h5>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#li
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<li [^>]+>' ${htmlPath} | head -n1)
			newStr="<li>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#ul
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<ul [^>]+>' ${htmlPath} | head -n1)
			newStr="<ul>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#ol
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<ol [^>]+>' ${htmlPath} | head -n1)
			newStr="<ol>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#article
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<article [^>]+>' ${htmlPath} | head -n1)
			newStr="<article>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#button
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<button [^>]+>' ${htmlPath} | head -n1)
			newStr="<button>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#blockquote
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<blockquote [^>]+>' ${htmlPath} | head -n1)
			newStr="<blockquote>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#i
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<i [^>]+>' ${htmlPath} | head -n1)
			newStr="<i>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#path
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<path [^>]+>' ${htmlPath} | head -n1)
			newStr="<path>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#svg
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<svg [^>]+>' ${htmlPath} | head -n1)
			newStr="<svg>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#figure
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<figure [^>]+>' ${htmlPath} | head -n1)
			newStr="<figure>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#ins
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<ins [^>]+>' ${htmlPath} | head -n1)
			newStr="<ins>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#section
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<section [^>]+>' ${htmlPath} | head -n1)
			newStr="<section>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		#em
		while [[ 1==1 ]]; do
			oldStr=$(grep -a -Eoi -m 1 '<em [^>]+>' ${htmlPath} | head -n1)
			newStr="<em>"
			if [[ -z $oldStr ]]; then
				break;
			fi
			if [[ $os = 1 ]]; then
				sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
			else
				sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
			fi
		done

		###########################################################

		oldStr='<span>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='</span>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		# oldStr='<a>'
		# newStr=""
		# if [[ $os = 1 ]]; then
		# 	sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		# else
		# 	sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		# fi

		# oldStr='</a>'
		# newStr=""
		# if [[ $os = 1 ]]; then
		# 	sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		# else
		# 	sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		# fi



		##########删除li ul ol   --start
		oldStr='</li>'
newStr='\
</li>'
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='</li>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='<li>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='<ul>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='</ul>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='<ol>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='</ol>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi
		##########删除li ul ol   --end

		oldStr='<code>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='</code>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='<div>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='</div>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='<article>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='</article>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='data-original-src'
		newStr="src"
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='<button>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='</button>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='<i>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='</i>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='<svg>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='</svg>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='<path>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='</path>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='<figure>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='</figure>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='<hr>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		#对句号换行进行整理 --start
		oldStr='。'
		newStr="<br>"
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi
		oldStr='<br><br>'
		newStr="<br>"
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		#br换行显示
		oldStr='<br>'
		newStr='<br>\
'
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		#对换行进行整理 --end


		#p换行显示
		oldStr='<p>'
		newStr='\
<p>'
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='</p>'
		newStr='</p>\
'
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='<ins>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='</ins>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='<blockquote>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='</blockquote>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi


		oldStr='<section>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='</section>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi


		oldStr='<em>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='</em>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='<font>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi

		oldStr='</font>'
		newStr=""
		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i "" "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi


		htmlContent=$(cat ${htmlPath})
		newContent=$hasFlushHtmlMark$htmlContent
		echo "${newContent}" > $htmlPath

	done
}
globalRel2


echo "清理html的标签的css完成"