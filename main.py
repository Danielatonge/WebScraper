import requests
from bs4 import BeautifulSoup

URL = "https://nhliga.org/team?search=&season=20&conference=2&division=0"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
temp1 = soup.findAll("div", {"data-key": True})
print(len(temp1))
for team in temp1:
    team_title = team.find("h5", class_="marketplace-item__name")
    team_link = team_title.find("a", {"href": True})
    go_to_link = team_link["href"]
    print(go_to_link)
    page = requests.get(f'https:{go_to_link}')
    # soup = BeautifulSoup(page.content, "html.parser")
    # print(soup.prettify())
    # print(arena_link)
