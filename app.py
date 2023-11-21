import requests
from bs4 import BeautifulSoup

URL = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"
# need to login to see
# URL = "https://www.facebook.com/profile.php?id=61552164673190"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# results = soup.find(id="ResultsContainer")
results = soup.findAll(string="python")

for x in results:
    print(x)