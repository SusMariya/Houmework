class Book:
    name = "Book_name"
    year = "year_release"
    publisher = "publisher_Book"
    genre = "genre_Book"
    author = "author_Book"
    prise = "prise_Book"

    def print_info(self):
        print(" История одной книги ".center(40, "*"))
        print(f"Название книги: {self.name}\nГод издания: {self.year}\n"
              f"Издательство: {self.publisher}\nЖанр: {self.genre}\nАвтор: {self.author}\n"
              f"Цена:{self.prise}")
        print("*" * 40)

    def input_info(self, name, year, publisher, genre, author, prise):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.prise = prise

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_publisher(self):
        return self.publisher

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_prise(self, prise):
        self.prise = prise

    def get_prise(self):
        return self.prise


book1 = Book()
book1.print_info()
book1.input_info("Малыш и Карлсон", "2020", "Азбука", "повесть", "Астрид Линдгрен", "348 р.")
book1.print_info()
book1.set_name("Маленький принц")
book1.set_year("2021")
book1.set_publisher("Эксмо,Эксмодетство")
book1.set_genre("философская сказка")
book1.set_author("Антуан де Сент-Экзюпери")
book1.set_prise("224 р.")
book1.print_info()
