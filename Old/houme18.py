
#
# mail = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
# reg = r'[а-яёa-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
# print(re.findall(reg, mail))
import re
# 3

s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78"
reg = r"([+]?[0-9-\s()]+)"
print(re.findall(reg, s))

# 1
pas = "my-p@ssw0rd"
reg = r'[\w+@-]{6,18}'
print(re.findall(reg, pas))

# 2

text = "В июне 2021 года 02/06/2021б 05/06/2021б 14/06/2021б были зафиксированы максимум ежемесячных осадков"
reg = r'[0-9]{2}/[0-9]{2}/[0-9]{4}'
print(re.findall(reg, text))
