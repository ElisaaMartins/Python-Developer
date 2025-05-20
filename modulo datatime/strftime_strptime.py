# converter e formatar datas e horas
# 'strftime' (string format time) 
# 'strptime' (string parse time)

from datetime import datetime

""" data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))

d = datetime.datetime.now() """

#formatando data e hora
print(d.strftime("%d/%m/%Y %H:%M:%S")) # 20/10/2023 10:20:00

#convertendo string para datetime
date_string = "2023-10-20 10:20"
d = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M")
print(d) # 2023-10-20 10:20:00