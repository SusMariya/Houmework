import json

x = input("Выбирете действие:\n1 - добавление данных;\n2 - удаление данных;\n3 - поиск данных;\n4 - редактирование данных;\n5 - сохранение данных;\n6 - просмотр данных - ")
class Country:
    def __init__(self, counrty, capital):
        self.country = counrty
        self.capital = capital

    def __str__(self):
        return f'Страна {self.country}: столица {self.capital}'
    list_counrty = []
    if x ==1:
        def add_country(self, country, list_counrty=None):
            list_counrty.append({self.country})

c_c=Country("Rassia", "Moskow")
