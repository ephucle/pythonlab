#!/usr/bin/python
# _*_ coding: utf-8
#remove crash from during 0h to 5h KST time
#version 191224_191600
#version 191225_191400
#support  top5 alarm, enb, gnb
#version 191226_152600
#add update sw pkg for DU, RU & TOTAL DU crash , if 4T crash sw have tail (gNB)
#version 191227_121000
#remove date time conconvert ==>do it manually by autofileter of excel
#version 191227_192600
#add again date, time for all DU crash, RU crash, DU ToTAL crash ==> no need manually ==> save ton of time
#version 191230_135600
#remove DU crash from 0h to 5h, remove RU crash from 0h to 5h, apply for monday for month change script
#add logo for tool, make life beautiful
#version 1.0 200102_172500
#update count TOP5 crash on the last crash day only
#version 1.1 200103_134400
#bug fix 3. BS_DG_Alarm, "DU" to "DG" in area column

#version 1.2 200114_111000, BUG fix
#UnicodeDecodeError: 'ascii' codec can't decode byte 0xf3 in position 170: ordinal not in range(128)

#version 1.3 200316_140700, BUG fix
#CD Zone Name Change GumiSagokT3 => gb-gumi-imeun-TC4

#version 1.4 200331_132800, BUG fix
#CD Zone Name Change GumiGongdan4T4 => gb-gumi-imeun-W114

#version 1.5 200401_125200, BUG fix
#CD Zone Name Change GumiJinpyeong3T0 => gb-gumi-hwangsang-W138

#version 1.6 200421_093500
#support checking 4T gNB, with product code  CXP9024418/15

#version 1.7 200422_115700
#fix (gNB) include to SW version of product code  CXP9024418/15

#version 1.8 200423_122900
#fix issue nodename exist in nodeid.log but does not exist in node_UP.log


import re
import pytz
#from datetime import datetime
import datetime
from datetime import datetime as dt
from pytz import timezone

#file browser
import os
from fnmatch import fnmatch
import xlsxwriter 

version = "version 1.8 200423_122900"
#LOGO
print ",-.----.                                                              "
print "\    /  \     ,---,       ,-.----.    .--.--.       ,---,.,-.----.    "
print "|   :    \   '  .' \      \    /  \  /  /    '.   ,'  .' |\    /  \   "
print "|   |  .\ : /  ;    '.    ;   :    \|  :  /`. / ,---.'   |;   :    \  "
print ".   :  |: |:  :       \   |   | .\ :;  |  |--`  |   |   .'|   | .\ :  "
print "|   |   \ ::  |   /\   \  .   : |: ||  :  ;_    :   :  |-,.   : |: |  "
print "|   : .   /|  :  ' ;.   : |   |  \ : \  \    `. :   |  ;/||   |  \ :  "
print ";   | |`-' |  |  ;/  \   \|   : .  /  `----.   \|   :   .'|   : .  /  "
print "|   | ;    '  :  | \  \ ,';   | |  \  __ \  \  ||   |  |-,;   | |  \  "
print ":   ' |    |  |  '  '--'  |   | ;\  \/  /`--'  /'   :  ;/||   | ;\  \ "
print ":   : :    |  :  :        :   ' | \.'--'.     / |   |    \:   ' | \.' "
print "|   | :    |  | ,'        :   : :-'   `--'---'  |   :   .':   : :-'   "
print "`---'.|    `--''          |   |.'               |   | ,'  |   |.'     "
print "  `---`                   `---'                 `----'    `---'       "
print version

#this distionary to store nodename & sw version
swdict = {}

#this is dictionary for crash signature & tr id
trdict = {}

#this list to store list of 4T gNB
fourtxlist = []

cdzone = [
'gb-gumi-hwangsang-W138'
'gb-gumi-imeun-W114'
'gb-gumi-imeun-TC4'
'bs-jingu-bujeon-10-30',
'bs-jingu-bujeon-10-29',
'bs-jingu-bujeon-10-27',
'bs-jingu-bujeon-10-20',
'bs-jingu-beomjeon-10-03',
'bs-jingu-bujeon-10-28',
'bs-jingu-bujeon-10-26',
'bs-jingu-bujeon-10-22',
'bs-jingu-bujeon-10-21',
'bs-jingu-bujeon-10-19',
'bs-jingu-bujeon-10-17',
'bs-jingu-bujeon-10-16',
'bs-jingu-bujeon-10-15',
'bs-jingu-bujeon-10-14',
'bs-jingu-bujeon-10-12',
'bs-jingu-bujeon-10-11',
'bs-jingu-bujeon-10-08',
'bs-jingu-danggam-10-01',
'bs-jingu-bujeon-10-10',
'bs-jingu-bujeon-10-09',
'bs-jingu-bujeon-10-06',
'bs-jingu-bujeon-10-04',
'bs-jingu-bujeon-10-03',
'bs-jingu-bujeon-10-02',
'bs-jingu-bujeon-10-01',
'bs-jingu-buam-10-02',
'bs-jingu-beomcheon-10-01',
'bs-donggu-sujeong-10-01',
'bs-donggu-choryang-10-09',
'bs-donggu-choryang-10-08',
'bs-donggu-choryang-10-07',
'bs-donggu-choryang-10-06',
'bs-donggu-choryang-10-05',
'bs-donggu-choryang-10-04',
'bs-jingu-bujeon-10-24',
'bs-jingu-bujeon-10-23',
'bs-jingu-bujeon-10-18',
'bs-jingu-bujeon-10-07',
'bs-jingu-bujeon-10-05',
'bs-jingu-buam-10-04',
'bs-jingu-buam-10-03',
'bs-jingu-buam-10-01',
'bs-donggu-sujeong-10-02',
'jingu-buam-QD30',
'bs-jingu-bujeon-10-25',
'jingu-buam-QD31',
'jingu-buam-DA8',
'jingu-buam-QB17',
'jingu-buam-QB10',
'donggu-sujeong-TC0',
'jingu-buam-DA3',
'donggu-sujeong-TB8',
'donggu-sujeong-TA3',
'donggu-sujeong-TA1',
'donggu-sujeong-TB0',
'donggu-sujeong-QB1',
'donggu-sujeong-DA1',
'jingu-buam-QD23',
'jingu-buam-QA1',
'jingu-buam-QA17',
'jingu-buam-DB2',
'donggu-sujeong-TC8',
'donggu-sujeong-DB0',
'jingu-buam-QA21',
'jingu-buam-QA22',
'jingu-buam-QA23',
'jingu-buam-QA29',
'jingu-buam-QC21',
'jingu-buam-QC22',
'jingu-buam-QD21',
'jingu-buam-QD25',
'jingu-buam-QD26',
'jingu-buam-TA23',
'jingu-buam-TA31',
'jingu-buam-QD28',
'jingu-buam-QD27',
'jingu-buam-QA30',
'jingu-buam-QC24',
'jingu-buam-QB27',
'jingu-buam-QA32',
'jingu-buam-QD29',
'jingu-buam-QA33',
'jingu-buam-QC26',
'jingu-buam-QA39',
'jingu-buam-QA40',
]

#print cdzone
#exit()

