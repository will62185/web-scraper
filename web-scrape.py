from bs4 import BeautifulSoup
import requests

urls = ["https://www.subaruofmiami.com/promotions/service/index.htm","  https://www.lehmansubaru.com/promotions/service/index.htm"] 

#scrape elements
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    print(f"Visit this link for more information: {url}")

    h1 = soup.find_all("div", class_="promo-title text-center h1")
    for tag in h1:
        print(tag.text)