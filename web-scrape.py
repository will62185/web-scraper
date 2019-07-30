import requests
from bs4 import BeautifulSoup as bs
from sys import argv
import datetime

# Example url "https://www.subaruofmiami.com/promotions/service/index.htm"
url = argv[1] # URL is now supplied at runtime

source = requests.get(url)
result = source.content
soup = bs(result, "lxml")

print(f"Get your coupons from: {url}")

html = soup.find_all("div", class_="promo-title text-center h1")
print(html)

"""
Results:
[<div class="promo-title text-center h1">
FREE MULTI-POINT INSPECTION
</div>, <div class="promo-title text-center h1">
$45 WIPER BLADES SPECIAL
</div>, <div class="promo-title text-center h1">
Free Alignment w/ Installation of 4 New Tires
</div>]
"""

# To Do:
# Print the titles and the prices e.g. Oil Change $19.99
# Have multiple sources of dealerships
# Print the Dealership name along with a link to the services page.
# Email Results.