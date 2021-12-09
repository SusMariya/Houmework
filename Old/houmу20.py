# 1
f = open("houme20.txt", 'w')
f.write('Замена строки в текстововм файле; \nизменить строку в списке; \nзаписать список в файл;\n')
f.close()
del_line = int(input("Какую строку удалить (1, 2 или 3): "))
f = open("houme20.txt", 'r')
lst_f = f.readlines()
print(lst_f)
for i in range(len(lst_f)):
    if int(i) != del_line-1:
        lst_f.append(lst_f[i])

print(lst_f)
f.close()
f = open("houme20.txt", 'w')
f.writelines(lst_f)
f.close()

# # 3
f = open("houme20-1.txt", 'w')
f.write('Замена строки в текстововм файле; \nизменить строку в списке; \nзаписать список в файл;\n')
f.close()
f = open("houme20-1.txt", 'r')
lst_f = f.readlines()
print(lst_f)
lst_f1 = lst_f[::-1]
print(lst_f1)
f.close()
f = open("houme20-1.txt", 'a')
f.writelines(lst_f1)
f.close()

# 2
f = open("houme20-2.txt", 'w')
f.write('Замена строки в текстововм файле; \nизменить строку в списке; \nзаписать список в файл;\n')
f.close()
f = open("houme20-2.txt", 'r')
lst_f = f.readlines()
print(lst_f)
pos1 = int(input("Введите номер первой строки (1, 2 или 3): "))
pos2 = int(input("Введите номер втрой строки (1, 2 или 3): "))
lst_f[pos1-1], lst_f[pos2-1] = lst_f[pos2-1], lst_f[pos1-1]
print(lst_f)
f.close()
f = open("houme20-2.txt", 'w')
f.writelines(lst_f)
f.close()


# 2-1
f = open("houme20-2.txt", 'w')
f.write('Замена строки в текстововм файле; \nизменить строку в списке; \nзаписать список в файл;\n')
f.close()
f = open("houme20-2.txt", 'r')
lst_f = f.readlines()
print(lst_f)
pos1 = int(input("Введите номер первой строки (1, 2 или 3): "))
pos2 = int(input("Введите номер втрой строки (1, 2 или 3): "))
lst_f[pos1-1], lst_f[pos2-1] = lst_f[pos2-1], lst_f[pos1-1]
print(lst_f)
f.close()
f = open("houme20-2.txt", 'a')
f.writelines(lst_f)
f.close()
