#!/usr/bin/env python3
import json

with open('parameters.json') as json_file:
	data = json.load(json_file)
	print(type(data))
	print(data)
	print("parameters input:")
	print(json.dumps(data,indent=4))
	print("*"*30)

print(data['nodename'])
print(data['sign'])