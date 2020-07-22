#!/usr/bin/env python3
#./wget.py https://www.python.org/

import sys
from urllib.request import urlopen

url = sys.argv[1]

if url.endswith("/"):
	output_filename = 'index.html'
else:
	url_parts = url.split("/")
	output_filename = url_parts[-1]



print(f"saving {url} as {output_filename}...")


response = urlopen(url)
content = response.read()
text = content.decode('utf-8')


with open(output_filename, 'w') as outfile:
	outfile.write(text)
print("Saving done !!!")
