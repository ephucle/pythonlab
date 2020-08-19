import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("BS2_ENM_2_External_CSV2.csv",sep ="\t",low_memory=False)

print(df.columns)
print(df['NodeId'])


df['NRPCI_PA2'] = 3*df['physicalLayerCellIdGroup']+ df['physicalLayerSubCellId']


print (df)