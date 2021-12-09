# 1

ch = [int(input("-> ")) for i in range(int(input("n = ")))]
print(ch)
b = ch[::2]
print("Четные элементы: ", b)

# 2

ch = [int(input("-> ")) for i in range(int(input("n = ")))]
print(ch)
s = []
for i in range(len(ch)-1):
   if ch[i] < ch[i+1]:
       s.append(ch[i+1])
print(s)

# 3

a = [int(input("-> ")) for i in range(int(input("n = ")))]
print(a)
for i in range(len(a)):
    for x in range(len(a)):
        if i != x and a[i] == a[x]:
            break
    else:
        print(a[i], end=" ")


