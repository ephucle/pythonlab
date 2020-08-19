#test read csv file by pandas

import pandas as pd
import matplotlib.pyplot as plt

#df = pd.read_csv("/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab/swmapping.csv",low_memory=False)
df = pd.read_csv("/mnt/c/cygwin/home/ephucle/tool_script/python/tr_tool/swmapping.txt",sep = "\t",low_memory=False)

print(df)
print(df.describe())

print("Column name:\n", "\n".join(list(df.columns)))
