import requests
from bs4 import BeautifulSoup

URL = "https://apia-arena.ledokat.ru/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
contacts = soup.find("div", class_="marketplace-view__contacts")

arena_title = soup.find("h1", class_="marketplace-view__title").find("span", class_="marketplace-view__name").text.strip()
arena_fullTitle = arena_title
arena_address = contacts.find("span", class_="marketplace-view__address").text.strip()
arena_metro = contacts.find("span", class_="marketplace-view__metro").text.strip()
arena_phone = contacts.find("span", class_="marketplace-view__phones").text.strip()
arena_tags = []
arena_website = ''
social_media = {}
description = ''
profilePicture = ''
gallery = []
latitude = soup.find("span", class_="marketplace-view-map__lat").text.strip()
longitude = soup.find("span", class_="marketplace-view-map__lng").text.strip()
arena_route = ''
sledge_hockey = ''
sledge_hockey_link = ''
court_size = ''
arena_city = arena_address.split(",")[0]
classmates = ''
arena_mails = ''


photos = soup.find_all("div", class_="carousel-item")
for index, image in enumerate(photos):
    if index == 0:
        picture = image.find("img")["src"]
        profilePicture = f"http:{picture}"
        continue

    picture = image.find("img")["src"]
    gallery.append(f"http:{picture}")

list_tags = soup.find_all("div", class_="marketplace-view-box")
for item in list_tags:
    heading = item.find("h3").text.strip()
    if heading == "Спортивные площадки" or \
            heading == "Виды катания" or \
            heading == "Сервисы":

        show = item.find_all("div", class_="marketplace-view-box__prop", text=True)
        for i in show:
            arena_tags.append(i.text.strip())
    if heading == "Сайт":
        arena_website = item.find("p", class_="marketplace-view-box__desc").text.strip()
    if heading == "Социальные сети":
        media = item.find_all("a", {"href": True})
        for x in media:
            link = x["href"]
            if "instagram.com" in link:
                social_media["instagram"] = link
            if "vk.com" in link:
                social_media["vk"] = link
            if "facebook.com" in link:
                social_media["facebook"] = link
            if "youtube.com" in link:
                social_media["youtube"] = link
            if "whatsapp" in link:
                social_media["whats_app"] = link
            if "tiktok" in link:
                social_media["tiktok"] = link
            if "twitter" in link:
                social_media["twitter"] = link
    if heading == "Описание":
        description = item.find("p").text


print(arena_title)
print(arena_city)
print(arena_address)
print(arena_metro)
print(latitude, longitude)
print(arena_phone)
print(profilePicture)
print(gallery)
print(arena_website)
print(description)
print(arena_tags)
print(social_media)

# "title, full_title, address, phones, tags, website, vk, facebook, youtube,
# instagram, description,
# "profile_picture, route, sledge_hockey, sledge_hockey_link, metro, court_size,
# city, lat, lan, gallery,
# "mails, whats_app, tiktok, classmates, twitter\n"
