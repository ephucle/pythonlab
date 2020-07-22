dict1 = {
	"nodename" : 'us-namgu-samsan-10-16',
	"crash_count" : 524,
	"crash_node" : 14,
	"hw" : 'fru_2048',
	"sign" : 'Board restart. Reason: Ordered immediate restart. Program: restart. Rank: Cold. Extra: Immediate',
	"kst" : '',
	"utc" : '2020-06-26 02:16:29',
	"sw" : 'MTR20.19_EC8',
	"matched_TR" : []
}

json.dumps(dict1)
y = json.dumps(dict1,indent=4)
print(y)

#>>> print(y)
#{
#    "nodename": "us-namgu-samsan-10-16",
#    "crash_count": 524,
#    "crash_node": 14,
#    "hw": "fru_2048",
#    "sign": "Board restart. Reason: Ordered immediate restart. Program: restart. Rank: Cold. Extra: Immediate",
#    "kst": "",
#    "utc": "2020-06-26 02:16:29",
#    "sw": "MTR20.19_EC8",
#    "matched_TR": []
#}

with open("parameters.json", "w") as out_file:
	json.dump(dict1, out_file, indent = 4, sort_keys = False)



#open json file

with open("parameters.json") as json_file:
    data = json.load(json_file)

print(data)
data.keys()
data.values()
data.items()
data['nodename']
data['crash_count']


>>> data.keys()
dict_keys(['nodename', 'crash_count', 'crash_node', 'hw', 'sign', 'kst', 'utc', 'sw', 'matched_TR'])
>>> data.values()
dict_values(['us-namgu-samsan-10-16', 524, 14, 'fru_2048', 'Board restart. Reason: Ordered immediate restart. Program: restart. Rank: Cold. Extra: Immediate', '', '2020-06-26 02:16:29',
'MTR20.19_EC8', []])
>>> data.items()
dict_items([('nodename', 'us-namgu-samsan-10-16'), ('crash_count', 524), ('crash_node', 14), ('hw', 'fru_2048'), ('sign', 'Board restart. Reason: Ordered immediate restart. Program: restart. Rank: Cold. Extra: Immediate'), ('kst', ''), ('utc', '2020-06-26 02:16:29'), ('sw', 'MTR20.19_EC8'), ('matched_TR', [])])
>>> data['nodename']
'us-namgu-samsan-10-16'
>>> data['crash_count']
524
>>>