# -*- coding: utf-8 -*-
import pprint
import time
import random
import time
import vk_api
def send(text="no text"):
    return vk.method("messages.send",
              {"peer_id": ids,
               "message": text,
               "random_id": random.randint(1, 2147483647)})
vk = vk_api.VkApi(token="")
words = {"а":['аршин', 'абзац', 'авантюризм', 'авантюризм', 'азот', 'автоматизм', 'абонемент', 'аврал', 'аборт', 'анонс', 'арбуз'],
         "б":['басурман', 'безалаберный', 'богатый', 'бобыль', 'благородный', 'брандахлыст', 'богатырважно'],
         "в":['важный', 'взаимодействие', 'влияние', 'внимание', 'возможно', 'возможности', 'возможность', 'вопрос', 'время'],
         "г":['гармония', 'герой', 'главный', 'глаза', 'глупый', 'говорит', 'говорить', 'гордост', 'город', 'государстводаже'],
         "д":['данные', 'данный', 'действие', 'дело', 'деятельность', 'для', 'добрый', 'должник'],
         "е":['еда', 'единомышленник', 'единственный', 'единство', 'единый', 'емкость', 'ерунда'],
         "ж":['жара', 'желание', 'желанный', 'желаю', 'желтый', 'женщина', 'жертва', 'жесткий', 'жестокость'],
         "з":['забота', 'зависимость', 'задача', 'защита', 'здоровье', 'злой', 'знание', 'знания', 'знание', 'значение'],
         "и":['идея', 'изменение', 'изучение', 'изучит', 'именно', 'интерес', 'интересно', 'интересный', 'информация'],
         "й":['йога', 'йогурт'],
         "к":['каждый', 'картина', 'качок', 'качество', 'книга', 'количество', 'команда', 'комплекс', 'контроль', 'концепция'],
         "л":['легкий', 'легко', 'лидер', 'лицо', 'личность', 'лишайник', 'лом', 'лучше', 'лужа'],
         "м":['маленький', 'материал', 'мероприятие', 'место', 'метод', 'механизм', 'мечта', 'мир', 'мнение', 'многонаиболее'],
         "н":['наличие', 'направление', 'например', 'нарушение', 'начало', 'невозможно', 'недостаток', 'необходимо', 'необходимо'],
         "о":['обеспечение', 'образ', 'однако', 'определение', 'определенный', 'определить', 'организация', 'основа', 'основной'],
         "п":['поддержка', 'позволяет', 'помощь', 'понятие', 'поскольку', 'поэтому', 'прекрасный', 'пример', 'природа', 'причина'],
         "р":['работа', 'радост', 'развитие', 'различные', 'разный', 'разработка', 'распространение', 'рассмотрение', 'расса', 'реализация'],
         "с":['система', 'ситуация', 'совокупность', 'современный', 'согласно', 'содержание', 'создание', 'собака', 'состояние'],
         "т":['ток', 'также', 'творчество', 'тема', 'тенденция', 'территория', 'технология', 'только', 'требование'],
         "у":['увеличение', 'удовольствие', 'улучшение', 'умный', 'уникальный', 'управление', 'ум', 'условие', 'условия', 'успех'],
         "ф":['факт', 'фактически', 'фактор', 'фантазия', 'феномен', 'фигура', 'фильм', 'фишка', 'форма', 'формат'],
         "х":['хаос', 'характер', 'харча', 'характеристика', 'харя', 'харизма', 'хитрый', 'холод', 'холодный', 'хороший'],
         "ц":['цвет', 'цветок', 'циган', 'целесообразно', 'целесообразность', 'целостност', 'цель', 'цена', 'ценности'],
         "ч":['часто', 'часть', 'чаще', 'человек', 'через', 'четко', 'чистый', 'член'],
         "ш":['шаблон', 'шаг', 'шанс', 'шарм', 'шедевр', 'шикарен', 'широкий', 'широко', 'школа'],
         "э":["экран", "экскаватор"],
         "щ":["щавель", "щур" , "щекотка", "щука"],
         "я":['явление', 'является', 'являются', 'явно', 'ядро', 'язык', 'якобы', 'яркий'],
         "ю":['юбилей', 'юдоль', 'юзер', 'юмор', 'юнга', 'юность', 'юноша', 'юный', 'юридический']}
usedwordsIDS = {}
slova_base_people = {}
play_or_not = {}
while True:
    messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unread"})
    if messages["count"] >= 1:
        ids = messages["items"][0]["last_message"]["from_id"]
        body = messages["items"][0]["last_message"]["text"]
        if body.lower() in ["старт","/запуск"]:
            send(
                "Игра началась.\nЖду твоего слова =)")
            slova_base_people[ids] = []
            usedwordsIDS[ids] = []
            play_or_not[ids] = True
        elif body.lower() == "офф":
            if play_or_not[ids]:
                send(
                    "Бля ну ты проебал, это первое.\n Второе, пока! Жду тебя еще.\n\n Для начала новой игры , пропиши СТАРТ")
                usedwordsIDS[ids].clear()
                slova_base_people[ids].clear()
                play_or_not[ids] = False
            else:
                send("Ты еще не начал игру!!!\n\n Для списка команд пропиши /команды")
        elif body.lower() == "/admin" and ids == 447023815:
            send(str(usedwordsIDS))
        elif body.lower() == "/команды":
            send("Старт - что бы начать игру\nОфф - что бы ее закончить\nТп - обращение к админу")
        elif body.lower() == "тп":
            send("@qwertymyname")
        else:
            try:
                if play_or_not[ids]:
                    igra_not_lose = True
                    slovo_by_user = body.lower().strip()
                    send(f"Твое слово: {slovo_by_user}")
                    try:
                        if slovo_by_user in usedwordsIDS[ids] or slovo_by_user[0] != slova_base_people[ids][-1][-1] or len(str(slovo_by_user).split()) >= 2 :
                            send("Ты проебала дура")
                            slova_base_people[ids] = []
                            usedwordsIDS[ids] = []
                            igra_not_lose = False
                            play_or_not[ids] = False
                    except:
                        pass
                    usedwordsIDS[ids].append(slovo_by_user)
                    if  igra_not_lose:
                        try:
                            tmp = 0
                            for i in words[slovo_by_user[-1]]:
                                if words[slovo_by_user[-1]][tmp] in usedwordsIDS[ids]:
                                    tmp += 1
                                else:
                                    slovo = words[slovo_by_user[-1]][tmp]
                                    break
                            slova_base_people[ids].append(slovo)
                            usedwordsIDS[ids].append(slovo)
                            send(f"Мое слово: {slovo} \n Тебе на: {slovo[-1]}")
                        except:
                            send("Ты выеьал компьютер")
                            usedwordsIDS[ids].clear()
                else:
                    send("Ты еще не начал игру!!!\n\n Для списка команд пропиши /команды")
            except:
                send("Привет навичек\n\n Для списка команд пропиши /команды")
                play_or_not[ids] = False

    time.sleep(0.3)
