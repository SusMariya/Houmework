#1
name = input("What is your name? ")
age = input("How old are you? ")
city = input("Where are you live? ")
print("This is a {0}. \nIt s {1}. \nHe lives in {2}.".format(name, age, city))

#2
print("Решите пример: 4 * 100 - 54")
a = input("Ваш ответ: ")
print("Правильный ответ: 346. \nВаш ответ: ", a)

#3
num = int(input("Введите целое число: "))
if num%2 == 0:
    print("Число ", num, "- четное")
else:
    print("Число ", num, "- нечетное")