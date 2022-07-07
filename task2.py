import requests
from bs4 import BeautifulSoup


animals = {}


def get_animals(url):
    """Парсим вики и сохраняем данные в словаре
    """
    page = requests.get(url).text

    while True:
        fl = True
        soup = BeautifulSoup(page, 'lxml')
        uls = soup.find('div', class_='mw-category mw-category-columns').find_all('ul')
        for ul in uls:
            names = ul.find_all('a') #Парсим названия животных
            for name in names:
                if name.get('title')[0] in animals: #Если в словаре есть первая буква животного, добавляем 1
                    animals[name.get('title')[0]] += 1
                else: #иначе добавляем букву в словарь
                    animals[name.get('title')[0]] = 1
        links = soup.find('div', id='mw-pages').find_all('a')
        for a in links: #проверяем есть ли ссылка на следующую страницу
            if a.text == 'Следующая страница':
                url = 'https://ru.wikipedia.org/' + a.get('href')
                page = requests.get(url).text
                fl = False
        if fl: break # если ссылки не было, выходим из цикла


if __name__ == "__main__":
    get_animals("https://inlnk.ru/jElywR")
    for i in animals:
        print(i, ':', animals[i])




