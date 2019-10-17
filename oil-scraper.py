from bs4 import BeautifulSoup as BS
import requests
import pandas as pd 

headers = {
        'user-agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'referrer': 'https://google.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }
count =0

# List of urls to scrape
urls = [
    "https://www.subaruofmiami.com/promotions/service/index.htm",
    "https://www.lehmansubaru.com/promotions/service/index.htm",
       ] 

# created reusable function and return the promo price and product name as a list 

def miami1(url):
    price1 = {}
    price1["miami"] = {}
    title = []
    response = requests.get(url, timeout=15, headers=headers)
    soup = BS(response.content, "html.parser")

    # The information was burried in a div
    html_tag = soup.find_all("div", class_="promo-title text-center h1")
    html_price = soup.find_all("div", class_="promo-discountValue text-center h1 has-image")[2]

    # The find_all method places the results in a list, so this needed to be looped through
    # to get just the text using the .text method.
    for tag in html_tag:
        if "OIL" in tag.text.strip():
            price1["miami"]["url"] = url[0:29]
            price1["miami"]["product"] = tag.text.strip()
            price1["miami"]["price"]  = html_price.text[1:8]

    print(pd.DataFrame.from_dict(price1, orient='index'))

    #print(html_tag,html_price)

def lehmans(url):
    price1 = {}
    price1["lehmans"] = {}
    title = []
    response = requests.get(url, timeout=15, headers=headers)
    soup = BS(response.content, "html.parser")

    # The information was burried in a div
    html_tag = soup.find_all("div", class_="promo-title text-center h1")
    html_price = soup.find_all("div", class_="promo-discountValue text-center h1 has-image")[4]

    # The find_all method places the results in a list, so this needed to be looped through
    # to get just the text using the .text method.
    for tag in html_tag:
        if "Oil" in tag.text.strip():
            price1["lehmans"]["url"] = url[0:29]
            price1["lehmans"]["product"] = tag.text.strip()
            price1["lehmans"]["price"]  = html_price.text[1:8]

    print(pd.DataFrame.from_dict(price1, orient='index'))

    #print(html_tag,html_price)

miami1(urls[0])
lehmans(urls[1])


