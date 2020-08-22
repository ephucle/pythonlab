#!/usr/bin/env python3.6

#import tkinter as tk
from tkinter import Tk, Button, Text, filedialog, W, END
import pandas as pd
import numpy as np
import glob
import datetime
import sys, os , platform
from pathlib import Path
root = Tk()
root.title("NRPCI duplicated check")
width  = 600
height = 285
root.geometry(f'{width}x{height}')

def browse_button():
	global root_path
	global BS1_ExternalGUtrancecell_File
	global BS2_ExternalGUtrancecell_File
	global BS2_gNBID_file
	global BS2_NRPCI_file
	
	root_path = filedialog.askdirectory()
	print("root_path in linux format: ", root_path)
	
	#https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
	root_path = Path(root_path)
	
	print("root_path window",root_path)
	
	
	#update dcgm_paths_listbox
	global ExternalGUtrancell_filepaths
	ExternalGUtrancell_filepaths = [ os.path.join(root_path,file) for file in os.listdir(root_path) if os.path.isfile(os.path.join(root_path, file)) and "ExternalGUtrancell" in file]
	
	BS1_ExternalGUtrancecell_File = ExternalGUtrancell_filepaths[0]
	BS2_ExternalGUtrancecell_File = ExternalGUtrancell_filepaths[1]
	
	
	BS2_gNBID_file = [ os.path.join(root_path,file) for file in os.listdir(root_path) if os.path.isfile(os.path.join(root_path, file)) and "gNBID" in file][0]
	
	BS2_NRPCI_file = [ os.path.join(root_path,file) for file in os.listdir(root_path) if os.path.isfile(os.path.join(root_path, file)) and "ENM_BS2_NRPCI" in file][0]
	
	print("ExternalGUtrancell_filepaths", ExternalGUtrancell_filepaths)
	print("BS2_gNBID_file", BS2_gNBID_file)
	print("BS2_NRPCI_file", BS2_NRPCI_file)
	print_to_textbox("ExternalGUtrancell_filepaths: " + str(ExternalGUtrancell_filepaths))
	print_to_textbox("BS2_gNBID_file: " + BS2_gNBID_file)
	print_to_textbox("BS2_NRPCI_file: " + BS2_NRPCI_file)
	print_to_textbox("-"*10)
	
	
	
def print_to_textbox(text_string):
	#main_textbox.insert(tk.END, text_string + "\n")
	main_textbox.insert(END, text_string + "\n")
	root.update_idletasks()