#old
#dt = dt.strftime("%Y/%m/%d %H:%M:%S")
def convert_datetime_timezone(dt, tz1, tz2):
	tz1 = pytz.timezone(tz1)
	tz2 = pytz.timezone(tz2)
	
	#below la dinh dang cua log cua node
	dt = datetime.datetime.strptime(dt,"%Y-%m-%d %H:%M:%S")
	dt = tz1.localize(dt)
	dt = dt.astimezone(tz2)
	
	#below la dinh dang can lam report excel
	#dt = dt.strftime("%Y/%m/%d %H:%M:%S")
	#new
	
	dt1 = dt.strftime("%Y/%m/%d %H:%M:%S")
	dt2 = dt.strftime("%m/%d/%Y %H:%M:%S")
	
	return [dt1, dt2];
	#return format ["%Y/%m/%d %H:%M:%S", "%m/%d/%Y %H:%M:%S"]

def removeduplicatedandcount(gnb):
	#gnb = ['HX85427', 'HY13193', 'HX95786', 'HX95255', 'HX97721', 'New Crash', 'New Crash', 'New Crash', 'HX95786', 'HX95786', 'New Crash', 'HX95786', 'HX85427', 'HY13193', 'HX95786', 'New Crash', 'HX95786', 'New Crash', 'HX95786', 'New Crash', 'New Crash', 'New Crash', 'HY12920', 'HX97721', 'HX95786', 'New Crash', 'New Crash', 'New Crash', 'HX95786', 'HX95786']
	x ={}
	gnbuniq = list(set(gnb))
	#reset
	for item in gnbuniq:
		x[item]=0
	#bat dau dem
	for i in  x:
		for tr in gnb:
			if i == tr:
				x[i]+=1
	
	y = sorted(x.items(), key=lambda x: x[1], reverse=True)
	#y = [('New Crash', 38), ('HX95786', 34), ('HX96268', 12), ('HX82707', 9), ('HX85427', 6), ('HX97721', 5), ('HY17824', 4), ('HY13193', 3), ('HX95255', 2), ('HX96299', 2), ('HX82729', 2), ('HY10892', 1), ('HY19547', 1), ('HX99090', 1), ('HY10307', 1), ('HY12920', 1), ('HX95174', 1), ('HX97383', 1), ('HY11574', 1)]

	return y

#file browser
root = '.'
#find DU & RU Crash log file

dufiles = []
rufiles = []
upfiles = []
bsupfiles = []
dgupfiles = []
nodeidfiles = []
alarmfiles = []
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, "*DU.log"):
            #print os.path.join(path, name)
			dufiles.append(os.path.join(path,name))

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, "*RU.log"):
            #print os.path.join(path, name)
			rufiles.append(os.path.join(path, name))
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, "*UP.log"):
            #print os.path.join(path, name)
			upfiles.append(os.path.join(path, name))

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, "*UP.log") and fnmatch(path, "*BS*"):
            #print os.path.join(path, name)
			bsupfiles.append(os.path.join(path, name))
			
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, "*UP.log") and fnmatch(path, "*DG*"):
            #print os.path.join(path, name)
			dgupfiles.append(os.path.join(path, name))
			
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, "*nodeid.log"):
            #print os.path.join(path, name)
			nodeidfiles.append(os.path.join(path, name))

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, "alarm.log"):
            #print os.path.join(path, name)
			alarmfiles.append(os.path.join(path,name))
print dufiles
#dufiles = ['./BS1/crash_DU.log', './BS2/crash_DU.log', './DG1/crash_DU.log', './DG2/crash_DU.log']

print rufiles
#rufiles = ['./BS1/crash_RU.log', './BS2/crash_RU.log', './DG1/crash_RU.log', './DG2/crash_RU.log']

print upfiles
#['./BS1/node_UP.log', './BS2/node_UP.log', './DG1/node_UP.log', './DG2/node_UP.log']

print bsupfiles
print dgupfiles
print nodeidfiles
print alarmfiles
#exit()

#start parse trmapping.txt
lines = [line.rstrip() for line in open("./trmapping.txt")]
#print lines

n=1
#TR MAPPING
for line in lines:	
	#m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")

	#note for regular expression
	#(.*?): match any string
	#\s+: match one or more continuous space for tab
	#(\w\w\d\d\d\d\d): match an TR ID (HX12345/HW45678/HY12345)
	#m = re.match(r"(.*?)	(\w\w\d\d\d\d\d)", line)
	m = re.match(r"(.*?)\s+(\w\w\d\d\d\d\d)", line)
	
	#rat quan trong, neu ko se fail
	if m:
		crashsignature = m.group(1)
		tr = m.group(2)
	
		report = str(n) + " | " + crashsignature + " | "+ str(tr)
		#print report
		
		trdict[crashsignature] = tr
		n+=1

#print trdict
#print trdict.keys()
#exit()

#start parse DU log
#file1 = open("du.txt","w+")
workbook = xlsxwriter.Workbook('crash_report.xlsx') 
worksheet = workbook.add_worksheet("2. BS_DG_Crash") 
worksheet.write('A1', 'Site Name') 
worksheet.write('B1', 'Date') 
worksheet.write('C1', 'Time') 
worksheet.write('D1', 'Date Time(UTC)') 
worksheet.write('E1', '+09:00') 
worksheet.write('F1', "Date Time(KST)") 
worksheet.write('G1', 'KST Dalry') 
worksheet.write('H1', 'Crash HW') 
worksheet.write('I1', 'UP')
worksheet.write('J1', '4T4RX')
worksheet.write('K1', 'Crash Details')
worksheet.write('L1', '#')
worksheet.write('M1', 'TRMapping')
worksheet.write('N1', 'Area')
worksheet.write('O1', 'CD Zone')


#create worksheet for RU crash
worksheet7 = workbook.add_worksheet("2.BS_DG_Total_RU_Crash") 
#Site Name	Date	Time	Date Time(UTC)	 +09:00	Date Time(KST)	Crash HW	UP	Crash Details	#	TR Mapping	CD Zone

worksheet7.write('A1', 'Site Name') 
worksheet7.write('B1', 'Date') 
worksheet7.write('C1', 'Time') 
worksheet7.write('D1', 'Date Time(UTC)') 
worksheet7.write('E1', '+09:00') 
worksheet7.write('F1', "Date Time(KST)") 
worksheet7.write('G1', 'Crash HW') 
worksheet7.write('H1', 'UP')
worksheet7.write('I1', 'Crash Details')
worksheet7.write('J1', '#')
worksheet7.write('K1', 'TRMapping')
worksheet7.write('L1', 'CD Zone')







#start write 5.BS_DG_Total#############

startline = 2
for path in upfiles:
	print "parsing file " + path + "..."
	lines = [line for line in open(path)]
	for line in lines:	
		#remove new line charactor
		line = line.rstrip()
		
		#line = haeundae-jwadong-QB0 CXP9024418/6_R73C96
		x = re.split("\s", line)
		#print(x)
		nodename = x[0]	
		#print nodename
		
		# neu co sw level thi len x se lon hon 1
		if len(x) > 1:
			sw = x[1]
		else:
			sw = ""
		
			
		#swdict, create dictionary,nodename vs sw to replace vlookup sw pkg
		swdict[nodename] = sw
		#print nodename,sw
		report = str(startline -1)+ " " + nodename + "|" + sw
		#print report		
				
		#worksheet3.write('A'+str(startline), nodename) 
		#worksheet3.write('B'+str(startline), sw) 				
		startline+=1
