#!/usr/bin/env python3
#script to get pulic ipaddress
import requests, json
data = requests.get('http://httpbin.org/get')

#>>> type(data)
#<class 'requests.models.Response'>

#print(data.text)

#{
#  "args": {},
#  "headers": {
#    "Accept": "*/*",
#    "Accept-Encoding": "gzip, deflate",
#    "Host": "httpbin.org",
#    "User-Agent": "python-requests/2.23.0",
#    "X-Amzn-Trace-Id": "Root=1-5f06cfd2-99254e60392b7ce0eded9f60"
#  },
#  "origin": "27.3.52.139",
#  "url": "http://httpbin.org/get"
#}

#print(type(data.text))
#<class 'str'>

#convert json format text string to dict
data_json = json.loads(data.text)

#>>> type(data_json)
#<class 'dict'>

#>>> print(data_json)
#{'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.23.0', 'X-Amzn-Trace-Id': 'Root=1-5f06d05c-6b60a4a63e8845822a69457a'}, 'origin': '27.3.52.139', 'url': 'http://httpbin.org/get'}

print("Your public IP address is:",data_json['origin'])
