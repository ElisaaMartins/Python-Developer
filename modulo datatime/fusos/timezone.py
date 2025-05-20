# lidar com fusos horários, sem a biblioteca PYTZ

from datetime import datetime, timedelta, timezone

# Criando datetime com timezone
data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(data_oslo)
print(data_sao_paulo)

d = datetime.datetime.now(timezone(timedelta(hours=-3), "BRT"))
print(d) #2023-07-19 10:20:00-03:00
