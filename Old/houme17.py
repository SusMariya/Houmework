# 1
stroka = "I am learning Python. hello, WOLRD!"
stroka = input("-> ")
first = stroka.find("h")
last = stroka.rfind("h")
stroka = stroka[:first] +stroka[last+1:]
print(stroka)

# 2
stroka = "I am learning Python. hello, WOLRD!"
first = stroka.find("h")
last = stroka.rfind("h")
print(first, "", last)
stroka = stroka[:first + 1] + stroka[first + 1:last][::-1] + stroka[last:]
print(stroka)

# 3
strok = input("Введите стоку: ")
s_old = input("Ее заменяемая подстрока: ")
s_new = input("Новая подстрока: ")
print(strok.replace(s_old, s_new))

# 4
st = "Ежевику для ежат \n Принсли два ежа. \n Ежевику еле-еле \n Ежата возле ели съели"
st1 = st.split(" ")
a = []
for i in st1:
    if i[0]=='Е' or i[0] =='е':
        a.append(i)

print(st, "\nКоличество слов:", len(a))