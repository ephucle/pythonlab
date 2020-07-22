#!/usr/bin/env python3
from covid import Covid
from plyer import notification

covid = Covid()

#>>> dir(covid)
#['_Covid__get_all_cases', '_Covid__get_total_by_case', '_Covid__get_total_cases_by_country_id', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'get_data', 'get_status_by_country_id', 'get_status_by_country_name', 'get_total_active_cases', 'get_total_confirmed_cases', 'get_total_deaths', 'get_total_recovered', 'list_countries', 'source']
#>>>

#get_total_active_cases() -> int method of covid.john_hopkins.covid.Covid instance
#    Method fetches and returns total number of active cases


covid.get_data()

total_active_cases = covid.get_total_active_cases()
total_confirmed_cases = covid.get_total_confirmed_cases()
total_deaths= covid.get_total_deaths()
total_recovered = covid.get_total_recovered()
print("Total number of active cases: ", total_active_cases)
print("\nTotal number of confirmed cases: ", total_confirmed_cases)
print("Total deaths: ", total_deaths)
print("Total recovered: ", total_recovered)


vn_cases = covid.get_status_by_country_name("Vietnam")
phi_cases = covid.get_status_by_country_name("Philippines")

print("Vietnam", "*"*10)
for key in vn_cases:
	print(key, vn_cases[key])

print("Philippines", "*"*10)
for key in phi_cases:
	print(key, phi_cases[key])


notification.notify(
title = "Covid 19 Notification",
message = "Active cases:"+ str(total_active_cases) + "\nConfirmed cases:" + str(total_confirmed_cases) + "\nTotal deaths:" + str(total_deaths) + "\nTotal recovered:"+str(total_recovered) , 
timeout = 20
)