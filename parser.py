import requests
from bs4 import BeautifulSoup

url = input("Введите ссылку на товар: ")

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

title = soup.find("h1").text.strip()
price = soup.find("meta", {"itemprop": "price"})["content"]

print("Название:", title)
print("Цена:", price, "руб.")
