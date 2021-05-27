#!/bin/bash

#系统类型  0:mac 1:win 2linux
os=1
if [ "$(uname)" == "Darwin" ]
then
	os=0
fi



filepath=$(cd "$(dirname "$0")"; pwd)  

sidebarpath=$filepath/menus/sidebar.html



for imgHttpEx in `grep "Tutorial/.*html" ${sidebarpath}`
do
	htmlNameFullStr=${imgHttpEx}
	if [[ $htmlNameFullStr = *Tutorial* ]]
 	then
		htmlNameStr=$(basename $htmlNameFullStr '.html"')
		# htmlNameStr=${htmlNameFullStr}
	else
		continue
	fi

	htmlFilePath=$filepath/Tutorial/${htmlNameStr}.html
	if [[ -e $htmlFilePath ]]
 	then
		continue
	else
		echo "$htmlNameFullStr"'=>'"${htmlNameStr}.html 丢失"
		echo 
	fi
	
done

echo "检查完成"
