# вар 1
class Temperature:
    count = 0

    @staticmethod
    def tem_C_F(a):
        Temperature.count += 1
        return (a*9/5)+32

    @staticmethod
    def tem_F_C(b):
        Temperature.count += 1
        return (b - 32)*5/9

print("Переводим из градусы Цельсия в Форенгейты: ", Temperature.tem_C_F(1))
print("Переводим из Форенгейтов в градусы Цельсия: ", round(Temperature.tem_F_C(33), 2))
print("Переводим из Форенгейтов в градусы Цельсия: ", round(Temperature.tem_F_C(45), 2))
print("Количество переводов", Temperature.count)

# вар 2
#
class Temperature:
    count = 0

    @staticmethod
    def tem_C_F(a):
        if isinstance(a, (int, float)):
            Temperature.count += 1
            return (a * 9 / 5) + 32
        else:
            return ("Неверно задан формат")

    @staticmethod
    def tem_F_C(b):
        if isinstance(b, (int, float)):
            Temperature.count += 1
            return (b - 32) * 5 / 9
        else:
            return ("Неверно задан формат")


print("Переводим из градусы Цельсия в Форенгейты: ", Temperature.tem_C_F(13))
print("Переводим из Форенгейтов в градусы Цельсия: ", round(Temperature.tem_F_C(33), 2))
print("Количество переводов", Temperature.count)
