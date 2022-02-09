import json
from random import choice


def gen_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'd', 'b', 'e', 'f', 'e', 'g']
    nam = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nam)
    person = {
        'name': name,
        'tel': tel
    }
    return person, tel


def write_json(person_dict, num):
    try:
        data = json.load(open('person1.json'))
    except FileNotFoundError:
        data = {}

    data[num] = person_dict
    with open('person1.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person()[0], gen_person()[1])

with open('person1.json', 'r') as f:
    print(json.load(f))