#end write busandaegu####################

#print swdict
print "Total of nodes: "+ str(startline -2)

#start write 4T4R DU Check(gNB&eNB)#############
#Node_Name	PKG_Ver	686	4T4RX

worksheet6 = workbook.add_worksheet("4T4R DU Check(gNB&eNB)")   
worksheet6.write('A1', 'Node_Name') 
worksheet6.write('B1', 'PKG_Ver') 
worksheet6.write('C1', '') 
worksheet6.write('D1', '4T4RX') 

startline = 2
#UPDATE 4T TAB
print "Start update 4T4R DU Check(gNB&eNB)..."
for path in nodeidfiles:
	print "parsing file " + path + "..."
	lines = [line for line in open(path)]
	for line in lines:	
		#remove new line charactor
		line = line.rstrip()
		
		#line = youngdo-namhang-TC7.log:ENodeBFunction=1                                        eNBId             62866
		#line = metro2dg-suseong-skb-10-89.log:GNBCUCPFunction=1                                       gNBId             1214782
		x = re.split(".log:", line)
		#print(x)
		nodename = x[0]	
		remain = x[1]
		#remain = 'ENodeBFunction=1                                        eNBId             62866'
		
		y=re.split("\s+",remain)
		#y = ['ENodeBFunction=1', 'eNBId', '62866']
		#y = ['GNBCUCPFunction=1', 'gNBId', '1181721']
		nodetype = y[1]
		#nodetype = eNBId or gNBId
		#nodeid = y[2]
		
		#gNB 4T: node type is gNBId, and swpkg id contain /6
		
		#print("trouble shooting...")
		#print(nodename)
		#print (swdict.get(nodename))
		if nodename in swdict.keys():
			if nodetype == 'gNBId' and "/6" in swdict.get(nodename) :	
				worksheet6.write('A'+str(startline), nodename)
				if "BS1" in path:
					worksheet6.write('C'+str(startline), "BS1")
				if "BS2" in path:
					worksheet6.write('C'+str(startline), "BS2")
				if "DG1" in path:
					worksheet6.write('C'+str(startline), "DG1")
				if "DG2" in path:
					worksheet6.write('C'+str(startline), "DG2")
				#get sw pkg thank to swdict dictionary
				
				#neu goi sw khac CXP9024418/6_R73E23 thi them (gNB) vao trong sw pkg
				if swdict.get(nodename) != "CXP9024418/6_R73E23" :
					worksheet6.write('B'+str(startline),swdict.get(nodename)+"(gNB)") 
				else:
					worksheet6.write('B'+str(startline),swdict.get(nodename))
				worksheet6.write('D'+str(startline),"4T4RX") 
				
				#create list of 4T gNB for other task
				fourtxlist.append(nodename)
				startline+=1
			
			#gNB 4T: node type is gNBId, and swpkg id contain /15
			if nodetype == 'gNBId' and "/15" in swdict.get(nodename) :	
				worksheet6.write('A'+str(startline), nodename)
				if "BS1" in path:
					worksheet6.write('C'+str(startline), "BS1")
				if "BS2" in path:
					worksheet6.write('C'+str(startline), "BS2")
				if "DG1" in path:
					worksheet6.write('C'+str(startline), "DG1")
				if "DG2" in path:
					worksheet6.write('C'+str(startline), "DG2")
				#get sw pkg thank to swdict dictionary
				
				worksheet6.write('B'+str(startline),swdict.get(nodename))
				worksheet6.write('D'+str(startline),"4T4RX") 
				
				#create list of 4T gNB for other task
				fourtxlist.append(nodename)
				startline+=1
#print fourtxlist
print "number of 4TX nodes:" + str(len(fourtxlist))
#end write 4T####################

#update swdict for 4TX gNB
for node in fourtxlist:
	currentsw = swdict[node]
	if currentsw != "CXP9024418/6_R73E23" and "/15" not in currentsw:
		swdict[node] = currentsw+"(gNB)"

#print swdict

#start write 5.BS_Site#############
worksheet4 = workbook.add_worksheet("5.BS_Site")   
worksheet4.write('A1', 'Node_Name') 
worksheet4.write('B1', 'PKG_Ver') 
worksheet4.write('C1', ' ') 
worksheet4.write('D1', '4T4RX') 

startline = 2
#UPDATE BS_Site tab
print "Start update BG_Site TAB..."
for path in bsupfiles:
	print "parsing file " + path + "..."
	lines = [line for line in open(path)]
	for line in lines:	
		#remove new line charactor
		line = line.rstrip()
		
		#line = haeundae-jwadong-QB0 CXP9024418/6_R73C96
		x = re.split("\s", line)
		#print(x)
		nodename = x[0]	
		#print nodename
		# neu co sw level thi len x se lon hon 1
		if len(x) > 1:
			sw = x[1]
		else:
			sw = ""
		#print nodename,sw
		#report = nodename + "|" + sw
		#print report		
				
		worksheet4.write('A'+str(startline), nodename) 
		if "/BS1/" in path:
			worksheet4.write('C'+str(startline), "BS1") 
		if "/BS2/" in path:
			worksheet4.write('C'+str(startline), "BS2") 
		if "/DG1/" in path:
			worksheet4.write('C'+str(startline), "DG1") 
		if "/DG2/" in path:
			worksheet4.write('C'+str(startline), "DG2") 
		
		#process 4TX node
		# "CXP9024418/6_R73E23" is madatory sw for 4T gnb
		if nodename in fourtxlist:
			if sw != "CXP9024418/6_R73E23" and "/15" not in sw:
				worksheet4.write('B'+str(startline), sw + "(gNB)")
			else :
				worksheet4.write('B'+str(startline), sw)
			worksheet4.write('D'+str(startline), "4T4RX")
		else:
			worksheet4.write('B'+str(startline), sw) 
		
		startline+=1
#end write busan####################

#start write 5.DG_Site#############
worksheet5 = workbook.add_worksheet("5.DG_Site")   
worksheet5.write('A1', 'Node_Name') 
worksheet5.write('B1', 'PKG_Ver') 
worksheet5.write('C1', ' ') 
worksheet5.write('D1', '4T4RX') 

startline = 2
#UPDATE DG_Site tab
print "Start update DG_Site TAB..."
for path in dgupfiles:
	print "parsing file " + path + "..."
	lines = [line for line in open(path)]
	for line in lines:	
		#remove new line charactor
		line = line.rstrip()
		
		#line = haeundae-jwadong-QB0 CXP9024418/6_R73C96
		x = re.split("\s", line)
		#print(x)
		nodename = x[0]	
		# neu co sw level thi len x se lon hon 1
		if len(x) > 1:
			sw = x[1]	
		else:
			sw = ""
		
		#print nodename,sw
		#report = nodename + "|" + sw
		#print report		
				
		worksheet5.write('A'+str(startline), nodename) 
		
		if "/BS1/" in path:
			worksheet5.write('C'+str(startline), "BS1") 
		if "/BS2/" in path:
			worksheet5.write('C'+str(startline), "BS2") 
		if "/DG1/" in path:
			worksheet5.write('C'+str(startline), "DG1") 
		if "/DG2/" in path:
			worksheet5.write('C'+str(startline), "DG2") 
		#worksheet5.write('B'+str(startline), sw) 
		#process 4TX node
		# "CXP9024418/6_R73E23" is madatory sw for 4T gnb
		if nodename in fourtxlist:
			if sw != "CXP9024418/6_R73E23" and "/15" not in sw:
				worksheet5.write('B'+str(startline), sw + "(gNB)")
			else :
				worksheet5.write('B'+str(startline), sw)
			worksheet5.write('D'+str(startline), "4T4RX")
		else:
			worksheet5.write('B'+str(startline), sw) 
		
		
		startline+=1
