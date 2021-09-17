import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/anyday-john-lewis-partners-inset-office-chair-black/p5132256")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("paragraph", {""})
# <p class="price price--large price--large--anyday">£119.00</p>


print(request.content)
