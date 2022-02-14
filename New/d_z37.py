import json

city={}
class Country:
    def __init__(self, counrty):
        self.country = counrty

    def __str__(self):
        return f'Список: {self.country}'
    def add_country(self):
        key = input("Введите новую страну: ")
        value = input("Введите столицу страны: ")
        self.country[key] = value
        return self.country

    def del_country(self):
        key =str(input("Какую страну удалить: "))
        self.country.pop(key)
        return self.country

    def edit_country(self):
        key = input("Какую страну отредактировать: ")
        if key in self.country:
            value = input("Введите новую столицу:")
            self.country[key] = value
        else:
            print("Такой мтраны нет в списке: ")
            edit = input("Какая столица в данной стране?: ")
            self.country[key] = edit
            print("Стана и столица включены: ")

    def seach_counrty(self):
        key = input("Какую страну найти: ")
        if key in self.country:
            print(f'Столица {self.country[key]}, страны {key}.')
        else:
            print("Такой страны нет в списке")

    def dump_to_json(self):
        try:
            data =json.load(open('file_city.json'))
        except FileNotFoundError:
            data = {}

        data.update(self.country)
        with open('file_city.json', 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=5)

    def load_file(self):
        with open('file_city.json', 'r') as f:
            print(json.load(f))
    def print_info(self):
        print(self.country)

c_c = Country(city)
while True:
    enter = input("Выбирете действие:\n1 - добавление данных;\n2 - удаление данных;\n3 - поиск данных;\n4 - редактирование данных;\n5 - сохранение данных;\n6 - просмотр данных\nваш выбор- ")
    if enter == "1":
        c_c.add_country()
        c_c.print_info()
    elif enter =="2":
        c_c.del_country()
        c_c.print_info()
    elif enter =="3":
        c_c.seach_counrty()
    elif enter =='4':
        c_c.edit_country()
        c_c.print_info()
    elif enter == '5':
        c_c.dump_to_json()
        c_c.load_file()
    elif enter =='6':
        c_c.load_file()

    else:
        break