#end write daegu####################

#start write 5.BS_DG_Total, second time#############
worksheet3 = workbook.add_worksheet("5.BS_DG_Total")   
worksheet3.write('A1', 'Node_Name') 
worksheet3.write('B1', 'PKG_Ver') 
worksheet3.write('C1', ' ') 
worksheet3.write('D1', '4T4RX') 

startline = 2
#Update BS_DG_TOTAL TAB
no_of_bs1_node = 0 
no_of_bs2_node = 0 
no_of_dg1_node = 0 
no_of_dg2_node = 0 

#update BS_DG_TOTAL TAB 
print "Start update BS_DG_TOTAL TAB..."
for path in upfiles:
	print "parsing file " + path + "..."
	lines = [line for line in open(path)]
	for line in lines:	
		#remove new line charactor
		line = line.rstrip()
		
		#line = haeundae-jwadong-QB0 CXP9024418/6_R73C96
		x = re.split("\s", line)
		#print(x)
		nodename = x[0]	
		#print nodename
		
		if len(x) > 1:
			sw = x[1]
		else :
			sw = ""
			
		#swdict, create dictionary,nodename vs sw to replace vlookup sw pkg
		swdict[nodename] = sw
		#print nodename,sw
		report = str(startline -1)+ " " + nodename + "|" + sw
		#print report		
				
		worksheet3.write('A'+str(startline), nodename)
		if "BS1" in path :
			worksheet3.write('C'+str(startline), "BS1")
			no_of_bs1_node+=1
		if "BS2" in path :
			worksheet3.write('C'+str(startline), "BS2")	
			no_of_bs2_node+=1
		if "DG1" in path :
			worksheet3.write('C'+str(startline), "DG1")
			no_of_dg1_node+=1
		if "DG2" in path :
			worksheet3.write('C'+str(startline), "DG2")
			no_of_dg2_node+=1
			
		if nodename in fourtxlist :	
			if sw != "CXP9024418/6_R73E23" and "/15" not in sw:
				worksheet3.write('B'+str(startline), sw + "(gNB)") 
			else:
				worksheet3.write('B'+str(startline), sw) 
			worksheet3.write('D'+str(startline), "4T4RX")
		else:
			worksheet3.write('B'+str(startline), sw)
		
		
		startline+=1

print "Number of node in BS1 ENM: "+ str(no_of_bs1_node)
print "Number of node in BS2 ENM: "+ str(no_of_bs2_node)
print "Number of node in DG1 ENM: "+ str(no_of_dg1_node)
print "Number of node in DG2 ENM: "+ str(no_of_dg2_node)

print "TOTAL BUSAN Nodes:" + str(no_of_bs1_node + no_of_bs2_node)
print "TOTAL DAEGU Nodes:" + str(no_of_dg1_node + no_of_dg2_node)
#end write total sw package####################


#start to write data from second line
#Site Name	Date	Time	Date Time(UTC)	 +09:00	Date Time(KST)	KST Dalry	Crash HW	UP	4T4RX	Crash Details	#	TRMapping	Area	CD Zone

#start DU crash report
startline = 2
new_crash = 0
old_crash =0
tr_list_gnb = []
tr_list_enb = []

#find last DU crash date
print "find last DU crash date ..."
last_crash_date = dt.strptime("1/1/1970",'%m/%d/%Y')
for path in dufiles:
	print "parsing file " + path + "..."
	lines = [line for line in open(path)]



	for line in lines:	
		#remove new line charactor
		line = line.rstrip()
		
		#line = seogu-buyong-TA9.log:2019-12-18 12:37:45 LLOG  0001 DUS5201     Program restart. Reason: Snapshot request. Program: lratBbomArmLm.bin. PMD: pmd-bbmcBbOmMeThrea-21741-20191218-123745. Extra: BB Restart: Emca 4:DSP 1: "LPP_send to invalid virtual pidnpid: 0x196"
		x = re.split(".log:", line)
		#print(x)
		nodename = x[0]	
		#print nodename
		
		remain1 = x[1]	
		#remain1 = 2019-12-18 12:37:45 LLOG  0001 DUS5201     Program restart. Reason: Snapshot request. Program: lratBbomArmLm.bin. PMD: pmd-bbmcBbOmMeThrea-21741-20191218-123745. Extra: BB Restart: Emca 4:DSP 1: "LPP_send to invalid virtual pidnpid: 0x196"
		
		
		
		#\s: space, split first 2 space
		y = re.split(" LLOG  ", remain1, 2)
		#print y
		
		#y = ['2019-12-18 09:49:31', '0001 DUS5201     Program restart. Reason: Snapshot request. Program: lratBbomArmLm.bin. PMD: pmd-bbmcBbOmMeThrea-15363-20191218-094931. Extra: BB Restart: Emca 4:DSP 1: "LPP_send to invalid virtual pidnpid: 0x18d"']
		utctime = y[0]
		#utctime = 2019-12-18 09:49:31
						
		utctime_new = utctime.replace("-", "/",2)		
		utctime_new2 = convert_datetime_timezone(utctime,"UTC","UTC")
		
		#convert timezone to korea time
		#utctime = 2019-12-18 09:49:31
		
		#["%Y/%m/%d %H:%M:%S", "%m/%d/%Y %H:%M:%S"]
		ksttime_new = convert_datetime_timezone(utctime,"UTC","Asia/Seoul")
		kstdaytime = ksttime_new[0]
		#string.replace(old, new, count)
		#utctime_new = utctime.replace('-','/',2)
		
		#split UTC date and time
		#temp = re.split("\s",utctime)
		#temp = re.split("\s",utctime_new)
		temp = re.split("\s",utctime_new2[1])
		date = temp[0]
		time = temp[1]
		
		#split to get kst day
		#ksttime_new[0] = 12/18/2019 13:57:59
		temp = re.split("\s", ksttime_new[1])		
		KST_Dalry = temp[0]
		
		
		
		kstdate = dt.strptime(KST_Dalry,'%m/%d/%Y')
		#find the last day, to find top 5
		if last_crash_date < kstdate:
			last_crash_date = kstdate

print "Last DU crash date: "+ str(last_crash_date)


