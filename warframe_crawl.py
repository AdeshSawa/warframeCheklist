import requests
import json
import os
from bs4 import BeautifulSoup

URL = "https://www.warframe.com/game/warframes"
warframes = []

# create folder if not exist
if not os.path.exists('data/images'):
   os.makedirs('data/images')


# downloads file, accepts url as parameter
def download_file(url):
    response = requests.get(url)
    if "content-disposition" in response.headers:
        content_disposition = response.headers["content-disposition"]
        filename = content_disposition.split("filename=")[1]
    else:
        filename = url.split("/")[-1]
    with open("./data/images/"+filename, mode="wb") as file:
        file.write(response.content)
    print(f"Downloaded file {filename}")

    return filename

# request page and get targeted elements
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
frames = soup.find_all("a", {"class": "wf"})


# loop over each element and grab data
for idx, x in enumerate(frames):
    item = {}
    img = x.find("img")['src']
    name = x.find("div", {"class": "innerWfTitle"}).text
    filename = download_file(img)

    item["id"] = idx
    item["name"] = name
    item["image"] = filename
    item["img_url"] = img
    item["built"] = 0
    item["owned"] = 0
    item["mastered"] = 0

    warframes.append(item)
    print("item #{} = {} - {}".format(idx, img, name))

# Serializing json
json_object = json.dumps(warframes)

# Writing to sample.json
with open("./data/warframes.json", "w") as outfile:
    outfile.write(json_object)