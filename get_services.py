import csv

fWriter = csv.writer(open('service.csv', "w"))
fWriter.writerow(["arena_id", "title", "description", "type", "size", "length", "width", "price_id", "profile_picture"])

service_photo = [
    {'text': 'wifi',
     'photo': 'https://cdn.discordapp.com/attachments/799296035029123072/886673028300275732/Wi-Fi.png'},
    {'text': 'Душ',
     'photo': 'https://cdn.discordapp.com/attachments/799296035029123072/886673029134962779/c945f200a1a62ac1.png'},
    {'text': 'Заточка коньков',
     'photo': 'https://cdn.discordapp.com/attachments/799296035029123072/886673029831200768/732ef226be8df12c.png'},
    {'text': 'Инвентарь',
     'photo': 'https://cdn.discordapp.com/attachments/799296035029123072/886673031831887872/e59eb4c57de02994.png'},
    {'text': 'Кафе',
     'photo': 'https://cdn.discordapp.com/attachments/799296035029123072/886673032553308220/f83c841abdf8f037.png'},
    {'text': 'Массовое катание',
     'photo': 'https://cdn.discordapp.com/attachments/799296035029123072/886673034394632192/f56a5d0ac31f4475.png'},
    {'text': 'Парковка',
     'photo': 'https://cdn.discordapp.com/attachments/799296035029123072/886673037460660274/56efbe8e5eedc117.png'},
    {'text': 'Раздевалки',
     'photo': 'https://cdn.discordapp.com/attachments/799296035029123072/886673038899282000/cfc5daf6c47e0132.png'},
    {'text': 'Фигурное катание',
     'photo': 'https://cdn.discordapp.com/attachments/799296035029123072/886673042351210536/6006e324b1021f73.png'},
    {'text': 'Хоккейное катание',
     'photo': 'https://cdn.discordapp.com/attachments/799296035029123072/886673053109604352/10ee8e92ed24f4be.png'},
]

with open('arena_tags.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        id = row['id']
        title = row['title']
        tags = row['tags'].replace('{', '')
        tags = tags.replace('}', '').split(',')
        # print(tags)
        for service in tags:
            services_ = service.split(' ')
            found = False
            photo_link = ''
            for item in service_photo:
                if service == item['text']:
                    # print(f'{service} | {item["text"]}')
                    photo_link = item['photo']
                else:
                    photo_link = "https://cdn.discordapp.com/attachments/799296035029123072/887109950353051658/blog_avatar.png"
                    # print(f'{service} | {item["text"]} = False')
            for word in services_:

                if word.lower() in ['катание', 'зал', 'зона', 'поле', 'арена', 'лед', 'площадка']:
                    found = True
                    break
            if found:
                fWriter.writerow([id, service, '', 'RENT', '', '', '', '', photo_link])
            else:
                fWriter.writerow([id, service, '', 'OTHER', '', '', '', '', photo_link])
csvfile.close()
