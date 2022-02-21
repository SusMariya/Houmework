from bs4 import BeautifulSoup
import requests
import re

def get_html(url):
    r = requests.get(url)
    return r.text

def refined(s):
    res = re.sub(r"\D+", "", s)
    return res

def get_page_data(html):
    list=[]
    soup = BeautifulSoup(html, 'lxml')
    elements = soup.find_all("div", class_="model-price-range")
    for el in elements:
        name = el.find_all('span')
        for i in name:
            j=refined(i.text)
            list.append(j)
    # print(list)
    list_new(list)
page =1
rez_new=0
def list_new(list):
    suma = 0
    count = 0
    global rez_new
    for i in list:
        if i!='':
            # print(i)
            suma +=int(i)
            count +=1
    rez = round((suma/count), 2)
    rez_new+=rez
    # return rez
    # print(rez)

def main():
    global page
    for i in range(0, 15):
        url = f"https://www.e-katalog.ru/list/206/{i}/"
        get_page_data(get_html(url))
        page+=1

if __name__ == '__main__':
    main()

# print(page)
print("Средняя цена", round((rez_new/page),2), "руб.")