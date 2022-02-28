def add_title(title):
    def wraper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" *50)
            return output
        return wrap
    return wraper



class UserInterfase:
    @add_title("Редактирование данных католога фильмов")
    def wait_user_answer(self):
        print("Действие с фильмами: ")
        print("1 - добавление фильма"
              "\n2 - просмотр фильмов"
              "\n3 - просмотр отдельного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title("Создание фильма: ")
    def add_user_aticals(self):
        dict_atical={
            "название фильма": None,
            "жанр": None,
            "режиссер": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None,
        }
        for key in dict_atical:
            dict_atical[key] = input(f"Введите {key} фильма: ")
        return dict_atical

    @add_title("Каталог фильмов:")
    def show_all_aticals(self, aticals):
        for ind, atical in enumerate(aticals, 1):
            print(f'{ind}. {atical}')

    @add_title("Ввод названия фильма:")
    def get_user_atical(self):
        user_atical = input("Введите название фильма: ")
        return user_atical

    @add_title("Промотр отдельного фильма:")
    def show_single_atical(self, atical):
        for key in atical:
            print(f"{key} фильма - {atical[key]}")

    @add_title("Сообщение об ошибке")
    def show_incorrect_title_error(self, user_title):
        print(f'ФИльма с названием {user_title} не существует')

    @add_title("Удаление фильма:")
    def remove_single_atical(self, atical):
        print(f"Фильм {atical} был удален")

    @add_title("Сообщение об ошибке")
    def show_incorrect_answer_error(self, user_answer):
        print(f'Варианта {user_answer} не существует')