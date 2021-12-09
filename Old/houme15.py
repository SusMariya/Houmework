# 2
print((lambda x: (lambda y: (lambda z: x + y + z)))(2)(4)(6))


# 1

def fun_complute(n):
    def compl(x):
        return n * x
    return compl

res = fun_complute(2)
print(res(15))
print(res(20))
res = fun_complute(3)
print(res(15))
print(res(20))

# 3
stuydents = [{'name': 'Jennifer', 'final': 95},
     {'name': 'David', 'final': 92},
     {'name': 'Nikolas', 'final': 98}
     ]

res = sorted(stuydents, key = lambda item: item['name'])
print(res)
res1 = sorted(stuydents, key = lambda item: item['final'], reverse=True)
print(res1)

# 4
stuydents = [{'name': 'Jennifer', 'final': 95},
     {'name': 'David', 'final': 92},
     {'name': 'Nikolas', 'final': 98}
     ]

print(max(stuydents, key = lambda item: item['final']))
print(min(stuydents, key = lambda item: item['final']))