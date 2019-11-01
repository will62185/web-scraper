from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
import sendEmail

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

returnData = ""

# created reusable function and return the promo price and product name as a list 

def getprices(url):
    price1 = []
    title = []
    response = requests.get(url, timeout=15, headers=headers)
    soup = BS(response.content, "html.parser")

    # The information was burried in a div
    html_tag = soup.find_all("div", class_="promo-title text-center h1")
    html_price = soup.find_all("div", class_="promo-discountValue text-center h1 has-image")

    # The find_all method places the results in a list, so this needed to be looped through
    # to get just the text using the .text method.
    for tag in html_tag:
        for price in html_price:
            if price.text.strip():
                #print(tag.text.strip())
                #print("Promotional price " + price.text.strip())
                price1.append(price.text.strip())
                title.append(tag.text.strip())

    return price1,title

# loop through the urls and parse the data 
while count < len(urls):
    # call the function for the specified url 
    will= getprices(urls[count])
    #print(will[0])
    #using paqdas to format the output 
    print(urls[count])
    print(pd.DataFrame({'Product': will[1], \
                    'Promo': will[0]}))
    returnData += urls[count]
    returnData += pd.DataFrame({'Product': will[1], 'Promo': will[0]}).to_html()
    count += 1

sendEmail.sendEmail(f"""
<html>
    <head></head>
    <body>
        {returnData}
    </body>
</html>
""")
