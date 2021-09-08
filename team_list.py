import time
import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, ElementNotInteractableException
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/home/kiro/Desktop/WebScraper-main/chromedriver')
driver.get("https://nhliga.org/team?search=&season=20&conference=2&division=0")
count = 0
while True:
    try:
        showmore = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "marketplace-results-more__btn")))
        showmore.click()
        time.sleep(5)
    except TimeoutException:
        break
    except StaleElementReferenceException:
        break
    except ElementNotInteractableException:
        break

soup = BeautifulSoup(driver.page_source, 'html.parser')
temp1 = soup.findAll("div", {"data-key": True})
print(len(temp1))
team_list = []

filename = "teams.csv"
fWriter = csv.writer(open(filename, "w"))
fWriter.writerow(["title", "miniDescription", "description", "city", "type", "level", "profilePicture", "isVisible",
                  "phones", "mails", "website", "whatsApp", "vk", "instagram", "facebook", "classmates", "twitter",
                  "youtube", "tiktok", "gallery"])

def array_output(array_input):
    temp = ', '.join(array_input)
    return "{" + temp + "}"


for team in temp1:
    team_title = team.find("h5", class_="marketplace-item__name")
    team_link = team_title.find("a", {"href": True})
    go_to_link = f'https:{team_link["href"]}'
    print(go_to_link)
    team_list.append(go_to_link)
    npage = requests.get(go_to_link)
    soup = BeautifulSoup(npage.content, "html.parser")
    contacts = soup.find("div", class_="marketplace-view__contacts")

    team_title = soup.find("h1", class_="marketplace-view__title").find("span",
                                                                    class_="marketplace-view__name").text.strip()
    team_title = ""
    team_miniDescription = ""
    team_description = ""
    team_city = ""
    team_type = ""
    team_level = ""
    team_profilePicture = ""
    team_isVisible = ''
    team_mails = []
    team_phones = []
    team_gallery = []
    team_website = ''
    social_media = {"vk": '', "facebook": '', "youtube": '', "instagram": '', "whats_app": '', "tiktok": '',
                    "twitter": '', "classmates": ''}

    if contacts.find("span", class_="marketplace-view__address"):
        team_address = contacts.find("span", class_="marketplace-view__address").text.strip()
    if contacts.find("span", class_="marketplace-view__metro"):
        arena_metro.append(contacts.find("span", class_="marketplace-view__metro").text.strip())
    if contacts.find("span", class_="marketplace-view__phones"):
        phone_contacts = contacts.find_all("span", class_="marketplace-view__phone")
        for phone in phone_contacts:
            arena_phone.append(phone.text.strip())
    if soup.find("span", class_="marketplace-view-map__lat"):
        latitude = soup.find("span", class_="marketplace-view-map__lat").text.strip()
    if soup.find("span", class_="marketplace-view-map__lng"):
        longitude = soup.find("span", class_="marketplace-view-map__lng").text.strip()
    if arena_address:
        arena_city = arena_address.split(",")[0].split(".")[1]

    photos = soup.find_all("div", class_="carousel-item")
    if photos:
        for index, image in enumerate(photos):
            if index == 0:
                picture = image.find("img")["src"]
                profilePicture = f"http:{picture}"
                continue

            picture = image.find("img")["src"]
            gallery.append(f"http:{picture}")
    else:
        picture_holder = soup.find("div", class_="marketplace-view__preview").find("img")
        profilePicture = f'http:{picture_holder["src"]}'

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
            description = item.find("p").text.strip()

    arena_tags = array_output(arena_tags)
    arena_phone = array_output(arena_phone)
    arena_metro = array_output(arena_metro)
    arena_mails = array_output(arena_mails)
    gallery = array_output(gallery)
    fWriter.writerow([team_title, team_miniDescription, team_description, team_phones, team_mails,
                      team_website, social_media["vk"], social_media["facebook"], social_media["youtube"],
                      social_media["instagram"], description, profilePicture, arena_route, sledge_hockey,
                      sledge_hockey_link, arena_metro, court_size, arena_city, latitude, longitude, gallery,
                      arena_mails, social_media["whats_app"], social_media["tiktok"], classmates,
                      social_media["twitter"]])
