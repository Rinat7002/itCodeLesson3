'''
1. Напечатайте на экран сообщение о текущей дате и погоде в этот день в следующем
формате:
Сегодня … …. На улице … градусов.
День хранится в переменной day, месяц - month. Температура хранится в переменной
temperature.
Если температура ниже нуля, то добавьте следующий строкой: «Холодно, лучше
остаться дома».
'''

# Чтобы использовать библиотеку BeautifulSoup , нужно в консоль ввести:
# pip install bs4
# pip install requests

from bs4 import BeautifulSoup
import requests

from datetime import datetime, date, time
dt = datetime.today()

day = dt.day
month = dt.month
year = dt.year
temperature = -5


url = "https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%A3%D1%84%D0%B5"
response = requests.get(url)
bs = BeautifulSoup(response.text,"html.parser")

temperature = bs.find('span', 't_0')

print('Сегодня ' + str(day) + '.' + str(month) + '.' + str(year) + ', на улице ' + str(temperature.text) + ' градусов')

if int(temperature.text[1:3]) < 0:
    print('Холодно, лучше останься дома')


