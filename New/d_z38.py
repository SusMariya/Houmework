import csv

data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London'],
        ['sw2', 'Cisco', '3850', 'Liverpool'],
        ['sw3', 'Cisco', '3650', 'Liverpool'],
        ['sw4', 'Cisco', '3650', 'London']]

with open("sw_data.csv", "w") as f:
    writer = csv.writer(f, delimiter=";", lineterminator="\r")

    for row in data:
        writer.writerow(row)

with open("sw_data.csv") as f:
    reader = list(csv.reader(f))
    for row in reader:
        print(row)
