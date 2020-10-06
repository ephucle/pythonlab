#!/usr/bin/env python3
from covid import Covid
import pandas as pd
import sys
from myfunc import Timer

#clear screen
print('\033c')

t =Timer() 
t.start()


#covid = Covid()
print("Source from https://www.worldometers.info/coronavirus/#countries")
covid = Covid(source="worldometers")  #https://www.worldometers.info/coronavirus/#countries



covid.get_data()

total_active_cases = covid.get_total_active_cases()
total_confirmed_cases = covid.get_total_confirmed_cases()
total_deaths= covid.get_total_deaths()
total_recovered = covid.get_total_recovered()


#print allign , https://stackoverflow.com/questions/8234445/format-output-string-right-alignment
print( f'{"Total number of confirmed cases":<40}  {total_confirmed_cases:<12}' )
print( f'{"Total number of active cases":<40}  {total_active_cases:<12}' )
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
continents = ["world", "asia", "oceania", "europe", "africa","south america", "north america"]

for item in continents:
	countries.remove(item)



#########dirty code

df_ = pd.DataFrame()
for country in continents:
	serie = fetch_covid_by_country_name(country)
	df_= pd.concat([df_,pd.DataFrame(serie)], axis=1)

df_ = df_.T
df_ = df_.iloc[1:]  #remove first row
#remove un useful columns
df_.pop("total_tests_per_million")
df_.pop("total_cases_per_million")
df_.pop("total_deaths_per_million")

print("#"*30)
print("World and Continent data")
print(df_)
print("#"*30)
###############################

df = pd.DataFrame()
for country in countries:
	serie = fetch_covid_by_country_name(country)
	df= pd.concat([df,pd.DataFrame(serie)], axis=1)

df = df.T
df = df.iloc[1:]  #remove first row
#remove un useful columns
df.pop("total_tests_per_million")
df.pop("total_cases_per_million")
df.pop("total_deaths_per_million")



import datetime
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))




print("--------------TOP 10, confirmed------------")
df= df.sort_values(by=['confirmed'], ascending=False)
print(df.head(10))
print("------------------------------------------\n")

print("--------------TOP 10, new_cases------------")
df= df.sort_values(by=['new_cases'], ascending=False)
print(df.head(10))
print("------------------------------------------\n")


print("--------------TOP 10, deaths------------")
df= df.sort_values(by=['deaths'], ascending=False)
print(df.head(10))
print("------------------------------------------\n")

print("--------------TOP 10, recovered------------")
df= df.sort_values(by=['recovered'], ascending=False)
print(df.head(10))
print("------------------------------------------\n")

print("--------------TOP 10, active------------")
df= df.sort_values(by=['active'], ascending=False)
print(df.head(10))
print("------------------------------------------\n")

print("--------------TOP 10, critical------------")
df= df.sort_values(by=['critical'], ascending=False)
print(df.head(10))
print("------------------------------------------\n")





t.stop()

