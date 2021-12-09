# 1
# import random as r
# mas1 = [r.randint(0, 50) for i in range(10)]
# print(mas1)
# mas1.sort(reverse = True)
# print(mas1)

# 2
# import random as r
# mas2 = [r.randint(0, 100) for i in range(20)]
# print(mas2)
# print("Сумма: ", sum(mas2))

# 3
# ch = [int(input("-> ")) for i in range(int(input("Введите элементы списка \nn = ")))]
# # print(ch)
# s = int(input("Введите число: \ns= "))
# for i in range(len(ch)):
#    if s == ch[i]:
#        print("Число присутствует в элементах списка")
#        break
# else:
#     print("Такого числа нет ")

ch = [int(input("-> ")) for i in range(int(input("Введите элементы списка \nn = ")))]
# print(ch)
s = int(input("Введите число: \ns= "))
for i in range(len(ch)):
   if s not in ch:
       print("Такого числа нет ")
       break
else:
    print("Число присутствует в элементах списка")