import requests
from bs4 import BeautifulSoup

URL = "https://ledokat.ru/rink"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
temp1 = soup.findAll("div", {"data-key": True})
print(len(temp1))
for arena in temp1:
    arena_title = arena.find("h5", class_="marketplace-item__name")
    arena_link = arena_title.find("a", {"href": True})
    go_to_link = arena_link["href"]
    print(go_to_link)
    page = requests.get(f'https:{go_to_link}')
    # soup = BeautifulSoup(page.content, "html.parser")
    # print(soup.prettify())
    # print(arena_link)