'''
SAMPLE DATA
>>> The action start at: 2020-10-06 09:10:48.002936
Source from https://www.worldometers.info/coronavirus/#countries
Total number of confirmed cases           35695735
Total number of active cases              7784060
Total deaths                              1045920
Total recovered                           26865755


Vietnam Covid Data:
country                      Vietnam
confirmed                       1097
new_cases                          0
deaths                            35
recovered                       1022
active                            40
critical                           0
new_deaths                         0
total_tests                  1009145
total_tests_per_million            0
total_cases_per_million           11
total_deaths_per_million         0.4
population                  97568899
Name: vietnam, dtype: object
##############################
World and Continent data
                     country confirmed new_cases  deaths recovered   active critical new_deaths total_tests population
asia                    Asia  11181470        87  203126   9476346  1501998    20727          0           0          0
oceania              Oceania     31835         3     937     29033     1865       15          0           0          0
europe                Europe   5438458         0  225689   2899644  2313125     9451          0           0          0
africa                Africa   1527905         0   36697   1268405   222803     1638          0           0          0
south america  South America   8336775       239  262683   7201509   872583    17459         28           0          0
north america  North America   9178571         0  316773   5990167  2871631    17587          0           0          0
##############################
2020-10-06 09:10:50
--------------TOP 10, confirmed------------
                   country confirmed new_cases  deaths recovered   active critical new_deaths total_tests  population
usa                    USA   7679644         0  215032   4895078  2569534    14283          0   112503131   331515730
india                India   6682073         0  103600   5659110   919363     8944          0    79982394  1383567415
brazil              Brazil   4940499         0  146773   4295302   498424     8318          0    17900000   212958012
russia              Russia   1225889         0   21475    982324   222090     2300          0    48042343   145951147
colombia          Colombia    862158         0   26844    766300    69014     2220          0     3930262    51025119
spain                Spain    852838         0   32225         0        0     1580          0    13689776    46759607
peru                  Peru    829999         0   32834    712888    84277     1269          0     3961345    33091634
argentina        Argentina    809728         0   21468    649017   139243     3978          0     2084513    45304806
mexico              Mexico    761665         0   79088    550053   132524     2401          0     2003141   129288090
south africa  South Africa    682215         0   17016    615684    49515      539          0     4280340    59504141
------------------------------------------

--------------TOP 10, new_cases------------
                 country confirmed new_cases deaths recovered active critical new_deaths total_tests  population
bolivia          Bolivia    137107       239   8129     98007  30971       71         28      308129    11714567
s. korea        S. Korea     24239        75    422     22083   1734      105          0     2365433    51280942
china              China     85482        12   4634     80635    213        2          0   160000000  1439323776
new zealand  New Zealand      1858         3     25      1790     43        1          0      985639     5002100
benin              Benin      2357         0     41      1973    343        0          0      203831    12204208
sri lanka      Sri Lanka      3513         0     13      3259    241        0          0      296611    21437046
malta              Malta      3327         0     39      2770    518        0          0      265630      441855
mali                Mali      3189         0    131      2482    576        0          0       56337    20398911
guyana            Guyana      3188         0     90      1972   1126       14          0       15078      787557
botswana        Botswana      3172         0     16       710   2446        1          0      184076     2363874
------------------------------------------

--------------TOP 10, deaths------------
       country confirmed new_cases  deaths recovered   active critical new_deaths total_tests  population
usa        USA   7679644         0  215032   4895078  2569534    14283          0   112503131   331515730
brazil  Brazil   4940499         0  146773   4295302   498424     8318          0    17900000   212958012
india    India   6682073         0  103600   5659110   919363     8944          0    79982394  1383567415
mexico  Mexico    761665         0   79088    550053   132524     2401          0     2003141   129288090
uk          UK    515571         0   42369         0        0      368          0    25865851    67980370
italy    Italy    327586         0   36002    232681    58903      323          0    11844346    60438050
peru      Peru    829999         0   32834    712888    84277     1269          0     3961345    33091634
france  France    624274         0   32299     98680   493295     1415          0    11616000    65311915
spain    Spain    852838         0   32225         0        0     1580          0    13689776    46759607
iran      Iran    475674         0   27192    392293    56189     4167          0     4151445    84273859
------------------------------------------

--------------TOP 10, recovered------------
                   country confirmed new_cases  deaths recovered   active critical new_deaths total_tests  population
india                India   6682073         0  103600   5659110   919363     8944          0    79982394  1383567415
usa                    USA   7679644         0  215032   4895078  2569534    14283          0   112503131   331515730
brazil              Brazil   4940499         0  146773   4295302   498424     8318          0    17900000   212958012
russia              Russia   1225889         0   21475    982324   222090     2300          0    48042343   145951147
colombia          Colombia    862158         0   26844    766300    69014     2220          0     3930262    51025119
peru                  Peru    829999         0   32834    712888    84277     1269          0     3961345    33091634
argentina        Argentina    809728         0   21468    649017   139243     3978          0     2084513    45304806
south africa  South Africa    682215         0   17016    615684    49515      539          0     4280340    59504141
mexico              Mexico    761665         0   79088    550053   132524     2401          0     2003141   129288090
chile                Chile    471746         0   13037    443453    15256      853          0     3502751    19159383
------------------------------------------

--------------TOP 10, active------------
             country confirmed new_cases  deaths recovered   active critical new_deaths total_tests  population
usa              USA   7679644         0  215032   4895078  2569534    14283          0   112503131   331515730
india          India   6682073         0  103600   5659110   919363     8944          0    79982394  1383567415
brazil        Brazil   4940499         0  146773   4295302   498424     8318          0    17900000   212958012
france        France    624274         0   32299     98680   493295     1415          0    11616000    65311915
russia        Russia   1225889         0   21475    982324   222090     2300          0    48042343   145951147
argentina  Argentina    809728         0   21468    649017   139243     3978          0     2084513    45304806
mexico        Mexico    761665         0   79088    550053   132524     2401          0     2003141   129288090
ukraine      Ukraine    230236         0    4430    101252   124554      177          0     2382259    43663012
belgium      Belgium    130235         0   10064     19679   100492      186          0     3402761    11602989
peru            Peru    829999         0   32834    712888    84277     1269          0     3961345    33091634
------------------------------------------

--------------TOP 10, critical------------
                 country confirmed new_cases  deaths recovered   active critical new_deaths total_tests  population
usa                  USA   7679644         0  215032   4895078  2569534    14283          0   112503131   331515730
india              India   6682073         0  103600   5659110   919363     8944          0    79982394  1383567415
brazil            Brazil   4940499         0  146773   4295302   498424     8318          0    17900000   212958012
iran                Iran    475674         0   27192    392293    56189     4167          0     4151445    84273859
argentina      Argentina    809728         0   21468    649017   139243     3978          0     2084513    45304806
mexico            Mexico    761665         0   79088    550053   132524     2401          0     2003141   129288090
russia            Russia   1225889         0   21475    982324   222090     2300          0    48042343   145951147
colombia        Colombia    862158         0   26844    766300    69014     2220          0     3930262    51025119
philippines  Philippines    324762         0    5840    273123    45799     1758          0     3914732   109961842
spain              Spain    852838         0   32225         0        0     1580          0    13689776    46759607
------------------------------------------

>>> Elapsed time: 3.0156 seconds  [00:00:03]
ephucle@VN-00000267:/mnt/c/cygwin/home/ephucle/tool_script/python/pythonlab$

'''