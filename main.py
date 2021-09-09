import requests
from bs4 import BeautifulSoup

URL = "https://vk.com/hockeyvezde"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
raw_events = [event.find("div", class_="pi_text") for event in soup.find_all("div", class_="wi_body")]
print(len(raw_events))

for event in raw_events:
    if event:
        print(event)
        print("-------------------------------------")