import sys, os
from TikiTarget import TikiTarget
from TikiItem import TikiItem
from TikiHunterThread import TikiHunterThread
from TikiDisplayThread import TikiDisplayThread
from TikiHelper import *
from TikiHelper import getTargetsFromFile
from bs4 import BeautifulSoup
import requests
import time

TARGET_FILE = "target_list.txt"

targets = getTargetsFromFile(TARGET_FILE)
print(targets, type(targets))
for t in targets:
	print(t.info())

#[<TikiTarget.TikiTarget object at 0x7fd20115ce48>, <TikiTarget.TikiTarget object at 0x7fd20115c320>] <class 'list'>
#Patterns: ['Máy ảnh', 'lấy liền', 'Fujifilm'] | category: https://tiki.vn/may-anh-lay-lien/c2144
#Patterns: ['Nồi Chiên Không Dầu', 'Philips'] | category: https://tiki.vn/noi-chien/c8123
#sys.exit()

threads = []
displayThread = TikiDisplayThread()

for t in targets:
    hunter = TikiHunterThread(t)
    hunter.start()
    threads.append(hunter)
    displayThread.addHunter(hunter)

displayThread.start()

for t in threads:
    t.join()

print ("===== END Main ====")