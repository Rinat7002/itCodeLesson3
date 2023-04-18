'''
1. Напечатайте на экран сообщение о текущей дате и погоде в этот день в следующем
формате:
Сегодня … …. На улице … градусов.
День хранится в переменной day, месяц - month. Температура хранится в переменной
temperature.
Если температура ниже нуля, то добавьте следующий строкой: «Холодно, лучше
остаться дома».
'''

from datetime import datetime, date, time
dt = datetime.today()

day = dt.day
month = dt.month
year = dt.year
temperature = -5

print('Сегодня ' + str(day) + '.' + str(month) + '.' + str(year) + ', на улице ' + str(temperature) + ' градусов')

if temperature < 0:
    print('Холодно, лучше останься дома')


