#!/bin/bash

#系统类型  0:mac 1:win 2linux
os=1
if [ "$(uname)" == "Darwin" ]
then
	os=0
fi



filepath=$(cd "$(dirname "$0")"; pwd)  

sidebarpath=$filepath/menus/sidebar.html
tutorialpath=$filepath/Tutorial/


arr=$(ls $tutorialpath | grep "html" )
for htmlFileWithExt in $arr; do

	htmlFileNoExt=$(basename $htmlFileWithExt '.html')


	# if [ "$htmlFileNoExt" = "几何变换详解" ];then
	# 	echo "$htmlFileNoExt"' => haha'
	# 	exit
	# fi


	isExit=1
	
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

		if [ "$htmlFileNoExt" = "$htmlNameStr" ]; then
			isExit=2
			break

		fi
		

	done

	if [ $isExit = 1 ]; then
		echo "sidebar.html不存在    $htmlFileNoExt"

	fi



done

echo '检查完成'


