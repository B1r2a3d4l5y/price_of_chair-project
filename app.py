import requests
from bs4 import BeautifulSoup

request = requests.get("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("paragraph", {"class": "price_color"})
print(element.text)
# <p class="price_color">£51.77</p>
