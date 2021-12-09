import requests
from bs4 import BeautifulSoup

products_to_track = [
    {
        "product_url": "https://www.flipkart.com/apple-iphone-12-mini-blue-128-gb/p/itm9b6cdec9700ee?pid=MOBFWBYZHU58PHCZ&lid=LSTMOBFWBYZHU58PHCZHCUJHW&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=browse&fm=neo%2Fmerchandising&iid=bce345e3-3518-4a8d-a50f-6b0d7050d6d8.MOBFWBYZHU58PHCZ.SEARCH&ppt=clp&ppn=mobile-phones-store&ssid=h8x1tzp00g0000001638518606431",
        "name": "iphone mini 12",
        "target_price": 50000
    },
    {
        "product_url": "https://www.flipkart.com/apple-iphone-se-black-64-gb/p/itm4d3d5718a5c95?pid=MOBFWQ6BR3MK7AUG&lid=LSTMOBFWQ6BR3MK7AUGVWESYW&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=nmenu_sub_Electronics_0_iPhone%20SE&fm=neo%2Fmerchandising&iid=2111f524-194a-49dd-b4cb-fe0dfd84fd4f.MOBFWQ6BR3MK7AUG.SEARCH&ppt=pp&ppn=pp&ssid=5vro734bbk0000001638946227983",
        "name": "iphone se",
        "target_price": 29000
    },
    {
        "product_url": "https://www.flipkart.com/apple-iphone-xr-blue-64-gb-includes-earpods-power-adapter/p/itmf9z7z4dgvug4h?pid=MOBF9Z7ZPZDS7RKH&lid=LSTMOBF9Z7ZPZDS7RKHAHDXLO&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_3&otracker=clp_banner_2_3.banner.BANNER_apple-products-store_2XLEYVFO3M8Z&fm=neo%2Fmerchandising&iid=46107851-553b-41b8-a403-2fd77a3bbdc2.MOBF9Z7ZPZDS7RKH.SEARCH&ppt=clp&ppn=apple-products-store&ssid=ap922oewg00000001638946382092",
        "name": "iphone xr",
        "target_price": 48000
    },
    {
        "product_url": "https://www.flipkart.com/apple-iphone-12-blue-128-gb/p/itm02853ae92e90a?pid=MOBFWBYZKPTZF9VG&lid=LSTMOBFWBYZKPTZF9VGIFSM7T&marketplace=FLIPKART&q=iphone&store=tyy%2F4io&srno=s_1_3&otracker=search&otracker1=search&fm=SEARCH&iid=050b4007-b378-4fd9-bcd2-5a28433785d8.MOBFWBYZKPTZF9VG.SEARCH&ppt=browse&ppn=browse&ssid=qyna0lvywg0000001638949406998&qH=0b3f45b266a97d70",
        "name": "iphone 12",
        "target_price": 62000
    },
    {
        "product_url":"https://www.flipkart.com/apple-iphone-11-black-64-gb/p/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYL0BETT&marketplace=FLIPKART&q=iphone&store=tyy%2F4io&srno=s_1_22&otracker=search&otracker1=search&fm=SEARCH&iid=050b4007-b378-4fd9-bcd2-5a28433785d8.MOBFWQ6BXGJCEYNY.SEARCH&ppt=browse&ppn=browse&ssid=qyna0lvywg0000001638949406998&qH=0b3f45b266a97d70",
        "name": "iphone 11",
        "target_price": 50000
    }
]


def give_product_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_price = soup.find("div", {"class": "_30jeq3 _16Jk6d"})
    if (product_price is None):
        product_price = soup.find("div", {"class": "_30jeq3 _16Jk6d"})
    return product_price.getText()


result_file = open('my_result_file.txt', 'w')
try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_url"))
        print(product_price_returned + " - " + every_product.get("name"))

        my_product_price = product_price_returned[1:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))

        print(my_product_price)
        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get(
                "name") + ' -  \t' + ' Available at Target Price ' + ' Current Price - ' + str(my_product_price) + '\n')

        else:
            print("Still at current price")

finally:
    result_file.close()
