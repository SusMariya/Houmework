# 1

a = ['red', 'green', 'blue']
b = ['#FF0000', '#008000', '#000FF']
a_b = dict(zip(a, b))
print(a_b)

# 2
d = {a: a ** 3 for a in range(1, 11)}
print(d)

# 3 -вар1
s = ['color', 'fruit', 'pet']
t = ['blue', 'apple', 'dog']
s_t = {k: v for(k, v) in zip(s, t)}
print(dict(s_t))

# 3 -вар2
print({k: v for(k, v) in list(dict(zip(['color', 'fruit', 'pet'], ['blue', 'apple', 'dog'])).items())})



