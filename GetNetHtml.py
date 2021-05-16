# encoding:utf-8
#!/usr/bin/python


# 这个脚本的作用是快速下载一堆超链接对应的网页到本地
# 需要传递一个包含超链接的文本作为参数


# title.txt的大概样式如下
# 脚本会使用正则表达式匹配出地址和标题
'''
<li class="devsite-nav-item"><a href="https://developer.android.google.cn/training/efficient-downloads/efficient-network-access?hl=zh-cn" class="devsite-nav-title"><span class="devsite-nav-text" tooltip="">优化下载以实现高效网络访问</span></a></li>
<li class="devsite-nav-item"><a href="https://developer.android.google.cn/training/efficient-downloads/regular_updates?hl=zh-cn" class="devsite-nav-title"><span class="devsite-nav-text" tooltip="">尽量减少定期更新的影响</span></a></li>
<li class="devsite-nav-item"><a href="https://developer.android.google.cn/training/efficient-downloads/redundant_redundant?hl=zh-cn" class="devsite-nav-title"><span class="devsite-nav-text" tooltip="">避免冗余下载</span></a></li>
<li class="devsite-nav-item"><a href="https://developer.android.google.cn/training/efficient-downloads/connectivity_patterns?hl=zh-cn" class="devsite-nav-title"><span class="devsite-nav-text" tooltip="">基于连接类型修改模式</span></a></li></ul>
'''



import re
import os
import sys
import requests
reload(sys)
sys.setdefaultencoding("utf-8")

TITLENANME = "title.txt"
PWD = os.getcwd()
COPYHTML = PWD+"/"+"copy.html"
SIDEBARHTML = PWD+"/menus/"+"sidebar.html"



################### 需要返回自己截取html需要的部分  ###################
def SplitTargetHtml(html,fileName):
	htmlArr = re.findall(r'<article[\s\S]*?</article>',html)
	if len(htmlArr) > 0:
		return htmlArr[0]
	raise RuntimeError('网页没有包含对应的提取标签!!!!fileName='+fileName)
	return html













###################   ###################



len_argv = len(sys.argv)
if len_argv != 2:
	print("需要标题文件路径")
	sys.exit(0)

TITLEPATH = str(sys.argv[1])
if not os.path.exists(TITLEPATH):
	print("标题文件不存在"+TITLEPATH)
	sys.exit(0)
if not os.path.exists(SIDEBARHTML):
	print("sidebar.html不存在"+SIDEBARHTML)
	sys.exit(0)


def GetHtml(fileName,url):
	print("正在下载------"+fileName)
	r = requests.get(url)
	code = r.status_code
	if code != 200 :
		raise RuntimeError('网页下载失败!!!!fileName='+fileName+"  code="+str(code)+"  url="+url)
	# html = r.text.encode("utf-8")

	r.encoding = "utf-8"
	html = r.text
   	return html

# 正则分割出标题和地址
def GetAllHyperlinksData(fileContent):
    dic = {}
    listFileName = []


    # print(fileContent)
    # print(re.findall(r'<li',fileContent))
    for item in(re.findall(r'<a[\s\S]*?</a>',fileContent)):
    	hyper = re.findall(r'href="[\s\S]*?"',item)
    	if len(hyper) > 0:
    		# href="https://developer.android.google.cn/training/efficient-downloads/efficient-network-access?hl=zh-cn"
    		urlStr = hyper[0]
    		url = urlStr[6:-1]
    		# print(url)
    		if url == "":
    			raise RuntimeError('提取超链接失败!!!!')

    		title = item
    		title = re.sub(r'<span[\s\S]*?>', "", title)
    		title = re.sub(r'</span>', "", title)
    		title = re.sub(r'<a[\s\S]*?>', "", title)
    		title = re.sub(r'</a>', "", title)
    		title = title.replace(" ","")
    		title = title.replace("-","_")
    		title = title.replace(".","_")
    		title = title.replace("/","")
    		title = title.replace("（","")
    		title = title.replace("）","")
    		title = title.replace("(","")
    		title = title.replace(")","")

    		# print(title)

    		dic[title] = url
    		listFileName.append(title)

    return dic,listFileName

