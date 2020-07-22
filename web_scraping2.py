#thu lay noi dung mot TR ID xem thanh cong hay ko

#https://www.edureka.co/blog/web-scraping-with-python/

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import pandas as pd



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


#url = "https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2"

url = "https://mhweb.ericsson.se/TREditWeb/faces/oo/object.xhtml?eriref=HY34532"
#url = "https://vnexpress.net/tac-gia-nhat-ky-vu-han-xuc-dong-ngay-cham-dut-phong-toa-4081291.html"


content = simple_get(url)
#print (content)

soup = BeautifulSoup(content, 'html.parser')
#beautifu print for easy check content, chuyen html page sang dinh dang ma con nguoi read duoc
#print(soup.prettify())


#print(content)

print(soup.prettify())