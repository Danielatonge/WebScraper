import time
import csv
import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, \
    ElementNotInteractableException, NoSuchElementException
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/macbookpro/Downloads/chromedriver')
driver.get("https://vk.com/hockeyvezde")

while True:
    try:
        username = driver.find_element_by_id("quick_email")
        password = driver.find_element_by_id("quick_pass")
        input_email = input("Enter email:")
        input_pass = input("Enter password:")
        username.send_keys(input_email)
        password.send_keys(input_pass)
        driver.find_element_by_id("quick_login_button").click()
        time.sleep(3)
        auth_code = driver.find_element_by_id("authcheck_code")
        input_code = int(input("Enter auth code:"))
        auth_code.send_keys(input_code)
        driver.find_element_by_id("login_authcheck_submit_btn").click()

        SCROLL_PAUSE_TIME = 2
        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")
        count = 0
        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")

            # To finally break
            # if new_height == last_height:
            #     break
            # last_height = new_height
            if count == 20:
                break
            count += 1

    except TimeoutException:
        break
    except StaleElementReferenceException:
        break
    except NoSuchElementException:
        break

invalid_tags = ['span', 'a', 'div']
soup = BeautifulSoup(driver.page_source, 'html.parser')

raw_events = soup.find_all("div", class_="wall_post_text")
print(len(raw_events))


def find_item(word, list_string):
    for (index, item) in enumerate(list_string):
        if word in item:
            return index
    return -1


with open('arena_id.csv', newline='') as f:
    reader = csv.reader(f)
    arena_id = list(reader)


def find_arena_id(address, list_arenas):
    for arena in list_arenas:
        component = address.split(" ")
        for segment in component:
            if len(segment) <= 2:
                break
            if segment in arena[1]:
                return arena[0]
    return ""



filename = "events.csv"
fWriter = csv.writer(open(filename, "w"))
fWriter.writerow(["title", "phone", "type", "date", "start_time", "end_time", "description", "activity_type", "price",
                  "arena_id"])

for event in raw_events:
    for tag in invalid_tags:
        for match in event.findAll(tag):
            match.replaceWithChildren()
    complete = list(event.stripped_strings)
    print(complete)
    date = complete[find_item("Дата", complete)] if find_item("Дата", complete) != -1 else complete[0]
    katok_address = complete[find_item("Адрес", complete)] if find_item("Адрес", complete) != -1 else complete[1]
    begin = complete[find_item("Начало", complete)] if find_item("Начало", complete) != -1 else ''
    length = complete[find_item("Продолжительность", complete)] if find_item("Продолжительность",
                                                                             complete) != -1 else ''
    tematika = complete[find_item("Тематика", complete)] if find_item("Тематика", complete) != -1 else ''
    level = complete[find_item("Уровень", complete)] if find_item("Уровень", complete) != -1 else ''
    goalkeeper = complete[find_item("Вратари", complete)] if find_item("Вратари", complete) != -1 else ''
    trainer = complete[find_item("Тренер", complete)] if find_item("Тренер", complete) != -1 else ''
    judge = complete[find_item("Судья", complete)] if find_item("Судья", complete) != -1 else ''
    cost = complete[find_item("Стоимость", complete)] if find_item("Стоимость", complete) != -1 else ''
    max_players = complete[find_item("полевых", complete)] if find_item("полевых", complete) != -1 else ''
    phone = complete[find_item("+7", complete)] if find_item("+7", complete) != -1 else complete[
        find_item("тел", complete)]
    telegram = complete[find_item("@", complete)] if find_item("@", complete) != -1 else ''
    note = complete[find_item("Примечание", complete)] if find_item("Примечание", complete) != -1 else ''

    description = f"{length}<br/>{level}<br/>{goalkeeper}<br/>{trainer}<br/>{judge}<br/>" \
                  f"{max_players}<br/>{note}<br/>{telegram}<br/>"

    event_arena_id = find_arena_id(katok_address, arena_id)
    if event_arena_id:
        fWriter.writerow([katok_address, phone, tematika, date, begin, "", description, "", cost, event_arena_id])
