import os, os.path, time

# 1
# file = r'text_dir\f1\4.txt'
file = r'C:\Users\suspi\OneDrive\Документы\Учеба 2\Домашенее задание\d_z10.py'
if os.path.exists(file):
    print(os.path.basename(file))
    print(os.path.dirname(file))
    print(os.path.getatime(file))
else:
    print('файл не существоует')


# 2
files = ['files\\one.txt', 'files\\three.txt','files\\two.txt', 'files\\dir']
for file in files:
    print(os.path.basename(file))


# 2-1
files = ['files\\one.txt', 'files\\three.txt', 'files\\two.txt', 'files\\dir']
f = []
d = []
file_s = os.listdir('files')
print(file_s)
for i in file_s:
    x = os.path.join('files', i)
    if os.path.isfile(x):
        f.append(i)
    elif os.path.isdir(x):
        d.append(i)
print(f, d)

# 3
os.makedirs('Work\empty_files')
for root, dirs, files in os.walk('Work'):
    for i in files:
        x = os.path.join(root, i)
        if os.path.getsize(x) > 0:
            print(f'{root}\\{i}-{os.path.getsize(x)} bytes')
        else:
            print(f'{root}\\{i}')
            os.replace(x, f'Work\empty_files\{os.path.basename(i)}')
            print(f'Work\empty_files\{os.path.basename(i)}')