import requests
import csv
from bs4 import BeautifulSoup

URL = "https://msk.nhliga.org/team"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
raw_teams = soup.find_all("tr")

print(len(raw_teams))
filename = "teams.csv"
fWriter = csv.writer(open(filename, "w"))
fWriter.writerow(["title", "description", "minidescription", "city", "type", "level", "profile_picture", "is_visible",
                  "phones", "mails", "instagram", "vk", "website", "whats_app", "facebook", "classmates", "tiktok",
                  "twitter", "youtube", "gallery"])


def array_output(array_input):
    temp = ', '.join(array_input)
    return "{" + temp + "}"


for team in raw_teams:
    team_link = ""
    if team.find("a"):
        team_link = team.find("a")["href"]
    if len(team_link) == 0:
        continue
    print(team_link)
    npage = requests.get(f'https:{team_link}')
    nsoup = BeautifulSoup(npage.content, "html.parser")
    full_team = nsoup.find("div", {"id": "tab_info"})
    team_header = full_team.find("div", class_="team-head__inner")
    team_name = team_header.find("h1").text.strip()
    start_team_link = team_link.split("/")[2]
    profilePicture = f'https://{start_team_link}' + team_header.find("img")["src"]
    team_meta = team_header.find("div", class_="team-head__block").find_all("div")

    team_ligue = ''
    team_region = ''
    team_city = ''
    if len(team_meta) == 3:
        team_ligue = team_meta[0].text.strip()
        team_region = team_meta[1].text.strip()
        team_city = team_meta[2].text.strip()

    gallery = []
    photos = full_team.find_all("img", class_="team-head__img")
    for pic in photos:
        complete_picture = f'https://{start_team_link}{pic["src"]}'
        gallery.append(complete_picture)

    description = ""
    if full_team.find("div", class_="hide-text__inner"):
        description = full_team.find("div", class_="hide-text__inner").text.strip()

    type = ''
    level = ''
    phones = '{}'
    mails = '{}'
    instagram = ''
    vk = ''
    website = ''
    whats_app = ''
    facebook = ''
    classmates = ''
    tiktok = ''
    twitter = ''
    youtube = ''
    is_visible = 'null'
    gallery = array_output(gallery)
    fWriter.writerow([team_name, description, description, team_city, type, level, profilePicture, is_visible,
                      phones, mails, instagram, vk, website, whats_app, facebook, classmates, tiktok,
                      twitter, youtube, gallery])
