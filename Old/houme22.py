# 1
f1 = open('text1.txt', 'w+')
f1.write('Hello!')
f2 = open('text2.txt', 'w+')
f2.write('World!')
f1.close()
f2.close()
f1 = open('text1.txt', 'r')
f2 = open('text2.txt', 'r')
f3 = open("text3.txt", 'w+')
f3.write(f1.read()+" "+f2.read())
f3.close()
f1.close()
f2.close()

# 2
lines = 0
words = 0
letters = 0
f = open('Houme22.txt', 'w+')
f.write('первая строка')
f.close()
f = open('Houme22.txt', 'a')
f.write('\nстрока номер два')
f.close()
f = open('Houme22.txt', 'a')
f.write('\nтретья строка')
f.close()
f = open('Houme22.txt', 'a')
f.write('\n4 строка')
f.close()
for line in open('Houme22.txt', 'r'):
    lines +=1
    letters = len(line)
    words = len(line.split(' '))
    print(line, letters, " симв. ", "\n", words, " сл.")
print(lines, " ст.")

