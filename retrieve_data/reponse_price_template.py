import requests
from bs4 import BeautifulSoup


class ResponsePriceTemplate:

    variants = ['A1', 'A2', 'A3', 'A4']

    def __init__(self):
        pass

    @staticmethod
    def get_apple_watch_response():
        url = "https://www.rebuy.de/i,10180460/smartwatches/apple-watch-sport-42-mm-space-gray-am-sportarmband-schwarz-wi-fi"
        return ResponsePriceTemplate.__get_price__(url)

    @staticmethod
    def __get_price__(url):
        response = requests.get(url)

        parser = BeautifulSoup(response.content, 'html.parser')

        price_box = parser.find_all("div", class_="ry-product-price-box__variant")

        lowest_price = float('inf')

        price_variants_dic = {}
        for i in range(0, len(price_box)):
            price_variant = price_box[i].find_all("div", class_="ry-product-price-box-variant__title")[0]
            price_list = price_variant.find_all("span", "ry-product-price-box-radio__price")
            if len(price_list) == 0:
                price = -1
            else:
                price = float(price_list[0].text.encode('ascii', errors='ignore').replace(",", "."))

            price_variants_dic[ResponsePriceTemplate.variants[i]] = price

            if (price > 1) and (price < lowest_price):
                lowest_price = price
                if lowest_price <= 210:
                    for i in range(0, 100):
                        "HOLLY FUCK IT IS LOWER= 210... BUY BUY BUY!!!!!"

        return price_variants_dic
