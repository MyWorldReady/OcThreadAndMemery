# -*- encoding: utf-8 -*-


import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os
import re
import shutil

path_root = os.getcwd()
sidebarHtmlPath = "{}/menus/sidebar.html".format(path_root)
tutorialHtmlPath = "{}/Tutorial".format(path_root)
# len_argv = len(sys.argv)
# if len_argv != 3:
#     print("需要标题文件路径")
#     sys.exit(0)

# old_input = str(sys.argv[1])
# new_input = str(sys.argv[2])




def rename_menu(old_mark,new_mark):
    path = sidebarHtmlPath
    f = open(path, "r")
    content = f.read()
    f.close()
    # content = re.sub(r'<a href="http://www.52im[\s\S]*?</a>', "", content)

    ori_str = """/{}.html" target="main">{}</a>""".format(old_mark,old_mark)
    new_str = """/{}.html" target="main">{}</a>""".format(new_mark,new_mark)

    content = content.replace(ori_str, new_str)
    # content = content.replace("""<表>""", """<table>""")
    # content = content.replace("""<头>""", """<thead>""")
    # content = content.replace("""<img src="images/""", """<img src="https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@11.0/manual/images/""")
    # content = content.replace("""<img src="images\\""", """<img src="https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@11.0/manual/images/""")
    # content = content.replace("""<img src="/Images/""", """<img src="https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@11.0/manual/images/""")
    f = open(path, "w")
    f.write(content)
    f.flush()
    f.close()

def rename_file(old_name,new_name):
    path = "{}/{}.html".format(tutorialHtmlPath,old_name)
    new_path = "{}/{}.html".format(tutorialHtmlPath,new_name)
    os.rename(path, new_path )



input_dic= {
    
"TheUniversalAdditionalLightDatacomponent":"通用附加光数据组件",
"ShadowsinURP":"阴影",
"Cameras":"摄像机",
"TheUniversalAdditionalCameraDatacomponent":"CameraData组件",
"RenderType":"RenderType",
}


for key,value in input_dic.items():
    # print(key,"  ",value)
    print("key===",key)
    rename_menu(key,value)
    rename_file(key,value)


# rename_menu(old_input,new_input)
# rename_file(old_input,new_input)

