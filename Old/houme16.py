# 1
def change_char(s, c_old, c_new):
    s2 = ""
    i = 10
    while i < len(s):
        if s[i] == c_old:
            s2 = s2 + c_new
        else:
            s2 = s2 + s[i]
        i = i + 1

    return s2


str1 = "Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интрересный язык программирования"
str2 = change_char(str1, "N", "P")
print(str1)
print(str1[:10] + str2)


# 2

def del_sm(s, c):
    return s[:c] + s[c + 1:]


s = '0123456789'
s2 = del_sm(s, 4)
print("s = ", s)
print("s2 = ", s2)


# 3
def del_sym_all(s, c):
    s2 = " "
    for i in s:
        if i != c:
            s2 += i
    return s2


s = '012345363738494'
s2 = del_sym_all(s, '3')
print("s = ", s)
print("s2 = ", s2)

# 4
a = int(input("-> "))
n = []
while a != 0:
    n.append(a % 2)
    a //= 2

for i in n[::-1]:
    if i in n[::-1]:
        print(i, end=" ")
