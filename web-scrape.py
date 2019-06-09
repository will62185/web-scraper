import requests
from bs4 import BeautifulSoup as bs


result = requests.get("https://www.subaruofpembrokepines.com/specials/service.htm")
source = result.content
soup = bs(source, "lxml")

h4_tag = soup.find_all("h4", class_="sssTitle")
print(h4_tag)

p_tag = soup.find_all("p", class_="value")
print(p_tag)

"""
Results:
[<h4 class="sssTitle">
<span>Meet Or Beat Any Tire Special</span>
</h4>, <h4 class="sssTitle">
<span>Battery System Service</span>
</h4>, <h4 class="sssTitle">
<span>Brake Fluid Service</span>
</h4>, <h4 class="sssTitle">
<span>Guard Against Harmful Effects Of Ethanol Gasoline</span>
</h4>, <h4 class="sssTitle">
<span>Air Conditioning Service</span>
</h4>, <h4 class="sssTitle">
<span>Subaru of Pembroke Pines Full Detail</span>
</h4>]
[<p class="value"></p>, <p class="value">$35.95</p>, <p class="value">$149.95</p>, <p class="v
alue">$129.95</p>, <p class="value">$69.95</p>, <p class="value">$20.00 Off</p>]
"""

# To Do:
# Print the titles and the prices e.g. Oil Change $19.99
# Have multiple sources of dealerships
# Print the Dealership name along with a link to the services page.
# Email Results.