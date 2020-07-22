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


url = "https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2"

content = simple_get(url)
#print (content)

soup = BeautifulSoup(content, 'html.parser')
#beautifu print for easy check content, chuyen html page sang dinh dang ma con nguoi read duoc
#print(soup.prettify())


#xu ly noi dung
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product

for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
	name=a.find('div', attrs={'class':'_3wU53n'})
	#<div class="_3wU53n">Lenovo Core i5 7th Gen - (8 GB/1 TB HDD/DOS/2 GB Graphics) IP 320-15IKB Laptop</div>
	
	price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
	#<div class="_1vC4OE _2rQ-NK">₹75,500</div>
	
	rating=a.find('div', attrs={'class':'hGSR34'})
	#<div class="hGSR34">4.3<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==" class="_2lQ_WZ"></div>
	
	products.append(name.text)
	prices.append(price.text)
	ratings.append(rating.text) 

print (products)
print (prices)
print (ratings)

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')