def check_NRPCI():
	global BS1_ExternalGUtrancecell_File
	global BS2_ExternalGUtrancecell_File
	global BS2_gNBID_file
	global BS2_NRPCI_file
	#print("button button_check_NRPCI is pressed ")
	
	print_to_textbox("Processing CSV file to find duplicated NRPCI...")
	root.update_idletasks()
	print_to_textbox("It will take some minute to finish, pls wait!!!")
	root.update_idletasks()
	
	df = pd.read_csv(BS1_ExternalGUtrancecell_File,sep ="\t",low_memory=False)
	df2 = pd.read_csv(BS2_ExternalGUtrancecell_File,sep ="\t",low_memory=False)
	df3 = pd.read_csv(BS2_gNBID_file,sep ="\t",low_memory=False)
	df4 = pd.read_csv(BS2_NRPCI_file,sep ="\t",low_memory=False)

	
	#while ExternalGUtrancecell_lists[:]:
	#allfile_list = glob.glob(os.path.join("*External*"))
	
	allfile_list = ExternalGUtrancell_filepaths
	
	allData = []
	for file in allfile_list :
		df_MM = pd.read_csv(file)
		allData.append(df_MM)
	
	
	#print(allData)

	DataCombine = pd.concat(allData, axis=0, ignore_index=False)
	
	DataCombine.to_csv(os.path.join(root_path,"DataCombine.csv"),index=False)
	del DataCombine # to save memory
	
	DataCombine_read = pd.read_csv(os.path.join(root_path,"DataCombine.csv"),sep='\t',low_memory=False)
	
	#print(DataCombine_read)
	
	#remove temp file
	os.remove(os.path.join(root_path,"DataCombine.csv"))
	
	
	
	##Create new column for getting NRPCI on eNB Terms
	DataCombine_read['NRPCI_on_eNB'] = 3*DataCombine_read['physicalLayerCellIdGroup'] + DataCombine_read['physicalLayerSubCellId']
	
	DataCombine_read['Object_NRPCI_on_eNB'] = DataCombine_read['NRPCI_on_eNB'].astype(str)
	
	##Create new column for sorting by words by Hoang
	DataCombine_read['NodeId_lower'] = DataCombine_read['NodeId'].str.lower()
	
	##sort by nodeid first, if nodeid is the same, it wil continue sort by NRPCI_on_eNB by Hoang
	DataCombine_read = DataCombine_read.sort_values(by=['NodeId_lower','NRPCI_on_eNB'], ascending=True, axis=0)
	
	
	##Merge(Like as VLOOKUP on EXCEL) for merging gNBID and NRPCI from BS2
	VLOOKUP = pd.merge(df3,df4,how='left',on='NodeId')
	
	
	##nRPCI type change from "int" to "Object" for adding NodeID and nRPCI
	VLOOKUP['Object_nRPCI'] = VLOOKUP['nRPCI'].astype(str)
	#print(VLOOKUP['Object_nRPCI'])
	
	VLOOKUP['Add_NodeID_n_Object_nRPCI'] = VLOOKUP['NodeId']+VLOOKUP['Object_nRPCI']
	#print(VLOOKUP['Add_NodeID_n_Object_nRPCI'])
	
	
	####Create new "gNBId" colunm for vlookup
	DataCombine_read['gNBId'] = DataCombine_read['ExternalGNodeBFunctionId']
	DataCombine_read
	
	##Import gNBID
	DataCombine_read_VLookup = pd.merge(DataCombine_read,df3,how='left', on='gNBId')
	DataCombine_read_VLookup
	
	del DataCombine_read  #del variable due to no use, to save memory
	
	DataCombine_read_VLookup['Concat_gNBID_Object_NRPCI_on_eNB'] = DataCombine_read_VLookup['NodeId_y']+DataCombine_read_VLookup['Object_NRPCI_on_eNB']
	DataCombine_read_VLookup
	
	DataCombine_read_VLookup['Add_NodeID_n_Object_nRPCI'] = DataCombine_read_VLookup['Concat_gNBID_Object_NRPCI_on_eNB']
	DataCombine_read_VLookup
	
	LAST_DataCombine_read_VLookup = pd.merge(DataCombine_read_VLookup,VLOOKUP,how='left', on='Add_NodeID_n_Object_nRPCI')
	LAST_DataCombine_read_VLookup
	
	
	##Select only duplicate date, expect dummpies
	Final_result_of_Dup_NR_PCI = LAST_DataCombine_read_VLookup[['NodeId_x','ExternalGNodeBFunctionId','Object_NRPCI_on_eNB','NodeId','NRCellDUId','Object_nRPCI']].copy()
	Final_result_of_Dup_NR_PCI
	
	del LAST_DataCombine_read_VLookup #del variable due to no use, to save memory
	
	#print("Fill nan value of Object_nRPCI by string 'nan' ")
	#print(Final_result_of_Dup_NR_PCI['Object_nRPCI'].isnull().values.any())  #True
	#count duplicated
	#print(Final_result_of_Dup_NR_PCI['Object_nRPCI'].isnull().sum()) #10876, from excel have 10876 empty cell
	Final_result_of_Dup_NR_PCI['Object_nRPCI'] = Final_result_of_Dup_NR_PCI['Object_nRPCI'].dropna(axis=0)
	Final_result_of_Dup_NR_PCI
	
	Final_result_of_Dup_NR_PCI['NodeId'] = Final_result_of_Dup_NR_PCI['NodeId'].dropna(axis=0)
	Final_result_of_Dup_NR_PCI
	
	Final_result_of_Dup_NR_PCI['NRCellDUId'] = Final_result_of_Dup_NR_PCI['NRCellDUId'].dropna(axis=0)
	Final_result_of_Dup_NR_PCI
	

	
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
	
	timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
	output_filename = "check_duplicated_result_"+timestamp+".xlsx"
	output_filepath  = os.path.join(root_path, output_filename)
	Final_result_of_Dup_NR_PCI.to_excel(output_filepath,index=False)
	
	
	print("Successful saved output file to",output_filepath )
	print_to_textbox("Successful saved output file to "+output_filepath )
	
	
	
root_path = os.path.expanduser('~')
default_padx = 5
width_entry = 70

button = Button(root,text = "Select csv data folder",command=browse_button).grid(row=0, column=0,sticky=W, padx = default_padx)

main_textbox = Text(root, font=("Calibri 12"), height=10, width= width_entry)
main_textbox.grid(row=1, column=0, sticky=W, padx = default_padx ,pady =5)

button_check_NRPCI = Button(root,text = "Check Duplicated NRPCI",command=check_NRPCI).grid(row=2, column=0,sticky=W, padx = default_padx)
button_quit = Button(root,text = "Quit", command=quit).grid(row=3, column=0, sticky=W, padx = default_padx)

root.mainloop()
