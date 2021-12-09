# 3
a = tuple(input("Введите по порядку, без пробела элементы кортежа: "))
print(a)

print("Количество 2 = ", a.count("2"))
print("Количество 5 = ", a.count("5"))
print("Количество 3 = ", a.count("3"))
print("Количество 6 = ", a.count("6"))
print("Количество 1 = ", a.count("1"))


# 1
def num(tpl, el):
    g = []
    for el in tpl:
        if el > 0 and el % 13 == 0:
            g.append(el)
    if not g:
        return "no numbers"
    u = (max(g))
    return u


print(num((2, 7, 0, 3, 1, 5, -13), 13))
print(num((2, 7, 0, 3, 1, 5, -13, 13), 13))
print(num((26,), 13))
print(num((99, 99, 100, 34, -39), 13))
print(num((99, 39, 99, 100, 34), 13))

# 2
cor = ('ab', 'abcd', 'cde', 'abc', 'def')
print(cor)
el = input("Введите требуемый элемент: ", )
if el in cor:
    print('Yes')
else:
    print('No')
