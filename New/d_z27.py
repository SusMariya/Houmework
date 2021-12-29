class Account:
    rate_usd = 0.013
    rate_euro = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_euro = "EURO"

    def __init__(self, surname="Д", nam="#123", persent= 0.0, value = 0):
        self.__surname = surname # фамилия владельца
        self.__nam = nam # номер счета
        self.__persent = persent # процент начисления
        self.__value = value # сумма в рублях

    def __del__(self):
        return (f'Счет {self.__nam} принадлежащий {self.__surname} был закрыт')

    def set_surname(self, surname):
        self.__surname = surname

    def set_nam(self, nam):
        self.__nam = nam

    def set_persent(self, persent):
        self.__persent = persent

    def set_value(self, value):
        self.__value = value

    def get_surname(self):
        return self.__surname

    def get_nam(self):
        return self.__nam

    def get_persent(self):
        return self.__persent

    def get_value(self):
        return self.__value

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_euro_rate(cls, rate):
        cls.rate_euro = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        return usd_val

    def convert_to_euro(self):
        return Account.convert(self.__value, Account.rate_euro)

    def add_persent(self):
        self.__value +=self.__value *self.__persent
        return self.__value

    def withdraw_money(self, val):
        if val >self.__value:
            return f"К сожалению у вас нет такой суммы {val} {Account.suffix}"
        else:
            self.__value-=val
            return (f"{val} {Account.suffix} были успешно сняты!")

    def add_money(self, val):
        self.__value +=val
        return (f"{val} {Account.suffix} были успешно добавлены!")

acc = Account()
acc.set_surname("Долгих")
acc.set_nam("#12345")
acc.set_persent(0.03)
acc.set_value(1000)
print("Счет ", acc.get_nam(), " принадлежащий ", acc.get_surname(), " был открыт")
print("*"*50)
print("Информация о счете\n", "-"*20)
print(acc.get_nam(), "\nВладелец: ", acc.get_surname(), "\nТекущий балланс: ", acc.get_value(), Account.suffix, "\nПрценты: ", acc.get_persent()*100, "%")
print("\nСостояние счета: ", acc.convert_to_usd(), Account.suffix_usd)
print("Состояние счета: ", acc.convert_to_euro(), Account.suffix_euro)
print("\nПроценты были успешно начислены!", "\nТекущий балланс: ", acc.add_persent(), Account.suffix)
acc1 = acc.withdraw_money(3000)
print("\n", acc1, "\nТекущий балланс: ", acc.get_value(), Account.suffix)
acc1 = acc.withdraw_money(100)
print("\n", acc1, "\nТекущий балланс: ", acc.get_value(), Account.suffix)
acc2 = acc.add_money(5000)
print("\n", acc2, "\nТекущий балланс: ", acc.get_value(), Account.suffix)
acc.set_surname("Дюма")
acc.set_persent(0.05)
print("\n", acc.get_persent()*100, "%", "были успешно начислены!", "\nТекущий балланс: ", acc.add_persent(), Account.suffix)
print("\nИнформация о счете", acc.get_nam(), "\nВладелец: ", acc.get_surname(), "\nТекущий балланс: ", acc.get_value(), Account.suffix, "\nПрценты: ", acc.get_persent()*100, "%")
print("*"*50, "\n",acc.__del__())

# при get и set переписывала основной код, а при добавлении @property в основнм коде ничего не меняла
class Account:
    rate_usd = 0.013
    rate_euro = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_euro = "EURO"

    def __init__(self, surname, nam, persent, value=0):
        self.__surname = surname  # фамилия владельца
        self.__nam = nam  # номер счета
        self.__persent = persent  # процент начисления
        self.__value = value  # сумма в рублях
        print(f'Счет #{self.nam} принадлежащий {self.surname} был открыт')
        print("*" * 50)

    def __del__(self):
        print(f'Счет #{self.nam} принадлежащий {self.surname} был закрыт')

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def nam(self):
        return self.__nam

    @nam.setter
    def nam(self, nam):
        self.__nam = nam

    @property
    def persent(self):
        return self.__persent

    @persent.setter
    def persent(self, persent):
        self.__persent = persent

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_euro_rate(cls, rate):
        cls.rate_euro = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def edit_ower(self, surname):  # смена владельца счета
        self.surname = surname

    def convert_to_usd(self):  # перевод в доллары
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}")

    def convert_to_euro(self):  # перевод в евро
        euro_val = Account.convert(self.value, Account.rate_euro)
        print(f"Состояние счета: {euro_val} {Account.suffix_euro}")

    def add_persent(self):
        self.value += self.value * self.persent
        print("Проценты были успешно начислены!")
        self.print_balans()

    def withdraw_money(self, val):  # сняние заданной суммы
        if val > self.value:
            print(f"К сожалению у вас нет такой {val} {Account.suffix}")
        else:
            self.value -= val
            print(f"{val} {Account.suffix} были успешно сняты!")
        self.print_balans()

    def add_money(self, val):
        self.value += val
        print(f"{val} {Account.suffix} были успешно добавлены!")
        self.print_balans()

    def print_balans(self):
        print(f"Текущий юаланс: {self.value} {Account.suffix}")

    def print_info(self):  # вывод информации о счете
        print("Информация о счете")
        print("-" * 20)
        print(f'#{self.nam}')
        print(f'Владелец: {self.surname}')
        self.print_balans()
        print(f"Проценты: {self.persent:.0%}")
        print("-" * 20)


acc = Account("Долгих", 12345, 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_euro()

Account.set_usd_rate(2)
Account.set_euro_rate(3)
print()
acc.convert_to_usd()
acc.convert_to_euro()
print()
acc.edit_ower("Дюма")
acc.print_info()
print()
acc.add_persent()
print()
acc.withdraw_money(3000)
acc.withdraw_money(100)
print()
acc.add_money(5000)
print()
acc.withdraw_money(3000)