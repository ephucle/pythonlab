#!/usr/bin/env python3
from covid import Covid
#from plyer import notification
import pandas as pd
from myfunc import Timer
t =Timer() 
t.start()

import sys

#covid = Covid()
print("Source from https://www.worldometers.info/coronavirus/#countries")
covid = Covid(source="worldometers")  #https://www.worldometers.info/coronavirus/#countries



covid.get_data()

total_active_cases = covid.get_total_active_cases()
total_confirmed_cases = covid.get_total_confirmed_cases()
total_deaths= covid.get_total_deaths()
total_recovered = covid.get_total_recovered()


#print allign , https://stackoverflow.com/questions/8234445/format-output-string-right-alignment
print( f'{"Total number of active cases":<40}  {total_active_cases:<12}' )
print( f'{"Total number of confirmed cases":<40}  {total_confirmed_cases:<12}' )
print( f'{"Total deaths":<40}  {total_deaths:<12}' )
print( f'{"Total recovered":<40}  {total_recovered:<12}' )

#Total number of active cases              7733778
#Total number of confirmed cases           35398976
#Total deaths                              1041823
#Total recovered                           26623375


print("\n")
def fetch_covid_by_country_name(country_name):
	#print("*"*30)
	data_dict = covid.get_status_by_country_name(country_name)
	#print(data_dict, type(data_dict))
	#for key in data_dict:
	#	print(f'{key:<40} {data_dict[key]:<12}')
	
	
	series = pd.Series(data_dict, name = country_name)  #https://www.geeksforgeeks.org/creating-a-pandas-series-from-dictionary/
	
	#print (series)
	return series
	
#columns = ['country','confirmed', 'new_cases', 'deaths', 'recovered', 'active', 'critical', 'new_deaths', 'total_tests', 'total_tests_per_million', 'total_cases_per_million', 'total_deaths_per_million', 'population' ]

s1 = fetch_covid_by_country_name("vietnam")
print("Vietnam Covid Data:")
print(s1)
#Vietnam Covid Data:
#country                      Vietnam
#confirmed                       1096
#new_cases                          0
#deaths                            35
#recovered                       1020
#active                            41
#critical                           0
#new_deaths                         0
#total_tests                  1009145
#total_tests_per_million            0
#total_cases_per_million           11
#total_deaths_per_million         0.4
#population                  97566509


#s2 = fetch_covid_by_country_name("usa")
#s3 = fetch_covid_by_country_name("india")
#s4 = fetch_covid_by_country_name("brazil")
#s5 = fetch_covid_by_country_name("philippines")

countries = covid.list_countries()

df = pd.DataFrame()
for country in countries:
	serie = fetch_covid_by_country_name(country)
	df= pd.concat([df,pd.DataFrame(serie)], axis=1)




df = df.T
df = df.iloc[1:]  #remove first row
#print(df)
import datetime

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("--------------TOP 15, confirmed------------")
df= df.sort_values(by=['confirmed'], ascending=False)
print(df.head(15))
print("------------------------------------------\n")

print("--------------TOP 15, confirmed------------")
df= df.sort_values(by=['new_cases'], ascending=False)
print(df.head(15))
print("------------------------------------------\n")


print("--------------TOP 15, confirmed------------")
df= df.sort_values(by=['deaths'], ascending=False)
print(df.head(15))
print("------------------------------------------\n")

print("--------------TOP 15, recovered------------")
df= df.sort_values(by=['recovered'], ascending=False)
print(df.head(15))
print("------------------------------------------\n")

print("--------------TOP 15, active------------")
df= df.sort_values(by=['active'], ascending=False)
print(df.head(15))
print("------------------------------------------\n")

print("--------------TOP 15, critical------------")
df= df.sort_values(by=['critical'], ascending=False)
print(df.head(15))
print("------------------------------------------\n")

print("--------------TOP 15, new_deaths------------")
df= df.sort_values(by=['new_deaths'], ascending=False)
print(df.head(15))
print("------------------------------------------\n")



t.stop()


