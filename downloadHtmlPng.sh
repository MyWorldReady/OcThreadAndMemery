#!/bin/bash

#TDOO文件名包含空格未处理 只处理了包看 "副本" 字眼的文件

#html文件返回到img目录路径
html2ImgPath="../img/"
#已经处理过的html文件的标记
hasFlushHtmlMark="../img/"


#系统类型  0:mac 1:win 2linux
os=1
if [ "$(uname)" == "Darwin" ]
then
	os=0
fi


shellParm1="$1"
shellParm1Exit=0
if [ -n "$1" ]; then
    shellParm1Exit=1
    #去掉最后的/ 如果有
    if [[ $shellParm1 == */ ]]; then
    	shellParm1=${shellParm1%/*}
    fi
fi



filepath=$(cd "$(dirname "$0")"; pwd)  

# 清理一次文件夹
# rm -rf img
# mkdir img
png2jpgOnePath="${filepath}/_png2jpgOne.py"
imgPath="${filepath}/img"
rootHtmlPath="${filepath}/Tutorial"





#清理成对标签
#比如这些标签包含了重复的图片下载地址, 需要清理掉
function ClearTags(){


	htmlFileName=$1
	if  ! [ $htmlFileName  ] 
	then
		echo "没有放html文件!! 结束shell"
		exit
	fi


	htmlPath="${rootHtmlPath}/${htmlFileName}"

	


	#<noscript></noscript>
	while [[ 1==1 ]]; do
		oldStr=$(grep -a -Eoi -m 1 '<noscript([!]|[^!])+?</noscript>' ${htmlPath} | head -n1)
		newStr=''
		if [[ -z $oldStr ]]; then
			break;
		fi


		if [[ $os = 1 ]]; then
			sed -i "s^${oldStr}^${newStr}^g" ${htmlPath}
		else
			sed -i '' "s^${oldStr}^${newStr}^g" ${htmlPath}
		fi
		
		

	done

}




 #下载png
 #刷新html文件
function Download(){


	htmlFileName=$1
	if  ! [ $htmlFileName  ] 
	then
		echo "没有放html文件!! 结束shell"
		exit
	fi


	htmlPath="${rootHtmlPath}/${htmlFileName}"

	strSearchHttp="<img.*src.*"

	contailStr=$(grep ${hasFlushHtmlMark} ${htmlPath})
	
	contailLen=${#contailStr}

	if [[ "$contailLen" != "0" ]]
	then
		# echo "已经处理过了 ${htmlPath}"
		return
	fi



	currentTimeStamp=$(($(date +%s)*1000000))


	randomInt=$RANDOM


	htmlContent=$(cat ${htmlPath})


	


	echo "${htmlFileName}  正在下载img, 请稍后"

	htmlOriContent=$(cat ${htmlPath})

	#下载<img标签之后第一个匹配的图片链接, 否则直到再次匹配之前都不下载
	isAfterImgTag=0
	for imgHttpEx in `grep "${strSearchHttp}" ${htmlPath}`
	do
		url=${imgHttpEx}

		mustContainStr='<img'
	
		if [[ $url == *$mustContainStr* ]]
		then
			isAfterImgTag=1
		else
			if [[ $isAfterImgTag == 0 ]]; then
				continue
			fi
		fi
		
		#提取包含src字段的超链接
		if [[ $url = src* ]] || [[ $url = data-src* ]] || [[ $url = data-original-src* ]]
	 	then
			url=${url#*\"}
			url=${url%\"*}
		else
			continue
		fi
		

		((currentTimeStamp++))
		imgNewName='A_'${randomInt}'_'${currentTimeStamp}

		if [  -f $imgNewName  ]
		then
			echo "img命名冲突,无法下载img文件!!! 结束下载!!"
			return
		fi

		
		newImgPath=${html2ImgPath}$imgNewName
		oldStr=$url
		newStr=$newImgPath
		if [[ $os = 1 ]]; then
			sed -i "s#${oldStr}#${newStr}#g" ${htmlPath}
		else
			sed -i "" "s#${oldStr}#${newStr}#g" ${htmlPath}
		fi


		httpUrl=$url

		if [[ $httpUrl = //* ]]; then
			
			if [ $shellParm1Exit == 1 ]; then
				potocal=${shellParm1%:*}
			    httpUrl="${potocal}:${url}"
			else
				echo "$htmlContent" > "${htmlPath}"
				echo "还原了html文件 ${htmlPath}"
				echo "错误！！"
				echo '想要传入完整的域名部分(不能有引号) 如 https://www.baidu.com'
				echo "结束进程！ 请用git还原下载的图片！"
				exit
			fi
		elif [[ $httpUrl = /* ]]; then
			if [ $shellParm1Exit == 1 ]; then
			    httpUrl="${shellParm1}${url}"
			else
				echo "$htmlContent" > "${htmlPath}"
				echo "还原了html文件 ${htmlPath}"
				echo "错误！！"
				echo '想要传入完整的域名部分(不能有引号) 如 https://www.baidu.com'
				echo "结束进程！ 请用git还原下载的图片！"
				exit
			fi
		else
			if ! [[ $httpUrl = http* ]]; then

				if [ $shellParm1Exit == 1 ]; then
					if [[ $httpUrl = ../* ]]; then
						len=${#httpUrl}-3
						httpUrl=${httpUrl:3:len}
					fi
					httpUrl="${shellParm1}/${httpUrl}"
				else
					echo "$htmlContent" > "${htmlPath}"
					echo "还原了html文件 ${htmlPath}"
					echo "错误！！"
					echo '想要传入完整的域名部分(不能有引号) 如 https://www.baidu.com'
					echo "结束进程！ 请用git还原下载的图片！"
					exit
				fi
				
			fi
		fi
		echo "----------------------------------------------------------------------------------------"
		echo $httpUrl
		

		# wget -O $imgNewName $url -q
		wget -O $imgNewName $httpUrl

		#使用python脚本处理图片
		python "${png2jpgOnePath}" "${imgNewName}"

		isAfterImgTag=0

	done


	# exit


	#写入html文件



	htmlContent=$(cat ${htmlPath})
	htmlContent="<!--${hasFlushHtmlMark}-->$htmlContent"
	echo "$htmlContent" > "${htmlPath}"

	if [[ $os = 1 ]]; then
		sed -i  "s/<pre/<!--\r\n\r\n\r\n\r\n\r\n--> <!-- 代码 --><!--\r\n\r\n--> <pre/g" ${htmlPath}
		sed -i  "s/<\/pre>/<\/pre><!--\r\n\r\n\r\n-->/g" ${htmlPath}
	else
		sed -i "" "s/<pre/<!--\r\n\r\n\r\n\r\n\r\n--> <!-- 代码 --><!--\r\n\r\n--> <pre/g" ${htmlPath}
		sed -i "" "s/<\/pre>/<\/pre><!--\r\n\r\n\r\n-->/g" ${htmlPath}
	fi

	
	

}




#echo "${htmlPath}"
if ! [ -d ${rootHtmlPath} ]; then
  echo "请在当前位置创建一个名为html的文件夹, 并将html脚本放到 html 文件夹内!  结束shell";
  exit
fi


cd img  



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




for f in ${fileArr[*]}
do
	ClearTags $f
	Download $f
done


#清理html的标签的css
sh ${filepath}''"/clearHtmlCss.sh"

echo "处理完成"