#update DU crash TAB
print "Start update DU Crash TAB..."
for path in dufiles:
	print "parsing file " + path + "..."
	lines = [line for line in open(path)]



	for line in lines:	
		#add on 14Jan2020, bug fig
		line = line.decode('utf-8','ignore').encode("utf-8")
		
		#remove new line charactor
		line = line.rstrip()
		
		#line = seogu-buyong-TA9.log:2019-12-18 12:37:45 LLOG  0001 DUS5201     Program restart. Reason: Snapshot request. Program: lratBbomArmLm.bin. PMD: pmd-bbmcBbOmMeThrea-21741-20191218-123745. Extra: BB Restart: Emca 4:DSP 1: "LPP_send to invalid virtual pidnpid: 0x196"
		x = re.split(".log:", line)
		#print(x)
		nodename = x[0]	
		#print nodename
		
		remain1 = x[1]	
		#remain1 = 2019-12-18 12:37:45 LLOG  0001 DUS5201     Program restart. Reason: Snapshot request. Program: lratBbomArmLm.bin. PMD: pmd-bbmcBbOmMeThrea-21741-20191218-123745. Extra: BB Restart: Emca 4:DSP 1: "LPP_send to invalid virtual pidnpid: 0x196"
		
		
		
		#\s: space, split first 2 space
		y = re.split(" LLOG  ", remain1, 2)
		#print y
		
		#y = ['2019-12-18 09:49:31', '0001 DUS5201     Program restart. Reason: Snapshot request. Program: lratBbomArmLm.bin. PMD: pmd-bbmcBbOmMeThrea-15363-20191218-094931. Extra: BB Restart: Emca 4:DSP 1: "LPP_send to invalid virtual pidnpid: 0x18d"']
		utctime = y[0]
		#utctime = 2019-12-18 09:49:31
						
		utctime_new = utctime.replace("-", "/",2)		
		utctime_new2 = convert_datetime_timezone(utctime,"UTC","UTC")
		
		#convert timezone to korea time
		#utctime = 2019-12-18 09:49:31
		
		#["%Y/%m/%d %H:%M:%S", "%m/%d/%Y %H:%M:%S"]
		ksttime_new = convert_datetime_timezone(utctime,"UTC","Asia/Seoul")
		kstdaytime = ksttime_new[0]
		#string.replace(old, new, count)
		#utctime_new = utctime.replace('-','/',2)
		
		#split UTC date and time
		#temp = re.split("\s",utctime)
		#temp = re.split("\s",utctime_new)
		temp = re.split("\s",utctime_new2[1])
		date = temp[0]
		time = temp[1]
		
		#split to get kst day
		#ksttime_new[0] = 12/18/2019 13:57:59
		temp = re.split("\s", ksttime_new[1])		
		KST_Dalry = temp[0]
		
		#KST_hhmmss = 13:57:59
		KST_hhmmss = temp[1]
		remain2= y[1]
		
		#remain2 = '0001 DUS5201     Program restart. Reason: Snapshot request. Program: lratBbomArmLm.bin. PMD: pmd-bbmcBbOmMeThrea-15363-20191218-094931. Extra: BB Restart: Emca 4:DSP 1: "LPP_send to invalid virtual pidnpid: 0x18d"'
		#print utctime
		#print ksttime
		#print remain2
		
		z = re.split("\s+", remain2, 2)
		#print z
		#z =  ['0001', 'DUS5201', 'Program restart. Reason: Snapshot request. Program: lratBbomArmLm.bin. PMD: pmd-bbmcBbOmMeThrea-15363-20191218-094931. Extra: BB Restart: Emca 4:DSP 1: "LPP_send to invalid virtual pidnpid: 0x18d"']
		
		hw = z[1]
		#hw = DUS5201 or DUS5301
		crash = z[2]
		#crash = Program restart. Reason: Snapshot request. Program: lratBbomArmLm.bin. PMD: pmd-bbmcBbOmMeThrea-15363-20191218-094931. Extra: BB Restart: Emca 4:DSP 1: "LPP_send to invalid virtual pidnpid: 0x18d"
		
		if hw == "DUS5201":
			hw = "eNB"
		if hw == "DUS5301":
			hw = "gNB"
		#print hw
		#print crash
		
		#turn on when need to troublesooting
		#print nodename,"|",utctime, "|", date, "|", time ,"|",ksttime,"|", KST_Dalry, "|",hw,"|",crash
		
		#Site Name	Date	Time	Date Time(UTC)	 +09:00	Date Time(KST)	KST Dalry	Crash HW	UP	4T4RX	Crash Details	#	TRMapping	Area	CD Zone

		report = str(startline-1) + " " + nodename + " | " +  date + "|" + time + "|" + "|" + utctime_new2[0] +  "|" + "09:00 | "  + kstdaytime + "|" + KST_Dalry + "|" + hw + "|" + crash
		
		#print report
		#write to text file to count number	
		#file1.write(report+"\r\n")
		#write data to excel file
		
		#remove crash from 00 KST to 05 KST 
		if not re.search("0[012345]:\d\d:\d\d",KST_hhmmss):
			worksheet.write('A'+str(startline), nodename) 
			#worksheet.write('B'+str(startline), date) 
			
			# Create a format for the date or time.
			date_format = workbook.add_format({'num_format': 'mm/dd/yyyy','align': 'left'})
			utcdate = dt.strptime(date,'%m/%d/%Y')			
			worksheet.write_datetime('B'+str(startline), utcdate,  date_format) 
			
			date_format = workbook.add_format({'num_format': 'hh:mm:ss','align': 'left'})
			utctime = dt.strptime(time,'%H:%M:%S')			
			#worksheet.write('C'+str(startline), time) 
			worksheet.write_datetime('C'+str(startline), utctime,  date_format) 
			
			date_format = workbook.add_format({'num_format': 'yyyy/mm/dd hh:mm:ss','align': 'left'})
			utcdatetime = dt.strptime(utctime_new2[0],'%Y/%m/%d %H:%M:%S')			
			worksheet.write_datetime('D'+str(startline), utcdatetime,  date_format) 
			#worksheet.write('D'+str(startline), utctime_new2[0]) 
			
			worksheet.write('E'+str(startline), '9:00')
			
			
			#worksheet.write('F'+str(startline), kstdaytime) 
			date_format = workbook.add_format({'num_format': 'yyyy/mm/dd hh:mm:ss','align': 'left'})
			kstdatetime = dt.strptime(kstdaytime,'%Y/%m/%d %H:%M:%S')			
			worksheet.write_datetime('F'+str(startline), kstdatetime,  date_format) 
			
			#worksheet.write('G'+str(startline), KST_Dalry) 
			date_format = workbook.add_format({'num_format': 'mm/dd/yyyy/','align': 'left'})
			
			kstdate = dt.strptime(KST_Dalry,'%m/%d/%Y')
			
			worksheet.write_datetime('G'+str(startline), kstdate,  date_format) 
			
			worksheet.write('H'+str(startline), hw) 
			if nodename in swdict.keys():
				if nodename in fourtxlist and swdict[nodename] != "CXP9024418/6_R73E23":				
					worksheet.write('I'+str(startline), swdict[nodename]+"(gNB)")
				else:
					worksheet.write('I'+str(startline), swdict[nodename])
			if nodename in fourtxlist:
				worksheet.write('J'+str(startline), '4T4RX')
			
			worksheet.write('K'+str(startline), crash)
			worksheet.write('L'+str(startline), '#')
			
			#TR MAPPING
			flag_mapping = 0
			for signature in trdict.keys():
				if signature in crash:
					tr_mapping = trdict[signature]
					worksheet.write('M'+str(startline), tr_mapping)
					
					#to check daily TOP 5 TR enb and gnb
					if hw == "gNB" and kstdate == last_crash_date:
						tr_list_gnb.append(tr_mapping)
					if hw == "eNB" and kstdate == last_crash_date:
						tr_list_enb.append(tr_mapping)
					old_crash+=1
					flag_mapping = 1
					break
				else:
					worksheet.write('M'+str(startline), "New Crash")
					#con thieu cai new crash enb/gnb, lam sao luu vao list	
			#nghia ko map duoc TR nao
			if flag_mapping == 0:
				if hw == "gNB" and kstdate == last_crash_date:
					tr_list_gnb.append("New Crash")
				if hw == "eNB" and kstdate == last_crash_date:
					tr_list_enb.append("New Crash")
					
			#worksheet.write('M'+str(startline), 'TRMapping')
			if "/BS1/" in path  or "/BS2/" in path:
				worksheet.write('N'+str(startline), 'BS')
			if "/DG1/" in path or "/DG2/" in path:
				worksheet.write('N'+str(startline), 'DG')
			if nodename in cdzone:
				worksheet.write('O'+str(startline), 'o')
			
			
			startline+=1
