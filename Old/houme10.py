# 1
s1 = set(input("Введите первую строку: ", ))
s2 = set(input("Введите вторую строку: ", ))
s1 -= s2
for i in s1:
    if i in s1:
        print(i, end=" ")
# 2

s = input("Введите строку: ")
count = 0
b = set("аиюяыеоыeuoia")
for i in s:
    if i in b:
        count += 1
print("Количество гласных равно:", count)

# 3
s1 = set(input("Введите первую строку: ", ))
s2 = set(input("Введите вторую строку: ", ))
s1 |= s2
print(list(s1))

# 4
s1 = set(input("Введите первую строку: ", ))
s2 = set(input("Введите вторую строку: ", ))
s3 = list(s1 ^ s2)
print("Искомыми буквами являются")
for i in s3:
    if i in s3:
        print(i, end=" ")

# 5
matim = {"Матвей", "Евгения", "Михаил", "Максим", "Наталья"}
physics = {"Максим", "Матвей", "Александр"}
print("Все призеры: ", matim | physics)
print("Призеры обеих олипиад: ", matim & physics)
matim &= physics
print("Обновленный список призеров по математике: ", matim)

# 6
def set_gen(s):

    for i in s:
        j = i-1
        while i == j:
            # i = i**j
            a.add(i)
            print(a)
    return set()


list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
# print(a)