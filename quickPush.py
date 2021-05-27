# -*- encoding: utf-8 -*-


import sys
import os
import re
import shutil
import thread
import threading
import time

reload(sys)
sys.setdefaultencoding('utf-8')

path_root = os.getcwd()

MAXTHREAD = 8

threadLock = threading.Lock()
threads = []


def get_all_folder_name():
    arr = []
    res = os.listdir(path_root)
    for name in res:
        full = path_root + "/" + name
        if not os.path.isfile(full):
            arr.append(name)
    arr.sort()
    return arr


def do_pull(threadName, foler_name):
    process = os.popen("cd " + foler_name + ";git add ./;git commit -m ex;git push")
    output = process.read()
    process.close()

    print (threadName + "   " + foler_name + "   " + output + "\n")


foler_name_arr = get_all_folder_name()


def print_foler_name(threadName, foler_name):
    print (threadName + "  " + str(foler_name) + "\n")


def do_job(threadName):
    while True:
        b_exit = False
        foler_name = ''
        threadLock.acquire()
        cnt = len(foler_name_arr)
        if cnt > 0:
            b_exit = True
            foler_name = foler_name_arr.pop(0)
            # print (threadName + "  " + str(foler_name) + "\n")
        threadLock.release()
        if not b_exit:
            return
        # print_foler_name(threadName, foler_name)
        do_pull(threadName, foler_name)


class myThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        do_job(self.name)


def get_thread_creat_length():
    return MAXTHREAD + 1


for num in range(1, get_thread_creat_length()):
    name = "Thread-" + str(num)
    thread1 = myThread(num, name)
    threads.append(thread1)

print ("线程已启动 请稍后")
for thread1 in threads:
    thread1.start()

# 等待所有线程完成
for t in threads:
    t.join()
print "Exiting Main Thread"