#start DU crash report


total_crash = startline-2
new_crash = total_crash- old_crash
print "Total DU crash: "+ str(total_crash)
print "Total DU NEW crash: "+ str(new_crash)



tr_gnb = removeduplicatedandcount(tr_list_gnb)
tr_enb = removeduplicatedandcount(tr_list_enb)
#print "gNB TR:"
#print tr_gnb
#print "eNB TR:"
#print tr_enb

print "Update sheet TOP5 crash..."
worksheet10 = workbook.add_worksheet("TOP 5 CRASH&AL") 

# Use the worksheet object to write 
# data via the write() method. 
worksheet10.write('A1', '1.TOP5 TR DAILY CRASH') 
worksheet10.write('A2', 'Daily TOP5(gNB)') 
worksheet10.write('B2', 'Count') 
worksheet10.write('C2', 'Daily TOP5(eNB)')
worksheet10.write('D2', 'Count')

lineindex = 3
count5 = 1
print "TOP5 gNB crash on " + str(last_crash_date)+ "(KST): "
for i in tr_gnb:
	if count5 <=5:
		tr = i[0]
		counttr= i[1]
		if tr != "New Crash":
			worksheet10.write('A'+str(lineindex), tr) 
			worksheet10.write('B'+str(lineindex), counttr)
			print count5, tr, counttr
			count5+=1
			lineindex+=1
	

lineindex = 3
count5 = 1
print "TOP5 eNB crash on " + str(last_crash_date)+ "(KST): "
for i in tr_enb:
	if count5 <=5:
		tr = i[0]
		counttr= i[1]
		if tr != "New Crash":
			worksheet10.write('C'+str(lineindex), i[0]) 
			worksheet10.write('D'+str(lineindex), i[1])
			print count5, tr, counttr
			count5+=1
			lineindex+=1
	
#exit()

#start 2.BS_DG_Total_Crash  report
#create worksheet for DU crash
worksheet2 = workbook.add_worksheet("2.BS_DG_Total_Crash") 

# Use the worksheet object to write 
# data via the write() method. 
worksheet2.write('A1', 'Site Name') 
worksheet2.write('B1', 'Date') 
worksheet2.write('C1', 'Time') 
worksheet2.write('D1', 'Date Time(UTC)') 
worksheet2.write('E1', '+09:00') 
worksheet2.write('F1', "Date Time(KST)") 
worksheet2.write('G1', 'Crash HW') 
worksheet2.write('H1', 'UP')
worksheet2.write('I1', '4T4RX')
worksheet2.write('J1', 'Crash Details')
worksheet2.write('K1', '#')
worksheet2.write('L1', 'TRMapping')
worksheet2.write('M1', 'Area')
worksheet2.write('N1', 'CD Zone')

startline = 2
#DU TOTAL CRASH