'''
sample printout
Vietnam Covid Data:
country                      Vietnam
confirmed                       1096
new_cases                          0
deaths                            35
recovered                       1020
active                            41
critical                           0
new_deaths                         0
total_tests                  1009145
total_tests_per_million            0
total_cases_per_million           11
total_deaths_per_million         0.4
population                  97566509
Name: vietnam, dtype: object
2020-10-05 17:24:06
--------------TOP 15, confirmed------------
                     country confirmed new_cases   deaths recovered   active critical new_deaths total_tests total_tests_per_million total_cases_per_million total_deaths_per_million  population
world                  World  35437409     47298  1042343  26645311  7749755    66506        794           0                       0                    4546                    133.7           0
asia                    Asia  11102904     16975   201762   9387391  1513751    20772        258           0                       0                       0                        0           0
south america  South America   8287914       299   261464   7142208   884242    17446         28           0                       0                       0                        0           0
usa                      USA   7637066       154   214615   4849454  2572997    14198          4   111471522                       0                   23037                      647   331510437
india                  India   6626291      4111   102746   5586703   936842     8944         32    79982394                       0                    4789                       74  1383530375
europe                Europe   5361834     25191   225329   2890100  2246405     9139        270           0                       0                       0                        0           0
brazil                Brazil   4915289         0   146375   4263208   505706     8318          0    17900000                       0                   23081                      687   212953890
africa                Africa   1522974        46    36569   1260456   225949     1632          0           0                       0                       0                        0           0
russia                Russia   1225889     10888    21475    982324   222090     2300        117    48042343                       0                    8399                      147   145950977
colombia            Colombia    855052         0    26712    761674    66666     2220          0     3894289                       0                   16758                      524    51023638
peru                    Peru    828169         0    32742    706223    89204     1287          0     3952298                       0                   25027                      989    33090379
spain                  Spain    810807         0    32086         0        0     1566          0    12723989                       0                   17340                      686    46759558
argentina          Argentina    798486         0    21018    636672   140796     3950          0     2064250                       0                   17625                      464    45303674
mexico                Mexico    761665      3712    79088    550053   132524     2401        208     2003141                       0                    5891                      612   129284391
south africa    South Africa    681289         0    16976    614781    49532      539          0     4269626                       0                   11450                      285    59502099
------------------------------------------

--------------TOP 15, confirmed------------
                 country confirmed new_cases   deaths recovered   active critical new_deaths total_tests total_tests_per_million total_cases_per_million total_deaths_per_million  population
world              World  35437409     47298  1042343  26645311  7749755    66506        794           0                       0                    4546                    133.7           0
europe            Europe   5361834     25191   225329   2890100  2246405     9139        270           0                       0                       0                        0           0
asia                Asia  11102904     16975   201762   9387391  1513751    20772        258           0                       0                       0                        0           0
russia            Russia   1225889     10888    21475    982324   222090     2300        117    48042343                       0                    8399                      147   145950977
india              India   6626291      4111   102746   5586703   936842     8944         32    79982394                       0                    4789                       74  1383530375
ukraine          Ukraine    230236      3774     4430    101252   124554      177         33     2382259                       0                    5273                      101    43663726
mexico            Mexico    761665      3712    79088    550053   132524     2401        208     2003141                       0                    5891                      612   129284391
indonesia      Indonesia    307120      3622    11253    232593    63274        0        102     3515165                       0                    1120                       41   274274332
belgium          Belgium    130235      2612    10064     19679   100492      186         20     3402761                       0                   11224                      867    11602851
philippines  Philippines    324762      2291     5840    273123    45799     1758         64     3873843                       0                    2954                       53   109957856
poland            Poland    102080      2006     2659     73552    25869      219         29     3465605                       0                    2698                       70    37835645
romania          Romania    137491      1591     5048    108526    23917      592         45     2516746                       0                    7160                      263    19203449
switzerland  Switzerland     55932      1548     2078     45800     8054       32          1     1417260                       0                    6450                      240     8671140
bangladesh    Bangladesh    370132      1442     5375    283182    81575        0         27     2001431                       0                    2242                       33   165115692
israel            Israel    268175      1400     1719    201392    65064      878          0     3733880                       0                   29157                      187     9197590
------------------------------------------

--------------TOP 15, confirmed------------
                     country confirmed new_cases   deaths recovered   active critical new_deaths total_tests total_tests_per_million total_cases_per_million total_deaths_per_million  population
world                  World  35437409     47298  1042343  26645311  7749755    66506        794           0                       0                    4546                    133.7           0
south america  South America   8287914       299   261464   7142208   884242    17446         28           0                       0                       0                        0           0
europe                Europe   5361834     25191   225329   2890100  2246405     9139        270           0                       0                       0                        0           0
usa                      USA   7637066       154   214615   4849454  2572997    14198          4   111471522                       0                   23037                      647   331510437
asia                    Asia  11102904     16975   201762   9387391  1513751    20772        258           0                       0                       0                        0           0
brazil                Brazil   4915289         0   146375   4263208   505706     8318          0    17900000                       0                   23081                      687   212953890
india                  India   6626291      4111   102746   5586703   936842     8944         32    79982394                       0                    4789                       74  1383530375
mexico                Mexico    761665      3712    79088    550053   132524     2401        208     2003141                       0                    5891                      612   129284391
uk                        UK    502978         0    42350         0        0      368          0    25048460                       0                    7399                      623    67979397
africa                Africa   1522974        46    36569   1260456   225949     1632          0           0                       0                       0                        0           0
italy                  Italy    325329         0    35986    231914    57429      303          0    11784105                       0                    5383                      595    60438292
peru                    Peru    828169         0    32742    706223    89204     1287          0     3952298                       0                   25027                      989    33090379
france                France    619190         0    32230     97778   489182     1276          0    11469737                       0                    9481                      493    65311522
spain                  Spain    810807         0    32086         0        0     1566          0    12723989                       0                   17340                      686    46759558
iran                    Iran    471772         0    26957    389966    54849     4154          0     4123173                       0                    5598                      320    84270921
------------------------------------------

--------------TOP 15, recovered------------
                     country confirmed new_cases   deaths recovered   active critical new_deaths total_tests total_tests_per_million total_cases_per_million total_deaths_per_million  population
world                  World  35437409     47298  1042343  26645311  7749755    66506        794           0                       0                    4546                    133.7           0
asia                    Asia  11102904     16975   201762   9387391  1513751    20772        258           0                       0                       0                        0           0
south america  South America   8287914       299   261464   7142208   884242    17446         28           0                       0                       0                        0           0
india                  India   6626291      4111   102746   5586703   936842     8944         32    79982394                       0                    4789                       74  1383530375
usa                      USA   7637066       154   214615   4849454  2572997    14198          4   111471522                       0                   23037                      647   331510437
brazil                Brazil   4915289         0   146375   4263208   505706     8318          0    17900000                       0                   23081                      687   212953890
europe                Europe   5361834     25191   225329   2890100  2246405     9139        270           0                       0                       0                        0           0
africa                Africa   1522974        46    36569   1260456   225949     1632          0           0                       0                       0                        0           0
russia                Russia   1225889     10888    21475    982324   222090     2300        117    48042343                       0                    8399                      147   145950977
colombia            Colombia    855052         0    26712    761674    66666     2220          0     3894289                       0                   16758                      524    51023638
peru                    Peru    828169         0    32742    706223    89204     1287          0     3952298                       0                   25027                      989    33090379
argentina          Argentina    798486         0    21018    636672   140796     3950          0     2064250                       0                   17625                      464    45303674
south africa    South Africa    681289         0    16976    614781    49532      539          0     4269626                       0                   11450                      285    59502099
mexico                Mexico    761665      3712    79088    550053   132524     2401        208     2003141                       0                    5891                      612   129284391
chile                  Chile    470179         0    12979    442070    15130      856          0     3466553                       0                   24541                      677    19158936
------------------------------------------

--------------TOP 15, active------------
                     country confirmed new_cases   deaths recovered   active critical new_deaths total_tests total_tests_per_million total_cases_per_million total_deaths_per_million  population
world                  World  35437409     47298  1042343  26645311  7749755    66506        794           0                       0                    4546                    133.7           0
usa                      USA   7637066       154   214615   4849454  2572997    14198          4   111471522                       0                   23037                      647   331510437
europe                Europe   5361834     25191   225329   2890100  2246405     9139        270           0                       0                       0                        0           0
asia                    Asia  11102904     16975   201762   9387391  1513751    20772        258           0                       0                       0                        0           0
india                  India   6626291      4111   102746   5586703   936842     8944         32    79982394                       0                    4789                       74  1383530375
south america  South America   8287914       299   261464   7142208   884242    17446         28           0                       0                       0                        0           0
brazil                Brazil   4915289         0   146375   4263208   505706     8318          0    17900000                       0                   23081                      687   212953890
france                France    619190         0    32230     97778   489182     1276          0    11469737                       0                    9481                      493    65311522
africa                Africa   1522974        46    36569   1260456   225949     1632          0           0                       0                       0                        0           0
russia                Russia   1225889     10888    21475    982324   222090     2300        117    48042343                       0                    8399                      147   145950977
argentina          Argentina    798486         0    21018    636672   140796     3950          0     2064250                       0                   17625                      464    45303674
mexico                Mexico    761665      3712    79088    550053   132524     2401        208     2003141                       0                    5891                      612   129284391
ukraine              Ukraine    230236      3774     4430    101252   124554      177         33     2382259                       0                    5273                      101    43663726
belgium              Belgium    130235      2612    10064     19679   100492      186         20     3402761                       0                   11224                      867    11602851
peru                    Peru    828169         0    32742    706223    89204     1287          0     3952298                       0                   25027                      989    33090379
------------------------------------------

--------------TOP 15, critical------------
                     country confirmed new_cases   deaths recovered   active critical new_deaths total_tests total_tests_per_million total_cases_per_million total_deaths_per_million  population
world                  World  35437409     47298  1042343  26645311  7749755    66506        794           0                       0                    4546                    133.7           0
asia                    Asia  11102904     16975   201762   9387391  1513751    20772        258           0                       0                       0                        0           0
south america  South America   8287914       299   261464   7142208   884242    17446         28           0                       0                       0                        0           0
usa                      USA   7637066       154   214615   4849454  2572997    14198          4   111471522                       0                   23037                      647   331510437
europe                Europe   5361834     25191   225329   2890100  2246405     9139        270           0                       0                       0                        0           0
india                  India   6626291      4111   102746   5586703   936842     8944         32    79982394                       0                    4789                       74  1383530375
brazil                Brazil   4915289         0   146375   4263208   505706     8318          0    17900000                       0                   23081                      687   212953890
iran                    Iran    471772         0    26957    389966    54849     4154          0     4123173                       0                    5598                      320    84270921
argentina          Argentina    798486         0    21018    636672   140796     3950          0     2064250                       0                   17625                      464    45303674
mexico                Mexico    761665      3712    79088    550053   132524     2401        208     2003141                       0                    5891                      612   129284391
russia                Russia   1225889     10888    21475    982324   222090     2300        117    48042343                       0                    8399                      147   145950977
colombia            Colombia    855052         0    26712    761674    66666     2220          0     3894289                       0                   16758                      524    51023638
philippines      Philippines    324762      2291     5840    273123    45799     1758         64     3873843                       0                    2954                       53   109957856
africa                Africa   1522974        46    36569   1260456   225949     1632          0           0                       0                       0                        0           0
spain                  Spain    810807         0    32086         0        0     1566          0    12723989                       0                   17340                      686    46759558
------------------------------------------

--------------TOP 15, new_deaths------------
                     country confirmed new_cases   deaths recovered   active critical new_deaths total_tests total_tests_per_million total_cases_per_million total_deaths_per_million  population
world                  World  35437409     47298  1042343  26645311  7749755    66506        794           0                       0                    4546                    133.7           0
europe                Europe   5361834     25191   225329   2890100  2246405     9139        270           0                       0                       0                        0           0
asia                    Asia  11102904     16975   201762   9387391  1513751    20772        258           0                       0                       0                        0           0
mexico                Mexico    761665      3712    79088    550053   132524     2401        208     2003141                       0                    5891                      612   129284391
russia                Russia   1225889     10888    21475    982324   222090     2300        117    48042343                       0                    8399                      147   145950977
indonesia          Indonesia    307120      3622    11253    232593    63274        0        102     3515165                       0                    1120                       41   274274332
philippines      Philippines    324762      2291     5840    273123    45799     1758         64     3873843                       0                    2954                       53   109957856
romania              Romania    137491      1591     5048    108526    23917      592         45     2516746                       0                    7160                      263    19203449
ukraine              Ukraine    230236      3774     4430    101252   124554      177         33     2382259                       0                    5273                      101    43663726
india                  India   6626291      4111   102746   5586703   936842     8944         32    79982394                       0                    4789                       74  1383530375
poland                Poland    102080      2006     2659     73552    25869      219         29     3465605                       0                    2698                       70    37835645
south america  South America   8287914       299   261464   7142208   884242    17446         28           0                       0                       0                        0           0
bolivia              Bolivia    136868       299     8101     97547    31220       71         28      307040                       0                   11684                      692    11714131
bangladesh        Bangladesh    370132      1442     5375    283182    81575        0         27     2001431                       0                    2242                       33   165115692
honduras            Honduras     79629       841     2422     29305    47902       30         23      186350                       0                    8007                      244     9945117
------------------------------------------

>>> Elapsed time: 3.0735 seconds  [00:00:03]
'''