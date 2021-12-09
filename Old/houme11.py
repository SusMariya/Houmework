# 1
a = {1: 10, 2: 20}
b = {3: 30, 4: 40}
c = {5: 50, 6: 60}
print("Объединенные словари: ", a | b | c)

#  3
x = input("Введите количество студентов: ")
i = 0
a = {}
f = []
count = 0
for i in range(int(x)):
    print(i+1, "- й", end="")
    b = input(" студент: ")
    c = int(input("Балл: "))
    a[b] = c
for i in a:
    count += a[i]
res = round(count / int(x))
print("Средний балл: ", res)
print("Студенты с баллм выше среднего: ")
for i in a:
    if a[i] > int(res):
        print(i)

# 2
a = {
    'emp1': {
        'name': 'Jhon',
        'salary': '7500'
    },
    'emp2': {
        'name': 'Emma',
        'salary': '8000'
    },
    'emp3': {
        'name': 'Brad',
        'salary': '6500'
    }
}
for x in a:
    print(x)
    for y in a[x]:
        print(y, ':', a[x][y])
print("Изменения в зарпалте Bred: с 6500 до 8500")
a['emp3']['salary'] = 8500
for x in a:
    print(x)
    for y in a[x]:
        print(y, ':', a[x][y])