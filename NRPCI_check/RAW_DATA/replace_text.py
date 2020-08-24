import pandas as pd
with open('0818_ENM_BS1_ExternalGUtrancell_new.csv', 'w') as outfile:
	with open('0818_ENM_BS1_ExternalGUtrancell.csv') as infile:
		lines = infile.readlines()
		for line in lines:
			outfile.write(line.replace('SubNetwork,ManagedElement,ENodeBFunction,GUtraNetwork,ExternalGNodeBFunction,ExternalGUtranCell', ""))
			
with open('0818_ENM_BS2_ExternalGUtrancell_new.csv', 'w') as outfile:
	with open('0818_ENM_BS2_ExternalGUtrancell.csv') as infile:
		lines = infile.readlines()
		for line in lines:
			outfile.write(line.replace('SubNetwork,ManagedElement,ENodeBFunction,GUtraNetwork,ExternalGNodeBFunction,ExternalGUtranCell', ""))

#df =pd.read_csv('0818_ENM_BS1_ExternalGUtrancell_new.csv', sep ="\t",low_memory=False)
#print(df)

df2 =pd.read_csv('0818_ENM_BS2_ExternalGUtrancell_new.csv', sep ="\t",low_memory=False)
print(df2)