def GetFilePath(fileName):
	filePath = PWD + "/Tutorial/" +fileName+".html"
	return filePath

def CheckURL(dic):
	for key,value in dic.items():
		url = value
		mark1 = "http://"
		mark2 = "https://"
		if not (url.find(mark1) != -1 or url.find(mark2) != -1):
			raise RuntimeError('url不全,需要先补全url!!!!'+url)

def CheckFileNameLegal(dic):
	for key,value in dic.items():
		fileName = key
		if fileName.find(";") != -1:
			raise RuntimeError('文件名包含;!!!!fileName='+fileName)
		if fileName.find("&") != -1:
			raise RuntimeError('文件名包含&!!!!fileName='+fileName)

def CheckFileExit(listFileName):
	exists = 0
	exitArr = []
	for i, fileName in enumerate(listFileName):
		filePath = GetFilePath(fileName)
		# print(filePath)
		if os.path.exists(filePath):
			exists = 1
			exitArr.append(fileName)
			
	if exists == 1:
		print("--------以下文件存在-------")
		for i, fileName in enumerate(exitArr):
			print(fileName)
		raise RuntimeError('文件存在!!!!')
	return exists

def CheckSidebar(dic):
	filePath = SIDEBARHTML
	sidebarHtmlStr = open(filePath).read()
	for key,value in dic.items():
		fileName = key
		mark = fileName+".html"
		if sidebarHtmlStr.find(mark) != -1:
			raise RuntimeError('sidebar文件已经存在制定超链接!!!!'+mark)

def AddSidebar(dic,listFileName):
	filePath = SIDEBARHTML
	sidebarHtmlStr = open(filePath).read()
	resultStr = ''
	for i, fileName in enumerate(listFileName):
		resultStr = resultStr+'\n'
		resultStr = resultStr+'<li><a href="../Tutorial/{0}.html" target="main">{1}</a></li>'.format(fileName, fileName)
	replaceMark = "</ul>"
	strcontent = sidebarHtmlStr.replace(replaceMark,resultStr+replaceMark)
	f = open(filePath,'w')
	f.write(strcontent)

def SublimeShell(dic):
	for key,value in dic.items():
		# print(key+'     '+value)
		fileName = key
		filePath = GetFilePath(fileName)
		command = "subl "+filePath
		os.system(command)

def Download(dic,listFileName):
	copyHtmlStr = open(COPYHTML).read()
	for i, fileName in enumerate(listFileName):
		# print(key+'     '+value)
		filePath = GetFilePath(fileName)

		url = dic[fileName]
		strcontent = GetHtml(fileName,url)
		strcontent = SplitTargetHtml(strcontent,fileName)
		replaceMark = "</body>"
		h1 = '<h1>{0}</h1>'.format(fileName)
		strcontent = h1 + strcontent
		strcontent = copyHtmlStr.replace(replaceMark,strcontent+"\n\n\n"+replaceMark)
		f = open(filePath,'w')
		f.write(strcontent)

	return

def GetFileContent():
	# path = os.path.abspath(sys.argv[0])

	all_the_text = open(TITLEPATH).read()
	# print lines

	return all_the_text

if not os.path.exists(COPYHTML):
	raise RuntimeError('copy.html不文件存在!!!!')

info = GetAllHyperlinksData(GetFileContent())
dic = info[0]
listFileName = info[1]

CheckURL(dic)
CheckFileExit(listFileName)
CheckFileNameLegal(dic)
CheckSidebar(dic)
# for key,value in dic.items():
# 		# print(key+'     '+value)
# 		fileName = key
# 		filePath = GetFilePath(fileName)
# 		url = value
# 		print(fileName+"\t\t"+url)



for i, fileName in enumerate(listFileName):
	# print ("序号：%s   值：%s" % (i + 1, val))
	url = dic[fileName]
	print(fileName+"\t\t"+url)

Download(dic,listFileName)
AddSidebar(dic,listFileName)
SublimeShell(dic)
