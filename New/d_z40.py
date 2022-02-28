# from bs4 import BeautifulSoup
# import requests
# import re
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def refined(s):
#     res = re.sub(r"\D+", "", s)
#     return res
#
# def get_page_data(html):
#     list=[]
#     soup = BeautifulSoup(html, 'lxml')
#     elements = soup.find_all("div", class_="model-price-range")
#     for el in elements:
#         name = el.find_all('span')
#         for i in name:
#             j=refined(i.text)
#             list.append(j)
#     # print(list)
#     list_new(list)
# page =0
# rez_new=0
# def list_new(list):
#     suma = 0
#     count = 0
#     global rez_new
#     for i in list:
#         if i!='':
#             # print(i)
#             suma +=int(i)
#             count +=1
#     rez = round((suma/count), 2)
#     rez_new+=rez
#     # return rez
#     print(rez)
#
# def main():
#     global page
#     for i in range(0, 15):
#         url = f"https://www.e-katalog.ru/list/206/{i}/"
#         get_page_data(get_html(url))
#         page+=1
#
# if __name__ == '__main__':
#     main()
#
# # print(page)
# print("Средняя цена", round((rez_new/page),2), "руб.")

# from bs4 import BeautifulSoup
# import requests
# import re
#
# class Parse:
#     html =""
#
#     def __init__(self, url):
#         self.url = url
#
#     def get_html(self):
#         req = requests.get(self.url).text
#         self.html = BeautifulSoup(req, 'lxml')
#
#     def parsing(self):
#         elements = self.html.find_all("div", class_="model-price-range")
#         prices = []
#         for element in elements:
#             pr1 = element.find_all('span')[0].text
#             price_1 = re.sub(r'\D+', '', pr1)
#             pr2 = element.find_all('span')[1].text
#             price_2 = re.sub(r'\D+', '', pr2)
#             if price_2.isnumeric():# содержит ли строка только числа
#                 prices.append((int(price_1)+int(price_2))/2)
#             else:
#                 prices.append(int(price_1))
#         print(prices)
#         print(f'Средняя цена {round(sum(prices)/len(prices))} руб.')
#
#     def run(self):
#         self.get_html()
#         self.parsing()
#
# pars=Parse(f'https://www.e-katalog.ru/list/206/')
# pars.run()


from bs4 import BeautifulSoup
import requests
import re

class Parse:
    html =""

    def __init__(self, url):
        self.url = url

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        elements = self.html.find_all("div", class_="model-price-range")
        prices = []
        for element in elements:
            pr1 = element.find_all('span')[0].text
            price_1 = re.sub(r'\D+', '', pr1)
            pr2 = element.find_all('span')[1].text
            price_2 = re.sub(r'\D+', '', pr2)
            if price_2.isnumeric():# содержит ли строка только числа
                prices.append((int(price_1)+int(price_2))/2)
            else:
                prices.append(int(price_1))
        return round(sum(prices)/len(prices), 2)

    def run(self):
        self.get_html()
        return self.parsing()
j=0
av=[]
for i in range(18):
    pars=Parse(f'https://www.e-katalog.ru/list/206/{i}/')
    av.append(pars.run())

print(av)
print(f'Средняя цена {round(sum(av)/len(av), 2)} руб.')


