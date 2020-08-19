import pandas as pd
import csv
import matplotlib.pyplot as plt
def remove_comma(x):
    return x.replace(',', '')

data = pd.read_csv("C:/000.Field/0000.Dup_PCI/0817/BS2_ENM_2_External_CSV.csv",sep='\n',low_memory=False)
#data.to_excel("C:/000.Field/0000.Dup_PCI/0817/ExternalGUtrancell_PA33.xlsx",index=False)
#data_sample = pd.read_excel("C:/000.Field/0000.Dup_PCI/0817/ExternalGUtrancell_PA33.xlsx")

#print(data.dtypes)

#data = ["SubNetwork,ManagedElement,ENodeBFunction,GUtraNetwork,ExternalGNodeBFunction,ExternalGUtranCell"]

data_sample_Dup_Del = data.drop_duplicates()

data_sample_Dup_Del = data_sample_Dup_Del.drop(data_sample_Dup_Del.index[0])

data_sample_Dup_Del.to_csv("C:/000.Field/0000.Dup_PCI/0817/0817_DUp_ENM1_ExternalGUtrancell_PA12.csv",index=False)

#data_sample_Dup_Del_read = csv.reader(data)

#parsed_csv_data_sample_Dup_Del_read = list(data_sample_Dup_Del_read)

#parsed_csv_data_sample_Dup_Del_read_DF = pd.DataFrame(parsed_csv_data_sample_Dup_Del_read)

#parsed_csv_data_sample_Dup_Del_read_DF_Dup_Del = parsed_csv_data_sample_Dup_Del_read_DF.drop_duplicates()



#split_ata_sample_Dup_Del = data_sample_Dup_Del.str.split()

#split_ata_sample_Dup_Del.to_excel("C:/000.Field/0000.Dup_PCI/0817/0817_DUp_ENM1_ExternalGUtrancell_PA99.xlsx",index=False)

#data_del_first_Del = data_sample_Dup_Del.dropna()
#data_del_first_Del.isnull().sum()
#data_sample_Dup_Del.to_excel("C:/000.Field/0000.Dup_PCI/0817/ExternalGUtrancell_Dup_Del_PA100.xlsx",index=False)

#data_del_first_raw = data_sample_Dup_Del.dropna(inplace=True)
#data_del_first_raw.to_excel("C:/000.Field/0000.Dup_PCI/0817/ExternalGUtrancell_Dup_Del_First_PA100.xlsx",index=False)

#data_del_first_Del = data_sample_Dup_Del.drop(data_sample_Dup_Del.index[0:1])

#data_del_first_Del = data_sample_Dup_Del.drop(data_sample_Dup_Del.index=["SubNetwork"])
#data_sample_Dup_Del.to_excel("C:/000.Field/0000.Dup_PCI/0817/ExternalGUtrancell_Del_PAAA1.xlsx",index=False)

#data_sample_Del.to_excel("C:/000.Field/0000.Dup_PCI/0817/ExternalGUtrancell_DEL_PA99.xlsx",index=False)

#data_sample_DEL = data_sample.drop(data_sample.index[1])

#data_sample_DEL.to_excel("C:/000.Field/0000.Dup_PCI/0817/ExternalGUtrancell_PA99.xlsx")

#data_sample_Del.to_excel("C:/000.Field/0000.Dup_PCI/0817/ExternalGUtrancell_Del_PA34.xlsx",index=False)

#print(data.index[0:],axis=0,inplace=True)
#Raw_0 = data.loc[0]

#print(data.loc[0])

#data_sample = data.drop(data.loc[0])

#print(data_sample)

#data_sample = data.drop(["SubNetwork,ManagedElement,ENodeBFunction,GUtraNetwork,ExternalGNodeBFunction,ExternalGUtranCell"],axis=0)

#Raw_0 = data.loc[0]

#print(Raw_0)



#print(data_sample)

#data_sample.to_excel("C:/000.Field/0000.Dup_PCI/0817/ExternalGUtrancell_PA22.xlsx",index=False)