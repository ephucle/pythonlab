#!/usr/bin/env python3

#!/usr/bin/env python3

import pandas as pd
import numpy as np
import glob
import sys
import tkinter
import os
import os.path
from datetime import datetime
from sys import argv

#os.system("pause")
time_now = datetime.now()

##Current_dir
file_dir = os.getcwd()

#print(time_now.date()+str('_')+str('Today'))

BS1_ExternalGUtrancecell_File = input("Please add ExternalGUtrancell csv file from BS1_ENM: ")
BS2_ExternalGUtrancecell_File = input("Please add ExternalGUtrancell csv file from BS2_ENM: ")
BS2_gNBID_file = input("Please add gNBID csv file from BS2_ENM: ")
BS2_NRPCI_file = input("Please add NRPCI csv file from BS2_ENM: ")
Result_file_Name = input("Please input Result file Name(*.csv format): ")

#CSV_format_reqeust_file_name = Result_file_Name+".csv"

if os.path.isfile(BS1_ExternalGUtrancecell_File):
    print(BS1_ExternalGUtrancecell_File+" is Ok")
else:
    print("[ERROR!!] "+BS1_ExternalGUtrancecell_File+" does not exist current folder!!")
    BS1_ExternalGUtrancecell_File = input("Please add ExternalGUtrancell csv file from BS1_ENM: ")

if os.path.isfile(BS2_ExternalGUtrancecell_File):
    print(BS2_ExternalGUtrancecell_File+" is OK")
else:
    print("[ERROR!!] "+BS2_ExternalGUtrancecell_File+" does not exist current folder!!")
    BS2_ExternalGUtrancecell_File = input("Please add ExternalGUtrancell csv file from BS2_ENM: ")

if os.path.isfile(BS2_gNBID_file):
    print(BS2_gNBID_file+" is Ok")
else:
    print("[ERROR!!] "+BS2_gNBID_file+" does not exist current folder!!")
    BS2_gNBID_file = input("Please add gNBID csv file from BS2_ENM: ")


if os.path.isfile(BS2_NRPCI_file):
    print(BS2_gNBID_file+" is OK")
else:
    print("[ERROR!!] "+BS2_gNBID_file+" does not exist current folder!!")
    BS2_NRPCI_file = input("Please add NRPCI csv file from BS2_ENM: ")

#df = pd.read_csv("RV_0818_ENM_BS1_ExternalGUtrancell_PA100.csv",sep ="\t",low_memory=False)
df = pd.read_csv(BS1_ExternalGUtrancecell_File,sep ="\t",low_memory=False)
df2 = pd.read_csv(BS2_ExternalGUtrancecell_File,sep ="\t",low_memory=False)
#df2 = pd.read_csv("RV_0818_ENM_BS2_ExternalGUtrancell_PA1.csv",sep ="\t",low_memory=False)
df3 = pd.read_csv(BS2_gNBID_file,sep ="\t",low_memory=False)
#df3 = pd.read_csv("RV_0818_ENM_BS2_gNBID_PA1.csv",sep ="\t",low_memory=False)
df4 = pd.read_csv(BS2_NRPCI_file,sep ="\t",low_memory=False)

##ExternalGUtrancecell File list
#ExternalGUtrancecell_lists = [BS1_ExternalGUtrancecell_File,BS2_ExternalGUtrancecell_File]

#BS1_ExternalGUtrancecell_File = sys.argv[1]


#print(ExternalGUtrancecell_lists)

#new_array = bytearray[BS1_ExternalGUtrancecell_File,BS2_ExternalGUtrancecell_File]

#print(new_array)
##Create new file for getting

#while ExternalGUtrancecell_lists[:]:
allfile_list = glob.glob(os.path.join("*External*"))

#print(allfile_list)

#print(allfile_list)
allData = []
for file in allfile_list :
    df_MM = pd.read_csv(file)
    allData.append(df_MM)

DataCombine = pd.concat(allData, axis=0, ignore_index=False)

DataCombine.to_csv("DataCombine.csv",index=False)

DataCombine_read = pd.read_csv("DataCombine.csv",sep='\t',low_memory=False)

##Create new column for getting NRPCI on eNB Terms
DataCombine_read['NRPCI_on_eNB'] = 3*DataCombine_read['physicalLayerCellIdGroup'] + DataCombine_read['physicalLayerSubCellId']
DataCombine_read

DataCombine_read['Object_NRPCI_on_eNB'] = DataCombine_read['NRPCI_on_eNB'].astype(str)

##Create new column for sorting by words by Hoang
DataCombine_read['NodeId_lower'] = DataCombine_read['NodeId'].str.lower()

##sort by nodeid first, if nodeid is the same, it wil continue sort by NRPCI_on_eNB by Hoang
DataCombine_read = DataCombine_read.sort_values(by=['NodeId_lower','NRPCI_on_eNB'], ascending=True, axis=0)
DataCombine_read

##Merge(Like as VLOOKUP on EXCEL) for merging gNBID and NRPCI from BS2
VLOOKUP = pd.merge(df3,df4,how='left',on='NodeId')
VLOOKUP

##nRPCI type change from "int" to "Object" for adding NodeID and nRPCI
VLOOKUP['Object_nRPCI'] = VLOOKUP['nRPCI'].astype(str)
#print(VLOOKUP['Object_nRPCI'])

VLOOKUP['Add_NodeID_n_Object_nRPCI'] = VLOOKUP['NodeId']+VLOOKUP['Object_nRPCI']
#print(VLOOKUP['Add_NodeID_n_Object_nRPCI'])
VLOOKUP

