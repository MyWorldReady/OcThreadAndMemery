#!/bin/bash

# echo "第1个参数为：$1"; 
# echo "第2个参数为：$2"; 


if [ -z $1 ] 
then 
	echo "没有传入文件名" 
	exit
fi 

if [ -z $2 ] 
then 
	echo "文件名: $1"
else
	echo "文件名包含空格" 
	exit
fi 

#已经处理过的html文件的标记
newFileNoExt=$1
newFile=$1'.html'

#系统类型  0:mac 1:win 2linux
os=1
if [ "$(uname)" == "Darwin" ]
then
	os=0
fi

filepath=$(cd "$(dirname "$0")"; pwd)  

sidebarHtmlPath="${filepath}/menus/sidebar.html"
copyHtmlPath="${filepath}/copy.html"
newHtmlPath="${filepath}/Tutorial/$newFile"





contailStr=$(grep $1 ${sidebarHtmlPath})
contailLen=${#contailStr}

if [[ "$contailLen" != "0" ]]
then
	echo "文件名已经存在"
	exit
else
    echo "新建文件名: $newFileNoExt"
fi


li='\
'"<li><a href=\"../Tutorial/${newFileNoExt}.html\" target=\"main\">${newFileNoExt}</a></li>"


delStr1='</ul>'
delStr2='</body>'
delStr3='</html>'


oldStr='</ul>'
newStr=${li}${oldStr}
if [[ $os = 1 ]]; then
	sed -i "s^${oldStr}^${newStr}^g" ${sidebarHtmlPath}
else
	sed -i "" "s^${oldStr}^${newStr}^g" ${sidebarHtmlPath}
fi



fileContent=$(cat $copyHtmlPath) 
echo "${fileContent}" > $newHtmlPath

title='<h1>'${newFileNoExt}'</h1>'
oldStr='</body>'
newStr=${title}'\
\
\
\
\
\
'${oldStr}
if [[ $os = 1 ]]; then
	sed -i "s^${oldStr}^${newStr}^g" ${newHtmlPath}
else
	sed -i "" "s^${oldStr}^${newStr}^g" ${newHtmlPath}
fi

if [[ $os = 1 ]]; then
	subl $newHtmlPath
else
	/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl  $newHtmlPath
fi

if [[ $os = 1 ]]; then
	# start $newHtmlPath
	x86Exe="/c/Program Files (x86)/Google/Chrome/Application/chrome.exe"
	x64Exe="/c/Program Files/Google/Chrome/Application/chrome.exe"
	tarExe=${x64Exe}
	if [[ -e ${x86Exe} ]]; then
		tarExe=${x86Exe}
	fi
	#隐藏模式打开
	# "${tarExe}" -incognito $newHtmlPath
	"${tarExe}" $newHtmlPath

else
	open $newHtmlPath
	# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome -incognito $newHtmlPath
fi




