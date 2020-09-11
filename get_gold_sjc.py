#!/usr/bin/env python3.8

#https://www.edureka.co/blog/web-scraping-with-python/

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import pandas as pd
import sys


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)



url = "http://acb.com.vn/wps/portal/Home/exchange?&ved=0CCYQFjADOBRqFQoTCMSRhKPI6MYCFWK_cgodTlwBSg&usg=AFQjCNFiAr98xL0PXNenLDeWvx69kFa_Jw"
#url = "https://vnexpress.net/tac-gia-nhat-ky-vu-han-xuc-dong-ngay-cham-dut-phong-toa-4081291.html"
#url = 'http://sjc.com.vn/giavang/'


content = simple_get(url)
#print (content)


soup = BeautifulSoup(content, 'html.parser')
#print(soup)
html = soup.prettify()
for line in html:
	print(line)


#<td class="bodertop txbody" align="right">55,800,000</td>
#<td class="bodertop txbody" align="right">56,400,000</td>