print "Start update DU TOTAL Crash TAB..."
for path in dufiles:
	print "parsing file " + path + "..."
	lines = [line for line in open(path)]



	for line in lines:	
		#add on 14Jan2020, bug fig
		line = line.decode('utf-8','ignore').encode("utf-8")
		
		#remove new line charactor
		line = line.rstrip()
		
		#line = seogu-buyong-TA9.log:2019-12-18 12:37:45 LLOG  0001 DUS5201     Program restart. Reason: Snapshot request. Program: lratBbomArmLm.bin. PMD: pmd-bbmcBbOmMeThrea-21741-20191218-123745. Extra: BB Restart: Emca 4:DSP 1: "LPP_send to invalid virtual pidnpid: 0x196"
		x = re.split(".log:", line)
		#print(x)
		nodename = x[0]	
		#print nodename
		
		remain1 = x[1]	
		#remain1 = 2019-12-18 12:37:45 LLOG  0001 DUS5201     Program restart. Reason: Snapshot request. Program: lratBbomArmLm.bin. PMD: pmd-bbmcBbOmMeThrea-21741-20191218-123745. Extra: BB Restart: Emca 4:DSP 1: "LPP_send to invalid virtual pidnpid: 0x196"
		
		
		
		#\s: space, split first 2 space
		y = re.split(" LLOG  ", remain1, 2)
		#print y
		
		#y = ['2019-12-18 09:49:31', '0001 DUS5201     Program restart. Reason: Snapshot request. Program: lratBbomArmLm.bin. PMD: pmd-bbmcBbOmMeThrea-15363-20191218-094931. Extra: BB Restart: Emca 4:DSP 1: "LPP_send to invalid virtual pidnpid: 0x18d"']
		utctime = y[0]
		utctime_new = utctime.replace("-", "/",2)
		utctime_new2 = convert_datetime_timezone(utctime,"UTC","UTC")
		
		#split UTC date and time
		#temp = re.split("\s",utctime_new)
		temp = re.split("\s",utctime_new2[1])
		date = temp[0]
		time = temp[1]
		
		#convert timezone to korea time
		#ksttime = convert_datetime_timezone(utctime,"UTC","Asia/Seoul")
		#["%Y/%m/%d %H:%M:%S", "%m/%d/%Y %H:%M:%S"]
		ksttime_new = convert_datetime_timezone(utctime,"UTC","Asia/Seoul")
		kstdaytime = ksttime_new[0]
		
		
		#split to get kst day
		#ksttime = 2019/12/18 13:57:59
		temp = re.split("\s", ksttime_new[1])
		KST_Dalry = temp[0]
		#KST_hhmmss = 13:57:59
		KST_hhmmss = temp[1]
		
		remain2= y[1]
		
		#remain2 = '0001 DUS5201     Program restart. Reason: Snapshot request. Program: lratBbomArmLm.bin. PMD: pmd-bbmcBbOmMeThrea-15363-20191218-094931. Extra: BB Restart: Emca 4:DSP 1: "LPP_send to invalid virtual pidnpid: 0x18d"'
		#print utctime
		#print ksttime
		#print remain2
		
		z = re.split("\s+", remain2, 2)
		#print z
		#z =  ['0001', 'DUS5201', 'Program restart. Reason: Snapshot request. Program: lratBbomArmLm.bin. PMD: pmd-bbmcBbOmMeThrea-15363-20191218-094931. Extra: BB Restart: Emca 4:DSP 1: "LPP_send to invalid virtual pidnpid: 0x18d"']
		
		hw = z[1]
		#hw = DUS5201 or DUS5301
		crash = z[2]
		#crash = Program restart. Reason: Snapshot request. Program: lratBbomArmLm.bin. PMD: pmd-bbmcBbOmMeThrea-15363-20191218-094931. Extra: BB Restart: Emca 4:DSP 1: "LPP_send to invalid virtual pidnpid: 0x18d"
		
		if hw == "DUS5201":
			hw = "eNB"
		if hw == "DUS5301":
			hw = "gNB"
		#print hw
		#print crash
		
		#turn on when need to troublesooting
		#print nodename,"|",utctime, "|", date, "|", time ,"|",kstdaytime,"|", kstday, "|",hw,"|",crash
		report = str(startline-1) + nodename + "|" + utctime +  "|" +  date + "|" + time + "|" + kstdaytime + "|" + KST_Dalry + "|" + hw + "|" + crash
		
		#print report
		#write to text file to count number	
		#file1.write(report+"\r\n")
		#write data to excel file
		
		#remove crash from 00 KST to 05 KST 
		if not re.search("0[012345]:\d\d:\d\d",KST_hhmmss):
		
			worksheet2.write('A'+str(startline), nodename) 
			#worksheet2.write('B'+str(startline), date) 
			#worksheet2.write('C'+str(startline), time) 
			
			date_format = workbook.add_format({'num_format': 'mm/dd/yyyy','align': 'left'})
			utcdate = dt.strptime(date,'%m/%d/%Y')			
			worksheet2.write_datetime('B'+str(startline), utcdate,  date_format) 
				
			date_format = workbook.add_format({'num_format': 'hh:mm:ss','align': 'left'})
			utctime = dt.strptime(time,'%H:%M:%S')			
			#worksheet.write('C'+str(startline), time) 
			worksheet2.write_datetime('C'+str(startline), utctime,  date_format) 
				
			date_format = workbook.add_format({'num_format': 'yyyy/mm/dd hh:mm:ss','align': 'left'})
			utcdatetime = dt.strptime(utctime_new,'%Y/%m/%d %H:%M:%S')			
			worksheet2.write_datetime('D'+str(startline), utcdatetime,  date_format) 		
			#worksheet2.write('D'+str(startline), utctime_new) 		
				
			worksheet2.write('E'+str(startline), '9:00')
				
				
			#worksheet.write('F'+str(startline), kstdaytime) 
			date_format = workbook.add_format({'num_format': 'yyyy/mm/dd hh:mm:ss','align': 'left'})
			kstdatetime = dt.strptime(kstdaytime,'%Y/%m/%d %H:%M:%S')			
			worksheet2.write_datetime('F'+str(startline), kstdatetime,  date_format) 
				
			
			
			
			
			#worksheet2.write('E'+str(startline), '9:00') 
			#worksheet2.write('F'+str(startline), kstdaytime) 		
			worksheet2.write('G'+str(startline), hw) 
			if nodename in swdict.keys():
				if nodename in fourtxlist and swdict[nodename] != "CXP9024418/6_R73E23":
					worksheet2.write('H'+str(startline), swdict[nodename]+"(gNB)")
				else:
					worksheet2.write('H'+str(startline), swdict[nodename])
			if nodename in fourtxlist:
				worksheet2.write('I'+str(startline), '4T4RX')
			
			worksheet2.write('J'+str(startline), crash)
			worksheet2.write('K'+str(startline), '#')
			#worksheet2.write('L'+str(startline), 'TRMapping')
			#TR MAPPING
			for signature in trdict.keys():
				if signature in crash:
					worksheet2.write('L'+str(startline), trdict[signature])
					break
				else:
					worksheet2.write('L'+str(startline), "New Crash")
			
			if "/BS1/" in path  or "/BS2/" in path:
				worksheet2.write('M'+str(startline), 'BS')
			if "/DG1/" in path or "/DG2/" in path:
				worksheet2.write('M'+str(startline), 'DG')
				
			if nodename in cdzone:
				worksheet2.write('N'+str(startline), 'o')
			
			
			startline+=1

#"end of TOTAL DU CRASH 2.BS_DG_Total_Crash report"

#start RU crash report
startline = 2
new_crash_ru = 0
old_crash_ru =0
#rufiles = ['./BS1/crash_RU.log', './BS2/crash_RU.log', './DG1/crash_RU.log', './DG2/crash_RU.log']

