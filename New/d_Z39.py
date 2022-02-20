import requests
import csv
from bs4 import BeautifulSoup
import re

def get_html(url):
    r = requests.get(url)
    return r.text

def refined(s):
    res = re.sub(r"\D+", "", s)
    return res


def write_csv(data):
    with open('intellekt.csv', 'a') as f:
        writer = csv.writer(f, delimiter =";", lineterminator ="\r")
        writer.writerow((data['name'], data["url"]))

def get_data(html):
    soup=BeautifulSoup(html, "lxml")
    s=soup.find_all("section", class_="block")[10]
    # print(s)
    plugins =s.find_all('p')
    # print(plugins)
    for plugin in plugins:
        name = plugin.find('a').text
        url1 = plugin.find('a').get('href')
        # print(name)
        # print(url1)
        data = {'name': name, "url": url1}
        write_csv(data)
    return len(plugins)

def main():
    url = 'https://fondnid.ru/'
    get_data(get_html(url))


if __name__ =='__main__':
    main()