####Create new "gNBId" colunm for vlookup
DataCombine_read['gNBId'] = DataCombine_read['ExternalGNodeBFunctionId']
DataCombine_read

##Import gNBID
DataCombine_read_VLookup = pd.merge(DataCombine_read,df3,how='left', on='gNBId')
DataCombine_read_VLookup

DataCombine_read_VLookup['Concat_gNBID_Object_NRPCI_on_eNB'] = DataCombine_read_VLookup['NodeId_y']+DataCombine_read_VLookup['Object_NRPCI_on_eNB']
DataCombine_read_VLookup

DataCombine_read_VLookup['Add_NodeID_n_Object_nRPCI'] = DataCombine_read_VLookup['Concat_gNBID_Object_NRPCI_on_eNB']
DataCombine_read_VLookup

LAST_DataCombine_read_VLookup = pd.merge(DataCombine_read_VLookup,VLOOKUP,how='left', on='Add_NodeID_n_Object_nRPCI')
LAST_DataCombine_read_VLookup

#LAST_DataCombine_read_VLookup['Is duplicated?'] = LAST_DataCombine_read_VLookup.duplicated(['Object_nRPCI'], keep="last")
#LAST_DataCombine_read_VLookup


#for i in LAST_DataCombine_read_VLookup['Object_nRPCI']:
#    if LAST_DataCombine_read_VLookup.iloc[i]['Object_nRPCI'] == LAST_DataCombine_read_VLookup.iloc[i]:
#        LAST_DataCombine_read_VLookup['Is duplicated?'] = "True"
#        print("Fin")
#    elif LAST_DataCombine_read_VLookup.iloc[i+1]['Object_nRPCI'] == LAST_DataCombine_read_VLookup.iloc[i]['Object_nRPCI']:
#        LAST_DataCombine_read_VLookup['Is duplicated?'] = "True"
#        print("FIn2")


##Select only duplicate date, expect dummpies
Final_result_of_Dup_NR_PCI = LAST_DataCombine_read_VLookup[['NodeId_x','ExternalGNodeBFunctionId','Object_NRPCI_on_eNB','NodeId','NRCellDUId','Object_nRPCI']].copy()
Final_result_of_Dup_NR_PCI

#fill na for empty Object_nRPCI
#check if have NAN cell in Object_nRPCI

print("Fill nan value of Object_nRPCI by string 'nan' ")
print(Final_result_of_Dup_NR_PCI['Object_nRPCI'].isnull().values.any())  #True
#count duplicated
print(Final_result_of_Dup_NR_PCI['Object_nRPCI'].isnull().sum()) #10876, from excel have 10876 empty cell
Final_result_of_Dup_NR_PCI['Object_nRPCI'] = Final_result_of_Dup_NR_PCI['Object_nRPCI'].dropna(axis=0)
Final_result_of_Dup_NR_PCI

Final_result_of_Dup_NR_PCI['NodeId'] = Final_result_of_Dup_NR_PCI['NodeId'].dropna(axis=0)
Final_result_of_Dup_NR_PCI

Final_result_of_Dup_NR_PCI['NRCellDUId'] = Final_result_of_Dup_NR_PCI['NRCellDUId'].dropna(axis=0)
Final_result_of_Dup_NR_PCI

#sys.exit()

Final_result_of_Dup_NR_PCI['Object_nRPCI_shift1'] = Final_result_of_Dup_NR_PCI['Object_nRPCI']
Final_result_of_Dup_NR_PCI.Object_nRPCI_shift1 = Final_result_of_Dup_NR_PCI.Object_nRPCI_shift1.shift(1)
Final_result_of_Dup_NR_PCI['Check_DUPLICATED1'] = np.where(Final_result_of_Dup_NR_PCI['Object_nRPCI']==Final_result_of_Dup_NR_PCI['Object_nRPCI_shift1'], 1, 0)


Final_result_of_Dup_NR_PCI['Object_nRPCI_shift_minus1'] = Final_result_of_Dup_NR_PCI['Object_nRPCI']
Final_result_of_Dup_NR_PCI.Object_nRPCI_shift_minus1 = Final_result_of_Dup_NR_PCI.Object_nRPCI_shift_minus1.shift(-1)
Final_result_of_Dup_NR_PCI['Check_DUPLICATED2'] = np.where(Final_result_of_Dup_NR_PCI['Object_nRPCI']==Final_result_of_Dup_NR_PCI['Object_nRPCI_shift_minus1'], 1, 0)


Final_result_of_Dup_NR_PCI['Check_DUPLICATED3'] = Final_result_of_Dup_NR_PCI['Check_DUPLICATED1'] + Final_result_of_Dup_NR_PCI['Check_DUPLICATED2']

Final_result_of_Dup_NR_PCI['Is Duplicated?'] = np.where(Final_result_of_Dup_NR_PCI['Check_DUPLICATED3'] > 0 , "yes", "no")

#remove temp column
del Final_result_of_Dup_NR_PCI['Object_nRPCI_shift1']
del Final_result_of_Dup_NR_PCI['Object_nRPCI_shift_minus1']
del Final_result_of_Dup_NR_PCI['Check_DUPLICATED1']
del Final_result_of_Dup_NR_PCI['Check_DUPLICATED2']
del Final_result_of_Dup_NR_PCI['Check_DUPLICATED3']

Final_result_of_Dup_NR_PCI.to_csv(Result_file_Name,index=False)

print(str(time_now.month)+"_"+str(time_now.day)+"_"+str(time_now.hour)+"_"+Result_file_Name+" is success!")
print("File save directory is: " + os.getcwd())

os.system("pause")