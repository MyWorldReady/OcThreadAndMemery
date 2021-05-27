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

	
	hasInsertTitleStr="<h1>${htmlNameStr}</h1>"
	contailStr=$(grep ${hasInsertTitleStr} ${htmlFilePath})
	contailLen=${#contailStr}

	if [[ "$contailLen" != "0" ]]
	then
		# echo "已经处理过了"
		continue
	fi

	echo  ${htmlNameStr}.html

	oldStr='sans-serif">'
	newStr=$oldStr$hasInsertTitleStr
	if [[ $os = 1 ]]; then
		sed -i "s#${oldStr}#${newStr}#g" ${htmlFilePath}
	else
		sed -i "" "s#${oldStr}#${newStr}#g" ${htmlFilePath}
	fi

	
done
