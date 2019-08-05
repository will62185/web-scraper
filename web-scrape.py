from bs4 import BeautifulSoup as BS
import requests

# List of urls to scrape
urls = [
    "https://www.subaruofmiami.com/promotions/service/index.htm",
    "https://www.lehmansubaru.com/promotions/service/index.htm",
       ] 

# Loop through the urls
for url in urls:
    response = requests.get(url)
    soup = BS(response.content, "html.parser")
    
    # The information was burried in a div
    html_tag = soup.find_all("div", class_="promo-title text-center h1")

    # The find_all method places the results in a list, so this needed to be looped through
    # to get just the text using the .text method.
    for tag in html_tag: 
        print(tag.text.strip())
    print(f"Visit this link for more information: {url}")