#update RU  crash sheet
print "Start update RU Crash TAB..."
for path in rufiles:
	print "parsing file " + path + "..."	
	lines = [line.rstrip() for line in open(path)]
	
		
	for line in lines:	
	
		#remove chactor not utf-8 from string , so that python python excelwriter can work
		
		line = line.decode('utf-8','ignore').encode("utf-8")		
		#UnicodeDecodeError: 'ascii' codec can't decode byte 0xd3 in position 202: ordinal not in range(128)
		#line = line.decode('ascii').strip()
		
		#line = JinjuokbongNX3.log:2019-12-18 13:54:28 LLOG  BXP_2049         Board restart. Reason: Ordered restart. Program: ngr2.elf. Rank: Cold. Extra: Recovery action, faultId: 0x513 (LinearizationFaultPartial), faultDescription: Linearization fault [ DL/B ]
		x = re.split(".log:", line)
		#print(x)
		nodename = x[0]	
		#print nodename
		
		remain1 = x[1]	
		#remain1 = 2019-12-18 13:54:28 LLOG  BXP_2049         Board restart. Reason: Ordered restart. Program: ngr2.elf. Rank: Cold. Extra: Recovery action, faultId: 0x513 (LinearizationFaultPartial), faultDescription: Linearization fault [ DL/B ]
		
						
		y = re.split(" LLOG  ", remain1, 2)
		#print y
		
		#y = ['2019-12-18 13:54:28', 'BXP_2049         Board restart. Reason: Ordered restart. Program: ngr2.elf. Rank: Cold. Extra: Recovery action, faultId: 0x513 (LinearizationFaultPartial), faultDescription: Linearization fault [ DL/B ]']
		utctime = y[0]
		#utctime_new = utctime.replace("-", "/",2)
		utctime_new2 = convert_datetime_timezone(utctime,"UTC","UTC")
		
		#split UTC date and time
		temp = re.split("\s",utctime_new2[1])
		date = temp[0]
		time = temp[1]
		
		#convert timezone to korea time
		ksttime_new = convert_datetime_timezone(utctime,"UTC","Asia/Seoul")
		kstdaytime = ksttime_new[0]
		#split to get kst day
		#ksttime = 2019/12/18 13:57:59
		temp = re.split("\s", ksttime_new[0])
		kstday = temp[0]
		KST_hhmmss = temp[1]
		
		remain2= y[1]
		
		#remain2 = 'BXP_2049         Board restart. Reason: Ordered restart. Program: ngr2.elf. Rank: Cold. Extra: Recovery action, faultId: 0x513 (LinearizationFaultPartial), faultDescription: Linearization fault [ DL/B ]'
		#print utctime
		#print ksttime
		#print remain2
		
		z = re.split("\s+", remain2, 1)
		#print z
		#z =  ['BXP_2049', 'Board restart. Reason: Ordered restart. Program: ngr2.elf. Rank: Cold. Extra: Recovery action, faultId: 0x513 (LinearizationFaultPartial), faultDescription: Linearization fault [ DL/B ]']
		
		hw = z[0]
		#hw = BXP_2049
		crash = z[1]
		#crash = Board restart. Reason: Ordered restart. Program: ngr2.elf. Rank: Cold. Extra: Recovery action, faultId: 0x513 (LinearizationFaultPartial), faultDescription: Linearization fault [ DL/B ]
		
		
		#print hw
		#print crash
		
		#turn on when need troubleshooting
		#print startline-1, nodename,"|",date, "|", time, "|", utctime ,"|",kstdaytime,"|", kstday, "|",hw,"|",crash
		
		#ghi chu ve cai duong ra ngoai me cung
		#utctime_new2[0] = 2019/12/22 00:57:36
		#utctime_new2[1] = 12/22/2019 00:57:36
		report = str(startline-1) + nodename + "|" + date + "|" + time + "|" + utctime_new2[0] + "|" + kstdaytime + "|" + kstday + "|" + hw + "|" + crash
		#print report
		
		#turn on when need to test, using text file for troubleshooting
		#file2.write( report + "\r\n" )
		#write data to excel file
		
		if not re.search("0[012345]:\d\d:\d\d",KST_hhmmss):
			worksheet7.write('A'+str(startline), nodename) 
			
			
			date_format = workbook.add_format({'num_format': 'mm/dd/yyyy','align': 'left'})
			utcdate = dt.strptime(date,'%m/%d/%Y')			
			worksheet7.write_datetime('B'+str(startline), utcdate,  date_format) 
				
			date_format = workbook.add_format({'num_format': 'hh:mm:ss','align': 'left'})
			utctime = dt.strptime(time,'%H:%M:%S')			
			
			worksheet7.write_datetime('C'+str(startline), utctime,  date_format) 

			
			date_format = workbook.add_format({'num_format': 'yyyy/mm/dd hh:mm:ss','align': 'left'})
			utcdatetime = dt.strptime(utctime_new2[0],'%Y/%m/%d %H:%M:%S')			
			worksheet7.write_datetime('D'+str(startline), utcdatetime,  date_format) 				
						
			worksheet7.write('E'+str(startline), '9:00')
			
			date_format = workbook.add_format({'num_format': 'yyyy/mm/dd hh:mm:ss','align': 'left'})
			kstdatetime = dt.strptime(kstdaytime,'%Y/%m/%d %H:%M:%S')			
			worksheet7.write_datetime('F'+str(startline), kstdatetime,  date_format) 
			
			
			worksheet7.write('G'+str(startline), hw) 
			if nodename in swdict.keys():
				if nodename in fourtxlist and swdict[nodename] != "CXP9024418/6_R73E23":
					worksheet7.write('H'+str(startline), swdict[nodename]+"(gNB)")
				else:
					worksheet7.write('H'+str(startline), swdict[nodename])
			
			#this line is very important, cannot remove
			crash = crash.decode("utf-8")		
			worksheet7.write('I'+str(startline), crash)
			worksheet7.write('J'+str(startline), '*')
			#worksheet7.write('K'+str(startline), 'TRMapping')
			#TR MAPPING
			for signature in trdict.keys():
				if signature in crash:
					old_crash_ru += 1
					worksheet7.write('K'+str(startline), trdict[signature])				
					break
				else:
					worksheet7.write('K'+str(startline), "New Crash")
			if nodename in cdzone:
				worksheet7.write('L'+str(startline), 'o')
			
			#increase to write in next line
			startline+=1


total_crash_ru = startline - 2
new_crash_ru = total_crash_ru - old_crash_ru
print "Total RU crash: "+ str(total_crash_ru)

#need to fix
print "Total RU NEW crash: "+ str(new_crash_ru)

#end RU crash report


###########start alarm parse##############
#SiteName	UTC Date	UTC Time	Current_UP	Alarm	Area	4T4RX

worksheet8 = workbook.add_worksheet("3. BS_DG_Alarm")   
worksheet8.write('A1', 'SiteName') 
worksheet8.write('B1', 'UTC Date') 
worksheet8.write('C1', 'UTC Time') 
worksheet8.write('D1', 'Current_UP') 
worksheet8.write('E1', 'Alarm') 
worksheet8.write('F1', 'Area') 
worksheet8.write('G1', '4T4RX') 

startline = 2
alarm_list = []
print "Start update alarm sheet..."
for path in alarmfiles:
	print "parsing file " + path + "..."
	lines = [line for line in open(path)]
	for line in lines:	
		#remove new line charactor
		line = line.rstrip()
		
		#line = dg-dalseo-bolli-TA6$2019-09-23$19:34:03$M Inconsistent Configuration 
		x = re.split("\$", line)
		#print(x)
		#x = ['dg-dalseo-bolli-TA6' , '2019-09-23', '19:34:03', 'M Inconsistent Configuration']
		nodename = x[0]	
		#print nodename
		
		date = x[1]
		time = x[2]
		alarm = x[3]
		if nodename in swdict.keys():
			sw = swdict[nodename]
		
		if "/BS1/" in path  or "/BS2/" in path:
			area = "BS"
		if "/DG1/" in path or "/DG2/" in path:
			area = "DG"
		
		#print nodename,sw
		#report = str(startline-1) + " | " + nodename + " | " + date + " | " + time + " | " + sw + " | " + alarm + " | " + area + " | "
		#print report		
		if  "/6" in sw and nodename in fourtxlist and alarm != "SFP Not Present" and alarm!= "Service Degraded":
			worksheet8.write('A'+str(startline), nodename) 
			worksheet8.write('B'+str(startline), date)
			worksheet8.write('C'+str(startline), time)
			worksheet8.write('D'+str(startline), sw)
			
			worksheet8.write('E'+str(startline), alarm)
			alarm_list.append(alarm)
			worksheet8.write('F'+str(startline), area)
			if nodename in fourtxlist:
				worksheet8.write('G'+str(startline), "4T4RX")
			startline+=1
			
		if not "/6" in sw and alarm != "SFP Not Present" and alarm!= "Service Degraded":
			worksheet8.write('A'+str(startline), nodename) 
			worksheet8.write('B'+str(startline), date)
			worksheet8.write('C'+str(startline), time)
			worksheet8.write('D'+str(startline), sw)
			worksheet8.write('E'+str(startline), alarm)
			alarm_list.append(alarm)
			worksheet8.write('F'+str(startline), area)
			if nodename in fourtxlist:
				worksheet8.write('G'+str(startline), "4T4RX")
			startline+=1
			


###########end alarm parse

print "Total alarm: "+ str(startline -2)
#close text file
#file2.close()
# Finally, close the Excel file 
# via the close() method. 
alarmcount = removeduplicatedandcount(alarm_list)
#print alarmcount

print "TOP5 ALARM"
worksheet10.write('E2', 'Daily TOP5(gNB) ALARM Today')
worksheet10.write('F2', 'Count')
lineindex = 3
count5 = 1

for i in alarmcount:
	if count5 <=5:		
		worksheet10.write('E'+str(lineindex), i[0]) 
		worksheet10.write('F'+str(lineindex), i[1])
		print count5, i[0], i[1]
		count5+=1
		lineindex+=1

print "Saving result to excel file..."
workbook.close()