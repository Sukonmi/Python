import requests
from bs4 import BeautifulSoup

"""url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

webpage = requests.get(url)

parsed_webpage = BeautifulSoup(webpage.content, "html.parser")

paragraphs = parsed_webpage.find_all("p")

with open("wiki-python.txt", "a", encoding="utf-8") as f:
    for paragraph in paragraphs:
        f.write(paragraph.text)
        

    print("Done Writing to file")
"""

url2 = "https://books.toscrape.com/"

webpage2 = requests.get(url2)

parsed_webpage2 = BeautifulSoup(webpage2.content, "html.parser")

title = parsed_webpage2.find("h3").get_text()
prices = parsed_webpage2.find("p", class_ ="price_color").get_text()

print(title)
print(prices)

all_products = parsed_webpage2.find_all("li", class_ = "col-xs-6 col-sm-4 col-md-3 col-lg-3")

for product in all_products:
    title = product.h3.a["title"]
    link = product.h3.a["href"]
    price = product.find("p", class_ = "price_color").text
    in_stock = product.find("p", class_ = "instock availability").text
    print(f"BookTitle: {title} ==> BookPrice: {price} ==> BookLink:{link} ==> InStock:{in_stock}")