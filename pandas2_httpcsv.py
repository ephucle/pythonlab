#!/usr/bin/env python

#https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
import pandas as pd
import random
 
# read the data from the downloaded CSV file.
data = pd.read_csv('https://s3-eu-west-1.amazonaws.com/shanebucket/downloads/uk-500.csv')
# set a numeric id for use as an index for examples.
data['id'] = [random.randint(0,1000) for x in range(data.shape[0])]

print("HEAD5")
print(data.head(5))
print("TAIL5")
print(data.tail(5))

print("columns:")
print(data.columns) 

print("index:")
print(data.index) 

print("# Single selections using iloc and DataFrame")
# Rows:
print("First row \n",data.iloc[0]) # first row of data frame (Aleshia Tomkiewicz) - Note a Series data type output.
print("Second row \n",data.iloc[1]) # second row of data frame (Evan Zigomalas)
print("Last row \n", data.iloc[-1]) # last row of data frame (Mi Richan)
print("Second Last row \n", data.iloc[-2]) # 


print("# Multiple row and column selections using iloc and DataFrame)--------------")
print("First 03 row by data.iloc[0:3] ", data.iloc[0:3]) # first five rows of dataframe


print(data.loc[data['email'].str.endswith("hotmail.com")])
#    first_name   last_name                    company_name                 address  ...        phone2                       email                                          web   id
#0      Aleshia  Tomkiewicz         Alan D Rosenburg Cpa Pc            14 Taylor St  ...  01944-369967     atomkiewicz@hotmail.com         http://www.alandrosenburgcpapc.co.uk  322
#2       France     Andrade             Elliott, John W Esq            8 Moor Place  ...  01935-821636  france.andrade@hotmail.com             http://www.elliottjohnwesq.co.uk  720
#3      Ulysses   Mcwalters                  Mcmahan, Ben L           505 Exeter Rd  ...  01302-601380         ulysses@hotmail.com                 http://www.mcmahanbenl.co.uk  681
#4       Tyisha      Veness                  Champagne Room       5396 Forth Street  ...  01290-367248   tyisha.veness@hotmail.com               http://www.champagneroom.co.uk  596
#6         Marg    Grasmick   Wrangle Hill Auto Auct & Slvg        7457 Cowl St #70  ...  01362-620532            marg@hotmail.com     http://www.wranglehillautoauctslvg.co.uk  780
#..         ...         ...                             ...                     ...  ...           ...                         ...                                          ...  ...
#486     Sophia     Gaucher               T C E Systems Inc  88 Upper Harrington St  ...  01254-919378  sophia.gaucher@hotmail.com               http://www.tcesystemsinc.co.uk  312
#490     Rosita   Ausdemore               Jurdem, Scott Esq    8 Heathfield St #657  ...  01997-765432      rausdemore@hotmail.com              http://www.jurdemscottesq.co.uk  519
#491       Huey     Stancil                   Lindner Funds             275 Peel Sq  ...  01468-195646        hstancil@hotmail.com                http://www.lindnerfunds.co.uk  547
#492     Elbert     Fiorino            Donald, G Nelson Esq  726 Westmoreland Place  ...  01992-537553          elbert@hotmail.com            http://www.donaldgnelsonesq.co.uk  880
#499         Mi      Richan  Nelson Wright Haworth Golf Crs         6 Norwood Grove  ...  01202-738406              mi@hotmail.com  http://www.nelsonwrighthaworthgolfcrs.co.uk  957



print(data.loc[data['first_name'] == 'Aleshia'])
#  first_name   last_name             company_name       address               city  ...        phone1        phone2                    email                                   web   id
#0    Aleshia  Tomkiewicz  Alan D Rosenburg Cpa Pc  14 Taylor St  St. Stephens Ward  ...  01835-703597  01944-369967  atomkiewicz@hotmail.com  http://www.alandrosenburgcpapc.co.uk  322

print(data.loc[data['first_name'].isin(['France', 'Tyisha', 'Eric'])])

# Select rows with first name Antonio AND hotmail email addresses
print(data.loc[data['email'].str.endswith("gmail.com") & (data['first_name'] == 'Antonio')] )


# select rows with id column between 100 and 200, and just return 'postal' and 'web' columns
print(data.loc[(data['id'] > 100) & (data['id'] <= 200), ['postal', 'web']] )


# A lambda function that yields True/False values can also be used.
# Select rows where the company name has 4 words in it.
print(data.loc[data['company_name'].apply(lambda x: len(x.split(' ')) == 4)] )
