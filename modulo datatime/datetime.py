from datetime import date, datetime, time

data = date(2023, 7, 10)
print(data)
print(date.today())


data_hora = datetime(2023, 7, 10)
print(data_hora)
print(datetime.today())

hora = time(10, 20, 0)
print(hora)

d =  datetime.date(2023, 7, 19)
print(d) #2023-07-19

# criando data e hora
d = datetime.datetime(2023, 7, 19, 10, 20)
print(d) #2023-07-19 10:20:00

# adicionando uma semana
d = d + datetime.timedelta(weeks=1)
print(d) #2023-07-26 10:20:00
