import os, os.path, time

# 1
# # file = r'text_dir\f1\4.txt'
# file = r'C:\Users\suspi\OneDrive\Документы\Учеба 2\Домашенее задание\d_z10.py'
# if os.path.exists(file):
#     print(os.path.basename(file))
#     print(os.path.dirname(file))
#     print(os.path.getatime(file))
# else:
#     print('файл не существоует')


# 2
files = ['files\\one.txt', 'files\\three.txt','files\\two.txt', 'files\\dir']
for file in files:
    print(os.path.basename(file))


# 3


