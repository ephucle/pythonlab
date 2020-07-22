import logging
import threading
import time
import sys

import pandas
import parsing_mhweb
import re
import xlsxwriter

pd = pandas.read_csv('crash_list.csv',encoding = "ISO-8859-1",low_memory=False)
pd = pd.filter(["UP", "Crash Details"])
pd = pd.dropna()
crashs = pd["Crash Details"]
ups = pd["UP"]

crash_sw  = zip(crashs, ups)
print(list(crash_sw))

sys.exit()

datas = []
print ("Values before run thread:", values)

def thread_function(name):
    logging.info("Thread %s: starting", name)
    global values
    values.append(name)
    time.sleep(0.1)
    logging.info("Thread %s: finishing", name)

def convert_sw(sw_string):
	'''
	convert_sw('CXP9024418/12_R64B39') = (CXP9024418/12, R64B39)
	'''
	items = re.split("_", sw_string)
	product = items[0]
	rev = items[1]
	sw = (product, rev)
	return sw

def thread_function_match(crash, sw):
	sw1 = sw.replace('(gNB)', '')
	sw_tuble = convert_sw(sw1)
	matched_tr_list = parsing_mhweb.matching_tr(crash, sw_tuble)
	global datas
	datas.append([crash, sw, matched_tr_list])

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    threads = list()
    for index in range(3):
        logging.info("Main    : create and start thread %d.", index)
#        x = threading.Thread(target=thread_function, args=(index,))
        x = threading.Thread(target=thread_function, args=(crash,sw,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)

    print ("Values after run thread:", values)

