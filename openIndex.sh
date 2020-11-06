#!/bin/bash

#这个脚本是用chrome的隐身模式打开index.html

#系统类型  0:mac 1:win 2linux
os=1
if [ "$(uname)" == "Darwin" ]
then
	os=0
fi

filepath=$(cd "$(dirname "$0")"; pwd)  

newHtmlPath="$filepath/index.html"


if [[ $os = 1 ]]; then
	# start $newHtmlPath
	x86Exe="/c/Program Files (x86)/Google/Chrome/Application/chrome.exe"
	x64Exe="/c/Program Files/Google/Chrome/Application/chrome.exe"
	tarExe=${x64Exe}
	if [[ -e ${x86Exe} ]]; then
		tarExe=${x86Exe}
	fi
	"${tarExe}" -incognito $newHtmlPath
else
	# open $newHtmlPath
	/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome -incognito $newHtmlPath
fi

